from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, FastAPI, Form, HTTPException, Request
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from services.contact import Contact

import templates

Contact.load_db()

middleware = [Middleware(SessionMiddleware, secret_key="super-secret")]

app = FastAPI(middleware=middleware)
app.mount("/public", StaticFiles(directory="public"), name="public")


ui_router = APIRouter(include_in_schema=False)


@ui_router.get("/")
def read_root():
    return RedirectResponse("/contacts")


@ui_router.get("/contacts")
def contacts(request: Request):
    search = request.query_params.get("q")
    if search is not None:
        contacts = Contact.search(search)
    else:
        contacts = Contact.all()

    return templates.index(request, searched=search, contacts=contacts)


@ui_router.get("/contacts/new")
def contacts_new_get(request: Request):
    return templates.new(request, contact=Contact())


@ui_router.post("/contacts/new")
def contacts_new(
    request: Request,
    first_name: str | None = Form(None),
    last_name: str | None = Form(None),
    phone: str | None = Form(None),
    email: str | None = Form(None),
):
    c = Contact(None, first_name, last_name, phone, email)

    if c.save():
        templates.flash(request, "Created New Contact!")
        return RedirectResponse("/contacts", status_code=303)
    else:
        return templates.new(request, contact=c)


@ui_router.get("/contacts/{contact_id}")
def contacts_view(request: Request, contact_id: int):
    contact = Contact.find(contact_id)
    if not contact:
        return HTTPException(404)

    return templates.show(request, contact=contact)


@ui_router.get("/contacts/{contact_id}/edit")
def contacts_edit_get(request: Request, contact_id: int):
    contact = Contact.find(contact_id)

    if not contact:
        raise HTTPException(404)

    return templates.edit(request, contact=contact)


@ui_router.post("/contacts/{contact_id}/edit")
def contacts_edit_post(
    request: Request,
    contact_id: int,
    first_name: str | None = Form(...),
    last_name: str | None = Form(...),
    phone: str | None = Form(...),
    email: str | None = Form(...),
):
    c = Contact.find(contact_id)
    if not c:
        raise HTTPException(404)
    c.update(
        first_name,
        last_name,
        phone,
        email,
    )
    if c.save():
        templates.flash(request, "Updated Contact!")
        return RedirectResponse("/contacts/" + str(contact_id), status_code=303)
    else:
        return templates.edit(request, contact=c)


@ui_router.post("/contacts/{contact_id}/delete")
def contacts_delete(request: Request, contact_id: int):
    contact = Contact.find(contact_id)
    if not contact:
        raise HTTPException(404)
    contact.delete()

    templates.flash(request, "Deleted Contact!")
    return RedirectResponse("/contacts", status_code=303)


app.include_router(ui_router)
