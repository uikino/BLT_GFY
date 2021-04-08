# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-06 13:39:18
@description: BLT 偏好配置
@email: 994679395@qq.com
"""

import bpy
from bpy.props import IntVectorProperty, StringProperty, CollectionProperty, BoolProperty, EnumProperty, FloatProperty


class BLT_GFY_preferences(bpy.types.AddonPreferences,object):
    bl_idname = 'BLT_GFY_preferences'

    