"""API with FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel

from calculator import calculate


class UserInput(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.post("/calculate")
def operate(user_input: UserInput):
    """

    Args:
        user_input: user input parameters

    Returns:
        Union[float, str]

    """
    result = calculate(user_input.operation, user_input.x, user_input.y)
    return result
