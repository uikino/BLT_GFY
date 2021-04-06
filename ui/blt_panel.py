# -*- coding: utf-8 -*-

import bpy

class PanelBLT(bpy.types.Panel):
    bl_idname = 'BLT_Panel'
    bl_label = 'BLT 工具'
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_order = 20

    @classmethod
    def poll(cls,context):
        pass