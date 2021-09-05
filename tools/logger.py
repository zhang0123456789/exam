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
# fmt='%(filename)s[line:%(lineno)d]  ---> %(levelname)s: %(message)s --->%(asctime)s'
# logging.basicConfig(level='DEBUG',datefmt='%Y-%m-%d %H-%M-%S',format=fmt)
#
# logging.info('这是info信息')
# logging.debug("这是debug信息")
# logging.warning('这是warning信息')
# logging.error('这是error信息')
# logging.critical('这是critical信息')

# 输出到控制台
# 创建日志对象
# logger=logging.getLogger()
# logger.setLevel('DEBUG')
#
# # 创建控制台
# console_handler=logging.StreamHandler()
# console_handler.setLevel('ERROR')
# logger.addHandler(console_handler)
#
# logging.info('这是info信息')
# logging.debug("这是debug信息")
# logging.warning('这是warning信息')
# logging.error('这是error信息')
# logging.critical('这是critical信息')

# 输出到文件

# 创建日志收集器
# logger=logging.getLogger()
# logger.setLevel('INFO')
# #
# file_handler=logging.FileHandler('../logs/log.txt',mode='a',encoding='utf-8')
# file_handler.setLevel('ERROR')
# logger.addHandler(file_handler)
#
# logging.info('这是info信息')
# logging.debug("这是debug信息")
# logging.warning('这是warning信息')
# logging.error('这是error信息')
# logging.critical('这是critical信息')
import logging,time

class Log:

    def __init__(self,level="DEBUG"):
        self.logger=logging.getLogger('huahua')
        self.logger.setLevel(level)

    def console_handler(self,level="DEBUG"):
        console_handler=logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(self.set_formatter()[0])
        return console_handler

    def file_handler(self,level="DEBUG"):
        t=time.strftime('%Y-m-%d %H-%M-%S')
        file_handler = logging.FileHandler(f'../logs/{t}_log.text',mode='a',encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(self.set_formatter()[1])
        return file_handler

    def set_formatter(self):
        console_fmt=logging.Formatter(fmt='%(filename)s[line:%(lineno)d]  ---> %(levelname)s: %(message)s --->%(asctime)s')
        file_fmt = logging.Formatter(
            fmt='%(filename)s ---> %(levelname)s --->%(asctime)s')
        return console_fmt,file_fmt

    def get_log(self):
        self.logger.addHandler(self.console_handler())
        self.logger.addFilter(self.file_handler)
        return self.logger