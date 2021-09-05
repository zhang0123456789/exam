# @Project  :exam
# @File     :logging
# @Date     :2021/8/30 6:19
# @Author   :qiuhua
# @Email    :1402686685@qq.com
# @Software :PyCharm
#coding=gbk
# -*- coding:utf-8 -*-
#-*-coding:gb2312-*-

# 初级
import logging
fmt='%(filename)s[line:%(lineno)d]  ---> %(levelname)s: %(message)s --->%(asctime)s'
logging.basicConfig(level='DEBUG',datefmt='%Y-%m-%d %H%M%S',format=fmt)


logging.info('This is a log info')
logging.debug("Debugging")
logging.warning('warning exists')
logging.info('finish')

# 高级

