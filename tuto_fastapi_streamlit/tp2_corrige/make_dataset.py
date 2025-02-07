"""Data module."""

from os import path

import pandas as pd

# data from github
INPUT_DATA_URI = "https://github.com/MouslyDiaw/creez-dashboard/blob/main/data"


def get_data():
    """

    Returns:

    """
    # Impressions --------------------------
    df_impressions = pd.read_csv(path.join(INPUT_DATA_URI, "impressions.csv?raw=true"),
                                 sep=",", on_bad_lines='skip',
                                 dtype={"cookie_id": str,
                                        "campaign_id": str,
                                        "external_site_id": str,
                                        }
                                 )
    # convert timestamp to date and create new column named 'date'
    df_impressions['date_impression'] = pd.to_datetime(df_impressions['timestamp'], unit='s')
    # Clics --------------------------
    df_clics = pd.read_csv(path.join(INPUT_DATA_URI, "clics.csv?raw=true"),
                           sep=",", on_bad_lines='skip',
                           dtype={"cookie_id": str}
                           )
    # convert timestamp to date and create new column named 'date'
    df_clics['date_clic'] = pd.to_datetime(df_clics['timestamp'], unit='s')

    # Achats --------------------------
    df_achats = pd.read_csv(path.join(INPUT_DATA_URI, "achats.csv?raw=true"),
                            sep=",", on_bad_lines='skip',
                            dtype={"cookie_id": str,
                                   "product_id": str,
                                   }
                            )
    # convert timestamp to date and create new column named 'date'
    df_achats['date_achat'] = pd.to_datetime(df_achats['timestamp'], unit='s')

    # Merge data
    data = (df_impressions.drop("timestamp", axis=1)
            # add clic on impressions that have this action
            .merge(df_clics.drop("timestamp", axis=1), how="left", on="cookie_id")
            # add clic on impressions that have this action
            .merge(df_achats.drop("timestamp", axis=1), how="left", on="cookie_id")
            .assign(is_clic=lambda dfr: dfr.date_clic.notnull(),
                    is_achat=lambda dfr: dfr.date_achat.notnull(),
                    )
            )
    return data
