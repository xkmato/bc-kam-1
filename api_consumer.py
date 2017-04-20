import http.client
import json


def get_quote():
    """An API call to `andruxnet-random-famous-quotes.p.mashape.com` to get famous movie quotes."""

    headers = {'X-Mashape-Key': 'Z37r8KDorrmshToSBkYND18TileAp1rRYFFjsnYntDyPuYUx0u',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'}
    domain = 'andruxnet-random-famous-quotes.p.mashape.com'
    connection = http.client.HTTPSConnection(domain)
    connection.request('POST', "/?cat=movies", headers=headers)
    response = connection.getresponse()
    if 199 < response.status < 300:
        data = json.loads(response.read().decode())
        return "Quote: `{}` by {}".format(data['quote'], data['author'])
    return "Oops... Something didn't work: {}({})".format(response.status, response.reason)


if __name__ == "__main__":
    print(get_quote())