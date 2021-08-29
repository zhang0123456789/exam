from configs.Url import base_url
from tools.request import Request
import requests
# md5进行数据的加密
import hashlib
from tools.read_execl import ReadExecl


# md5加密
def get_md5(pwd):
    m = hashlib.md5()  # 创建一个hashlib.md5()对象
    m.update(pwd.encode("utf8"))  # 将参数转换为UTF8编码
    return m.hexdigest()  # 用十六进制输出加密后的数据


class Login:
    url = base_url + 'api/loginS'

    def login(self, data: object, mode: object) -> object:
        # 字典名[键名]=新的值   字典修改值操作
        # data["password"] = get_md5(data["password"])
        # payload=data  # data里面包含有用户名里面
        # resp=requests.post(self.url,json=payload)
        # if mode:#获取token
        #     return resp.json()["token"]
        # else: #获取响应数据
        #     return resp.json()


        #参数
        data["password"]=get_md5(data["password"])
        payload = data
        """
        data---一般时表单格式
        json---json
        files--文件上传接口
        params--参数会放到url路径里？ a=1&b=2
        """
        resp_1=Request().get_response(self.url,payload,test_headers=None,request_type='post',expect_return_code=200)
        resp=Request().get_json(self.url,payload)
        if mode:#获取token
            return resp["token"]
        else: #获取响应数据
            return resp_1.json()


import pprint
if __name__ == '__main__':
    resp=Login().login({"username": "20200015", "password": "123456"},False)
    pprint.pprint(resp)

