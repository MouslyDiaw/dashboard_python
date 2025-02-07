"""API module."""

from fastapi import FastAPI

from make_dataset import get_data

app = FastAPI()


@app.get("/")
def root():
    """ Display the home page.

    Returns:
        dict: {"message": .....}

    """
    return {"message": "API for data marketing campaign"}


@app.get("/get_data")
async def load_data():
    """Load all data

    Returns:
        json with orient "records" like [{{column -> value}}, ... , {{column -> value}}]

    """
    data = get_data()
    return data.to_json(orient="records")


@app.get("/get_data_campaign/{campaign_id}")
async def get_data_campaign(campaign_id: str):
    """Get a specific campaign data

    Args:
        campaign_id: campaign id

    Returns:
        json with orient "records" like [{{column -> value}}, ... , {{column -> value}}]

    """
    data = get_data()
    return data.loc[data.campaign_id == campaign_id].to_json(orient="records")
