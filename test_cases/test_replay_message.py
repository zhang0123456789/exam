# @Project  :exam
# @File     :test_replay_message
# @Date     :2021/8/29 8:42
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-

import pytest,datetime,os,time
from api.message import Message
from tools.read_execl import ReadExecl

datas = ReadExecl('cases.xlsx', 'replay_message').read_execl()
print(datas)


class TestMessage:
    @pytest.mark.parametrize('parma,Result',datas)
    def test(self,parma,Result):
        resp = Message().replay_message(parma)
        print(resp)
        assert resp["message"] == Result


ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
if __name__ == '__main__':
    pytest.main(["test_replay_message.py", "-s", "--alluredir=../report/tmp","--clean-alluredir"])
    # pytest.main(['-s', '-v', f'--html=../report/{ts}.html'])
    os.system("allure serve ../report/tmp ")