# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-09 11:09:34
@description: BLT 登录窗口
@email: 994679395@qq.com
"""

from .base_panel import BasePanel
import bpy

class LoginPanel(BasePanel,bpy.types.Panel):
    bl_idname = 'BLT_PT_LoginPanel'
    bl_label = 'BLT 登录窗口'


    def draw(self, context):
        layout = self.layout

        pass