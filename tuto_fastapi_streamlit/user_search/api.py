"""API module."""
import json

from fastapi import FastAPI

app = FastAPI()

USERS = json.dumps([
    {"id": 1, "nom": "Dupont", "prénom": "Jean", "email": "jean.dupont@example.com", },
    {"id": 2, "nom": "Martin", "prénom": "Marie", "email": "marie.martin@example.com", },
    {"id": 3, "nom": "Robert", "prénom": "Paul", "email": "paul.robert@example.com", },
    {"id": 4, "nom": "Ignace", "prénom": "Simon", "email": "simon.robert@example.com", },
    {"id": 5, "nom": "Lancelot", "prénom": "Nicolas", "email": "nicolas.lancelot@example.com", },
    {"id": 7, "nom": "Baudin", "prénom": "Raphaelle", "email": "raphaelle.baudin@example.com", },
    {"id": 8, "nom": "Lusignet", "prénom": "Josseline", "email": "josseline.lusignet@example.com", },
])


@app.get("/")
def root():
    """ Display the home page.

    Returns:
        dict: {"message": .....}

    """
    return {"message": "API for searching users"}


@app.get("/get_data")
async def load_data():
    """Load all data

    Returns:
        json with orient "records" like [{{column -> value}}, ... , {{column -> value}}]

    """
    return USERS
