import requests

url = "http://test-riko-xms.uu.cc"


def get_token():
    data = {"user_id": 2377317731}
    res = requests.post(url=url + '/app/user/generate-token', json=data)
    return "Bearer " + res.json()['data']['token']


def Header():
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_token()
    }
    return headers


def api_post(path, data):
    return requests.post(url=url + path, headers=Header(), json=data)


def api_get(path, data):
    return requests.get(url=url + path, headers=Header(), params=data)
