# 导包 json
import json


# with open("../data/login.json", encoding="utf-8") as f:
# 调用load方法加载文件流
# data = json.load(f)
# print(data)

# 打开json文件并获取文件流
# def read_json():
#     with open("../data/login.json", encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         return json.load(f)


class ReadJson(object):

    def __init__(self, filename):
        self.filePath = "/api_hm_dome/data/" + filename

    def read_json(self):
        with open(self.filePath, encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)


"""
    问题：
        1.未经过封装无法在别的模块内使用。
        2.数据存储文件有好几个，如果写次，在读取别的文件时无法使用
        3.预期格式为列表嵌套元祖
        
    解决：
        1.进行封装
        2.使用参数替换静态写死的文件名
        3.读取字典内容，并添加到新的列表中
"""
if __name__ == '__main__':
    ReadJson("login.json").read_json()
    # data = ReadJson("login.json").read_json()
    # ars = []
    # ars.append((data.get("url"),
    #              data.get("openid"),
    #              data.get("uid"),
    #              data.get("sessionid"),
    #              data.get("msg"),
    #              data.get("status_code")
    #              ))
    # print(arrs)