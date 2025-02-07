""" First API tutorial with FastAPI."""
from typing import Union

from fastapi import FastAPI

app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/home")
def root():
    """ Display the home page.

    Returns:
        dict: {"message": .....}

    """
    return {"message": "Welcome to my page!"}


@app.get("/items/{item_id}")
async def read_item(item_id: Union[int, str]) -> dict:
    """Return item's descriptions.

    Args:
        item_id (Union[int, str]): item id

    Returns:
        dict: dictionary with key name equal to 'item_id'

    """

    return {"item_id": item_id}
