import requests
url = "http://test-riko-xms.uu.cc"


def get_token():
    data = {"user_id": 2377317731}
    res = requests.post(url=url + '/app/user/generate-token', json=data)
    return "Bearer " + res.json()['data']['token']


class ApiRes(object):

    def api_post(self, path, data):
        headers = {
                            "Content-Type": "application/json",
                            "Authorization": get_token()
                        }
        return requests.post(url=url+path, headers=headers, json=data)

    def api_get(self, path, data):
        headers = {
                            "Content-Type": "application/json",
                            "Authorization": get_token()
                        }
        return requests.get(url=url+path, headers=headers, params=data)


if __name__ == '__main__':
    res =ApiRes().api_post('/app/user/generate-token', {"user_id": 2377317731})
    print(res.json())