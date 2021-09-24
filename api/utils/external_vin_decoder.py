import os

from requests import get


def decode(vin_code: str) -> dict:
    """
    Decoding the VIN via external services

    Parameters
    ----------
    vin_code : str
        VIN number


    Returns
    -------
    dict
        contains make, model, year, manufacturer, engine, trim, transmission values of inputted vin_code
    """
    headers = {
        'authorization': os.environ.get('AUTHORIZATION'),
        'partner-token': os.environ.get('PARTNER-TOKEN')
    }
    endpoint = "http://api.carmd.com/v3.0/decode"

    try:
        response = get(
            endpoint,
            headers=headers,
            params={"vin": vin_code}
        ).json()
        if type(response['data']) is dict:
            return response['data']
    except Exception:
        pass
    return {}
