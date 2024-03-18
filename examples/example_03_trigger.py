from fastapi import APIRouter, Form, Query, Request
from fastapi.responses import HTMLResponse

import asyncio
from datetime import datetime

from jinja2 import Template

import templates

router = APIRouter()


@router.get("/")
def example_3_page(request: Request):
    return templates.example_3_page(request)


@router.post("/bind")
def bind_variable(inputName: str | None = Form(None)):
    if not inputName:
        inputName = "-- no input --"

    return HTMLResponse(
        f"""
            <input 
                id="bind-target"
                class="form-control"
                disabled 
                value="{inputName}" 
                type="text"
            >
    """
    )


@router.get("/time")
async def get_time():
    await asyncio.sleep(2.5)

    current_time = datetime.now().strftime("%A, %B %d, %Y %H:%M:%S")

    return HTMLResponse(
        f"""
        <p id="current-time">Current time is: {current_time}</p>
    """
    )


all_animals = [
    "Aardvark",
    "Binturong",
    "Capuchin Monkey",
    "Dugong",
    "Echidna",
    "Fennec Fox",
    "Giraffe",
    "Hedgehog",
    "Iguana",
    "Jackalope",
    "Kinkajou",
    "Lemur",
    "Mongoose",
    "Narwhal",
    "Ocelot",
    "Pangolin",
    "Quokka",
    "Red Panda",
    "Sloth",
    "Tarsier",
]


@router.get("/search")
async def get_search_results(search: str | None = Query(None)):
    selected_animals = all_animals

    if search:
        selected_animals = [a for a in all_animals if search in a.lower()]

    return HTMLResponse(
        Template(
            """
            {% for a in animals %}
                <span class="badge rounded-pill text-bg-dark">{{ a }}</span>
            {% endfor %}
        """
        ).render(animals=selected_animals)
    )
