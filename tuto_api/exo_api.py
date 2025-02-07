""" First API tutorial with FastAPI."""
from typing import Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(docs_url="/docs", redoc_url="/redoc")


# Exo 1 ==============================================================

@app.get("/read_items/{item_id}")
def read_items(item_id: int, q_name: Optional[str] = None):
    """ Return items' values

    Args:
        item_id (int):
        q_name (Optional[str]):

    Returns:
        dict: dictionary of query parameters

    """
    return {"items": item_id, "q_name": q_name}


# Exo 2 ==============================================================
# Query parameters ---------------------------
@app.get("/pricer/{price}")
def compute_total_price(price: float, tax: Optional[float] = None):
    """Compute price with tax.

    Args:
        price (float): item's price
        tax (Optional[float]): default is None, tax value

    Returns:
        Union[str, dict]:
            If tax is in [0:1]: keys are: `price`, `tax`, `price_with_tax`
            Else, we return a string with

    """
    if tax and (tax < 0 or tax):
        return f"Tax must be in range `[0:1]`, but you gave {tax}"
    else:
        price_with_tax = price * (1 + tax)
        return {"price": price,
                "tax": tax,
                "price_with_tax": price_with_tax,
                }


# Pydantic version ---------------------------
# Data model & Body request

class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: float
    tax: Union[float, None] = None


@app.post("/pricer_item/")
def compute_total_price_with_Pydantic(item: Item):
    """ Compute price with tax.

    Args:
        item: item details

    Returns:
        dict

    """
    item_dict = item.dict()
    tax = item.tax
    if tax and (tax < 0 or tax > 1.):
        return f"Tax must be in range 0 and 1, but you gave {tax}"
    else:
        price_with_tax = item.price * (1 + tax)
        item_dict.update({"price_with_tax": round(price_with_tax, 2)})
        return item_dict

# Postman


