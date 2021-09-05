# @Project  :exam
# @File     :submit_message
# @Date     :2021/8/25 6:53
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-
from configs.Url import base_url
from tools.request import Request,RequestType
import pprint,time
from api.login import Login
from tools.login_info import username,password
from tools.read_execl import ReadExecl

token=Login().login({"username":username,"password":password},True)

class Message(Request):
    headers={"Content-Type": "application/json","charset":"UTF-8",
             "X-AUTH-TOKEN":token}

    def add_message(self,params):
        url = base_url + 'api/message'
        resp=self.get_json(url,test_params=params,test_headers=self.headers)
        return resp

    def get_message(self):
        url = base_url + 'api/messages/1/4'
        resp=self.get_json(url,test_headers=self.headers,request_type=RequestType.get)
        return resp

    def replay_message(self,params):
        url=base_url+'api/replay'
        # params={"replay": "222","messageId":"3982" }
        # print(params)
        resp=self.get_json(url,params,self.headers)
        return resp


if __name__ == '__main__':
    # datas=ReadExecl('cases.xlsx','add_message').read_execl()
    # print(datas)
    # for parma in datas:
    #     print(parma[0])
    #     add_message_resp=Message().add_message(parma[0])
    #     pprint.pprint(add_message_resp)

    # get_message=Message().get_message()
    # pprint.pprint(get_message)


    datas = ReadExecl('cases.xlsx', 'replay_message').read_execl()
    # print(datas)
    for parma in datas:
        print(parma[0])
        replay_message_resp=Message().replay_message(parma[0])
        # pprint.pprint(replay_message_resp)
        time.sleep(3)
