import requests


class ApiCollect(object):
    def api_post_collect(self, url, book_id, type):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImtpZC1oZWFkZXIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE1ODQ3MTUyNDMsInVpZCI6OTk5OTk5OTk5OTl9.pHBrYYG01_3Zfz3122WoXZSscbvPX-oG_1JzNkgXNzQ"}
        # data 定义
        data = {"book_id": book_id, "type": type}

        return requests.post(url, headers=headers, json=data)
