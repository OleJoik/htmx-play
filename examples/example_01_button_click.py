from fastapi import APIRouter, Request

import templates

router = APIRouter()


@router.get("/")
def example_1_page(request: Request):
    return templates.example_1_page(request)


@router.get("/button-click")
def get_button_click():
    print("GET button clicked")
    return "GET"


@router.post("/button-click")
def post_button_click():
    print("POST button clicked")
    return "POST"


@router.put("/button-click")
def put_button_click():
    print("PUT button clicked")
    return "PUT"


@router.patch("/button-click")
def patch_button_click():
    print("PATCH button clicked")
    return "PATCH"


@router.delete("/button-click")
def delete_button_click():
    print("DELETE button clicked")
    return "DELETE"
