from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

import templates

router = APIRouter()


@router.get("/")
def example_2_page(request: Request):
    return templates.example_2_page(request)


@router.put("/increment")
def increment(currentValue: str = Form(...)):
    print(f"Received a current value of {currentValue}")
    new_value = int(currentValue) + 1
    print(f"New value is {new_value}")

    return HTMLResponse(
        f"""
        {new_value} 
        <input type="hidden" name="currentValue" id="currentValue" value="{new_value}" />
        """
    )


@router.put("/decrement")
def decrement(currentValue: str = Form(...)):
    print(f"Received a current value of {currentValue}")
    new_value = int(currentValue) - 1
    print(f"New value is {new_value}")

    return HTMLResponse(
        f"""
        {new_value} 
        <input type="hidden" name="currentValue" id="currentValue" value="{new_value}" />
        """
    )
