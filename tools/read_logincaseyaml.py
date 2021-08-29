# @Project  :exam
# @File     :read_logincaseyaml
# @Date     :2021/8/23 6:31
# @Author   :
# @Email    :1402686685@qq.com
# @Software :PyCharm
# -*- coding: UTF-8 -*-

import  yaml,time

def get_logincaseyaml(filename):
    res_list=[]
    with open(f'../data/{filename}', 'r',encoding='gbk') as f:
        res=yaml.load(f, Loader=yaml.FullLoader)
    del res[0]
    for one in res:
        res_list.append([one['data'], one['resp']])
    return res_list

if __name__ == '__main__':
    res=get_logincaseyaml('logincase.yaml')
    for one in res:
        print(one)
    # print(res)