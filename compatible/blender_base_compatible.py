# -*- coding: utf-8 -*-
'''
@author: discaz
@date: 2021-04-06 15:07:36
@description: BLT 完全版插件
@email: 994679395@qq.com
'''

import bpy

class Blender_Base_Compatible(object):
    """
    Blender 基础兼容处理
    """
    def __init__(self):
        self.blender_version = '{}.{}'.format(bpy.app.version[0],bpy.app.version[1])

    def __compatible_verification(self):
        print(20*'=' + ' 执行 Blender Base 兼容性检查 ' + 20*'=')
        
