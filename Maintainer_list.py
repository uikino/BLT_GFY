# -*- coding: utf-8 -*-


class AuthorInfo(object):
    def __init__(self):
        # 作者者名称
        self.name = ''
        # 负责的模块
        self.modules = []
        # 作者邮箱
        self.email = ''
        # 作者qq
        self.qq = ''

    def set_name(self,name:str):
        self.name = name

    def append_module(self,module_name:str):
        self.modules.append(module_name)

    def set_email(self,email:str):
        self.email = email

    def set_qq(self,qq:str):
        self.qq = qq
