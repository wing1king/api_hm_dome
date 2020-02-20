import requests


class ApiCollect(object):
    def api_post_collect(self, url, headers, data):

        return requests.post(url, headers=headers, json=data)
