import http.client, urllib.parse
import haversine as hs
from haversine import Unit
import json

def get_location_info(address: str): 

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        "Content-type": "application/json",
        'access_key': '5d628c43e45ecbb326c9274c09aff369',
        'query': address,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    my_json = data.decode('utf-8')
    info = json.loads(my_json)
    # final = json.dumps(info, indent=4, sort_keys=True)
    lat = int(info["data"][0]["latitude"])
    long = int(info["data"][0]["longitude"])
    moscow_ring = (55.71, 37.612)
    location = (lat, long)
    distance = hs.haversine(location, moscow_ring, unit=Unit.KILOMETERS)

    
    return str(round(distance, 2))
