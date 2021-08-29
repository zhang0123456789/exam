# @Project  :exam
# @File     :test_get_message
# @Date     :2021/8/29 8:41
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-

import pytest,datetime,os
from api.message import Message
from tools.read_execl import ReadExecl


class TestMessage:
    @pytest.mark.parametrize('message,Result',ReadExecl('cases.xlsx','get_message').read_execl())
    def test(self,message,Result):
        resp = Message().get_message()
        assert resp["message"] == Result


ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
if __name__ == '__main__':
    pytest.main(["test_get_message.py", "-s", "--alluredir=../report/tmp","--clean-alluredir"])
    # pytest.main(['-s', '-v', f'--html=../report/{ts}.html'])
    os.system("allure serve ../report/tmp ")