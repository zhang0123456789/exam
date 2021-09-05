# @Project  :exam
# @File     :exam
# @Date     :2021/9/5 16:58
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-
# -*- coding: gbk -*-
from tools.request import Request,RequestType
from api.login import Login
from tools.login_info import username,password
import pprint

token=Login().login({"username":username,"password":password},True)
class Exam(Request):
    headers = {"Content-Type": "application/json", "charset": "UTF-8",
               "X-AUTH-TOKEN": token}


    #  获取所有试卷列表
    def get_exam(self):
        url='http://121.41.14.39:9097/api/exams/1/6'
        resp=self.get_json(url,request_type=RequestType.get)
        return resp


if __name__ == '__main__':
    pprint.pprint(Exam().get_exam())