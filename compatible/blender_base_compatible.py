# -*- coding: utf-8 -*-
'''
@author: discaz
@date: 2021-04-06 15:07:36
@description: BLT 完全版插件
@email: 994679395@qq.com
'''

import bpy
import prettytable

class Blender_Base_Compatible(object):
    """
    Blender 基础兼容处理
    """
    def __init__(self):
        print(20*'=' + ' 执行 Blender Base 兼容性检查 ' + 20*'=')
        self.__internal_basic_API_CE()
        # 变量获取


    def __internal_basic_API_CE(self):
        compatibility_table = prettytable.PrettyTable()
        compatibility_table.field_names = ["模块位置", "API名称", "状态"]
        compatibility_table.align["模块位置"] = "l"
        compatibility_table.align["API名称"] = "l"

        compatibility_table.add_row(["bpy", "app", hasattr(bpy, "app")])
        compatibility_table.add_row(['bpy', 'context', hasattr(bpy, 'context')])
        compatibility_table.add_row(['bpy', 'props', hasattr(bpy, 'props')])
        compatibility_table.add_row(['bpy', 'types', hasattr(bpy, 'types')])
        compatibility_table.add_row(['bpy', 'utils', hasattr(bpy, 'utils')])
        api_pass = hasattr(bpy, "app") and hasattr(bpy, 'context') and hasattr(bpy, 'props') and hasattr(bpy, 'types') and hasattr(bpy, 'utils')
        if not api_pass:
            print(compatibility_table.get_string(title="Blender 基础API状态"))
            raise Exception('无法满足API要求')
        compatibility_table.add_row(["bpy.app", "version", hasattr(bpy.app, 'version')])
        compatibility_table.add_row(['bpy.app', 'build_platform', hasattr(bpy.app, 'build_platform')])
        compatibility_table.add_row(['bpy.app', 'tempdir', hasattr(bpy.app, 'tempdir')])
        compatibility_table.add_row(['bpy.utils', 'resource_path', hasattr(bpy.utils, 'resource_path')])
        compatibility_table.add_row(['bpy.utils', 'script_path_user', hasattr(bpy.utils, 'script_path_user')])
        compatibility_table.add_row(['bpy.types', 'AddonPreferences', hasattr(bpy.types, 'AddonPreferences')])
        compatibility_table.add_row(['bpy.types', 'Operator', hasattr(bpy.types, 'Operator')])
        compatibility_table.add_row(['bpy.context', 'preferences', hasattr(bpy.context, 'preferences')])
        compatibility_table.add_row(['bpy.props', 'IntProperty', hasattr(bpy.props, 'IntProperty')])
        compatibility_table.add_row(['bpy.props', 'FloatProperty', hasattr(bpy.props, 'FloatProperty')])
        compatibility_table.add_row(['bpy.props', 'FloatVectorProperty', hasattr(bpy.props, 'FloatVectorProperty')])
        compatibility_table.add_row(['bpy.props', 'BoolProperty', hasattr(bpy.props, 'BoolProperty')])
        compatibility_table.add_row(['bpy.props', 'EnumProperty', hasattr(bpy.props, 'EnumProperty')])
        compatibility_table.add_row(['bpy.props', 'StringProperty', hasattr(bpy.props, 'StringProperty')])
        compatibility_table.add_row(['bpy.props', 'CollectionProperty', hasattr(bpy.props, 'CollectionProperty')])
        compatibility_table.add_row(['bpy.types', 'Menu', hasattr(bpy.types, 'Menu')])
        compatibility_table.add_row(['bpy.types', 'Panel', hasattr(bpy.types, 'Panel')])
        compatibility_table.sortby = '模块位置'
        print(compatibility_table.get_string(title="Blender API 检查"))
        print('')
