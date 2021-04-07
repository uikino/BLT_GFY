# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-06 10:10:18
@description: BLT 完全版插件
@email: 994679395@qq.com
"""

import os

import bpy
import prettytable


class CompatibleUtils(object):
    def __init__(self):
        self.name = 'BLT 兼容性检查工具'
        self.addon_name = __package__
        this_file = os.path.abspath(__file__)
        self.current_addon_compatibility_CE_dir = this_file[0:this_file.rfind('/')] + '../API_CE'
        print('')



    def set_API_CE_dir(self, path):
        """
        重设API描述文件目录位置 默认为BLT/API_CE/
        :param path:
        :return:
        """
        self.current_addon_compatibility_CE_dir = path

    def compatible_verification_from_API_description_file(self, API_description_file):
        """
        根据API描述文件对API进行检查
        API_description_file 为API描述文件名称
        :param API_description_file:
        :return:
        """
        # 读取整个文件列表
        if self.current_addon_compatibility_CE_dir[-1] != '/':
            self.current_addon_compatibility_CE_dir + '/'
        line = ''
        with open(self.current_addon_compatibility_CE_dir + API_description_file, 'r') as f:
            while line in f:
                if line[0] == '#':
                    continue
                else:
                    field_list = line.split('-')

        pass
