# @Project  :exam
# @File     :study_pytest
# @Date     :2021/8/22 14:57
# @Author   :秋花
# @Email    :1402686685@qq.com
# @Software :PyCharm


import pytest
#单参数单值
# @pytest.mark.parametrize("user",["18221124104"])
# def test(user):
#     print(user)
#     assert user=="18221124104"

datalist=['{username: "20200015", password: "123456"}', '登录成功']
@pytest.mark.parametrize("parmas,info",[datalist])
def test(parmas,info):
    print(parmas)
    assert info=="登录成功"

#单参数多值
# @pytest.mark.parametrize("user",["18221124104","18200000000","18200000001"])
# def test(user):
#     print(user)
#     assert user=="18221124104"

#多参数多值
# @pytest.mark.parametrize("user,pwd",[("18221124104",111111),("18200000000",111111)])
# def test(user,pwd):
#     print(user,pwd)


# 使用内置的mark.xfail标记为失败的用例就不运行了，直接跳过显示xfailed
# @pytest.mark.parametrize("user,pwd",[("18221124104",111111),pytest.param("18200000000",111111,marks=pytest.mark.xfail)])
# def test(user,pwd):
#     print(user,pwd)
#     assert user == "18221124104"
#     assert pwd== 111111

#若要获得多个参数化参数的所有组合，可以堆叠参数化装饰器
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     print("测试数据组合：x->%s, y->%s" % (x, y))


if __name__ == '__main__':
    pytest.main(["-s","study_pytest.py"])