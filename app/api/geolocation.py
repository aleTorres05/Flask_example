import http.client
import json
import urllib.parse

import haversine as hs
from haversine import Unit
from loguru import logger


def get_location_info(address: str):
    
    logger.add("logs/distance_response.log")

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        "Content-type": "application/json",
        'access_key': '5d628c43e45ecbb326c9274c09aff369',
        'query': address,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))
    try:
        res = conn.getresponse().read().decode('utf-8')
        info = json.loads(res)
        lat = int(info["data"][0]["latitude"])
        long = int(info["data"][0]["longitude"])
        moscow_ring = (55.71, 37.612)
        location = (lat, long)
        distance = hs.haversine(location, moscow_ring, unit=Unit.KILOMETERS)
        logger.info(f"{info['data'][0]['label']} is {str('{:,.2f}'.format(distance))} KM away from Moscow Ring Road")
    except Exception:
        logger.exception(f"ERROR: PLEASE INSERT A VALID ADDRESS WITH EXCEPTION {Exception}")
        return f"ERROR: PLEASE INSERT A VALID ADDRESS WITH EXCEPTION {Exception}"
    
    return f"{info['data'][0]['label']} is {str('{:,.2f}'.format(distance))} KM away from Moscow Ring Road"
