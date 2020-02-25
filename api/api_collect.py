import requests


class ApiCollect(object):

    def get_token(self):
        data = {"user_id": 2377317731}
        res = requests.post(url='http://test-riko-xms.uu.cc/app/user/generate-token', json=data)
        return "Bearer " + res.json()['data']['token']

    def api_post_collect(self, url, data):
        headers = {
                            "Content-Type": "application/json",
                            "Authorization": self.get_token()
                        }
        return requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    res = ApiCollect().api_post_collect('http://test-riko-xms.uu.cc/app/user/generate-token',{"user_id": 2377317731})
    print(res.json())