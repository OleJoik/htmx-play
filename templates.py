from typing import Any
from fastapi import Request
from fastapi.templating import Jinja2Templates

from services.contact import Contact


_templates = Jinja2Templates(directory="templates")


def index(request: Request, searched: str | None, contacts: list[Contact]):
    return _templates.TemplateResponse(
        name="index.html",
        context={"request": request, "contacts": contacts, "searched": searched},
    )


def new(request: Request, contact: Contact):
    return _templates.TemplateResponse(
        name="new.html",
        context={"request": request, "contact": contact},
    )


def show(request: Request, contact: Contact):
    return _templates.TemplateResponse(
        name="show.html",
        context={"request": request, "contact": contact},
    )


def edit(request: Request, contact: Contact):
    return _templates.TemplateResponse(
        name="edit.html",
        context={"request": request, "contact": contact},
    )


def example_1_page(request: Request):
    return _templates.TemplateResponse(
        name="examples/01-button-click.html",
        context={"request": request},
    )


def flash(request: Request, message: Any, category: str = "primary") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
        request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request):
    return request.session.pop("_messages") if "_messages" in request.session else []


_templates.env.globals["get_flashed_messages"] = get_flashed_messages
