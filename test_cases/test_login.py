import pytest
from api.login import Login
from tools.read_execl import ReadExecl
import os,datetime
from tools.read_logincaseyaml import get_logincaseyaml

# #测试execl一条用例
# datas=ReadExecl('cases.xlsx','login').read_execl()
# class TestLogin:
#     @pytest.mark.parametrize('param,Result',[ReadExecl('cases.xlsx','login').read_execl()])
#     def test_001(self,param,Result):
#         resp = Login().login(param,False)
#         assert resp["message"] == Result

#测试execl多条用例
# class TestLogin:
#     @pytest.mark.parametrize('param,Result',ReadExecl('cases.xlsx','login').read_execl())
#     def test_001(self,param,Result):
#         resp = Login().login(param,False)
#         assert resp["message"] == Result


#测试yaml多条用例

class TestLogin:
    @pytest.mark.parametrize('param,Result',get_logincaseyaml('logincase.yaml'))
    def test_001(self,param,Result):
        resp = Login().login(param,False)
        assert resp["message"] == Result["message"]

ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
if __name__ == '__main__':
    # allure报告在在线生成,–alluredir=xx/xxx报告存放的地址，"--clean-alluredir"清除报告
    pytest.main(["test_login.py", "-s", "--alluredir=../report/tmp","--clean-alluredir"])
    os.system("allure serve ../report/tmp ")

    #下面是静态的html文件,生成的报告目录和服务不在一个文件
    # pytest.main(["test_login.py", "-s","--alluredir=../report/tmp","--clean-alluredir"])
    # os.system('allure generate ../report/tmp')
    # os.system('allure open ../report/tmp')

