import http.client, urllib.parse

def get_location(adress: str): 

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': '5d628c43e45ecbb326c9274c09aff369',
        'query': adress,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    return data.decode('utf-8')


print(get_location("1600 Pennsylvania Ave NW, Washington DC"))