"""Member signup, login, and session routes for APP-002."""

from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, SignupInput

router = APIRouter()


def _form_template(
    request: Request,
    name: str,
    context: dict[str, object],
    status_code: int = 200,
) -> Response:
    """Render a form with a same-origin CSRF token without reflecting secrets."""
    csrf_response = Response()
    context["csrf_token"] = security.csrf_token(request, csrf_response)
    template = request.app.state.templates.TemplateResponse(
        request=request,
        name=name,
        context=context,
        status_code=status_code,
    )
    template.headers["Cache-Control"] = "no-store"
    template.raw_headers.extend(
        (name, value)
        for name, value in csrf_response.raw_headers
        if name.lower() == b"set-cookie"
    )
    return template


def _public_user(user: dict[str, str]) -> dict[str, str]:
    """Expose identity fields, never session identifiers."""
    return {key: user[key] for key in ("id", "username", "role")}


@router.get("/signup", include_in_schema=False)
def signup_page(request: Request) -> Response:
    """Show the browser signup form."""
    return _form_template(request, "signup.html", {"username": "", "error": None})


@router.post("/signup", include_in_schema=False)
async def signup_form(request: Request) -> Response:
    """Create a member from the form and send them to the shared login flow."""
    submitted = dict(await request.form())
    csrf_token = submitted.pop("csrf_token", None)
    security.require_csrf(request, csrf_token if isinstance(csrf_token, str) else None)
    try:
        credentials = SignupInput.model_validate(submitted)
    except ValidationError:
        return _form_template(
            request,
            "signup.html",
            {"username": "", "error": "Enter a valid username and passphrase."},
            status_code=422,
        )
    try:
        security.limit_signup(request)
        security.signup(
            request.app.state.settings,
            credentials.username,
            credentials.password,
        )
    except HTTPException as error:
        return _form_template(
            request,
            "signup.html",
            {"username": credentials.username, "error": error.detail},
            status_code=error.status_code,
        )
    return RedirectResponse("/login?registered=1", status_code=303)


@router.get("/login", include_in_schema=False)
def login_page(request: Request) -> Response:
    """Show the browser login form and a fixed post-signup notice."""
    notice = (
        "Account created. Please log in."
        if request.query_params.get("registered") == "1"
        else None
    )
    return _form_template(
        request,
        "login.html",
        {"username": "", "error": None, "notice": notice},
    )


@router.post("/login", include_in_schema=False)
async def login_form(request: Request) -> Response:
    """Authenticate the form through the same helper used by the REST endpoint."""
    submitted = dict(await request.form())
    csrf_token = submitted.pop("csrf_token", None)
    security.require_csrf(request, csrf_token if isinstance(csrf_token, str) else None)
    try:
        credentials = LoginInput.model_validate(submitted)
    except ValidationError:
        return _form_template(
            request,
            "login.html",
            {
                "username": "",
                "error": "Enter a valid username and password.",
                "notice": None,
            },
            status_code=422,
        )

    redirect = RedirectResponse("/dashboard", status_code=303)
    try:
        security.login(
            request,
            redirect,
            credentials.username,
            credentials.password,
        )
    except HTTPException as error:
        return _form_template(
            request,
            "login.html",
            {
                "username": credentials.username,
                "error": error.detail,
                "notice": None,
            },
            status_code=error.status_code,
        )
    return redirect


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request) -> Response:
    """Redirect anonymous visitors and render only the current member's identity."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    return _form_template(
        request,
        "dashboard.html",
        {"user": _public_user(user)},
    )


@router.post("/logout", include_in_schema=False)
async def logout_form(request: Request) -> Response:
    """Validate form CSRF, revoke the server session, and return home."""
    form = await request.form()
    csrf_token = form.get("csrf_token")
    security.require_csrf(request, csrf_token if isinstance(csrf_token, str) else None)
    redirect = RedirectResponse("/", status_code=303)
    security.logout(request, redirect)
    return redirect


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response) -> dict[str, str]:
    """Start or reuse a pre-login session for same-origin API form protection."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post("/api/signup", status_code=201)
def api_signup(request: Request, credentials: SignupInput) -> dict[str, str]:
    """Create a member after CSRF and signup-rate-limit checks."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings,
        credentials.username,
        credentials.password,
    )


@router.post("/api/login")
def api_login(
    request: Request, credentials: LoginInput, response: Response
) -> dict[str, str]:
    """Issue an HttpOnly session cookie without returning a token in JSON."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    return _public_user(
        security.login(
            request,
            response,
            credentials.username,
            credentials.password,
        )
    )


@router.get("/api/me")
def api_me(request: Request) -> dict[str, str]:
    """Return the authenticated member's public identity or 401."""
    return _public_user(security.require_user(request))


@router.post("/api/logout")
def api_logout(request: Request, response: Response) -> dict[str, str]:
    """Revoke the server-side session after validating the current CSRF token."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.logout(request, response)
    return {"status": "ok"}
