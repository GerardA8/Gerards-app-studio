"""Server-enforced admin page and API for APP-003."""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse, Response

from app import security

router = APIRouter()


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request) -> Response:
    """Redirect anonymous visitors and forbid members from the admin page."""
    try:
        user = security.require_admin(request)
    except HTTPException as error:
        if error.status_code == 401:
            return RedirectResponse("/login", status_code=303)
        if error.status_code != 403:
            raise
        return request.app.state.templates.TemplateResponse(
            request=request,
            name="admin_denied.html",
            context={},
            status_code=403,
        )
    return request.app.state.templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"user": user},
    )


@router.get("/api/admin")
def admin_api(request: Request) -> dict[str, str]:
    """Expose the admin API only to a currently authorized admin."""
    security.require_admin(request)
    return {"status": "ok"}
