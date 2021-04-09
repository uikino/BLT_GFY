# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-09 11:09:34
@description: BLT 登录窗口
@email: 994679395@qq.com
"""

import bpy

class BasePanel(object):
    bl_idname = 'BLT_PT_BasePanel'
    bl_label = 'BLT 工具'
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Tools'
    bl_order = 20

