# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-09 14:29:39
@description: BLT 登录窗口
@email: 994679395@qq.com
"""

from bpy.types import Operator


class LoginButton(Operator):
    bl_idname = 'BLT_OP.LoginButton'
    bl_label = 'BLT_OP.LoginButton'
    bl_description = 'BLT登录按钮'
