# @Project  :exam
# @File     :test_message
# @Date     :2021/8/28 16:17
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-
import pytest,datetime,os
from api.message import Message
from tools.read_execl import ReadExecl

datas=ReadExecl('cases.xlsx','add_message').read_execl()

class TestMessage:
    @pytest.mark.parametrize('message,Result',ReadExecl('cases.xlsx','add_message').read_execl())
    def test(self,message,Result):
        resp = Message().add_message(params=datas[0][0])
        assert resp["message"] == Result


ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
if __name__ == '__main__':
    pytest.main(["test_add_message.py", "-s", "--alluredir=../report/tmp","--clean-alluredir"])
    # pytest.main(['-s', '-v', f'--html=../report/{ts}.html'])
    os.system("allure serve ../report/tmp ")