# @Project  :exam
# @File     :conftest
# @Date     :2021/8/22 19:44
# @Author   :秋花
# @Email    :1402686685@qq.com
# @Software :PyCharm
# import pytest
# #自动化测试执行前--环境初始化操作
# @pytest.fixture(scope="session",autouse=True)
# def start_running():
#     print("----马上开始执行自动化测试-----")
#     yield
#     print("----自动化测试完成，开始处理垃圾数据-----")
#
# #自动化测试执行后--做数据清除操作