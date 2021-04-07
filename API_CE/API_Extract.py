# -*- coding: utf-8 -*-
'''
@author: discaz
@date: 2021-04-06 16:55:18
@description: Python 包API提取工具
@email: 994679395@qq.com
'''

# 类型inspect
import inspect
# 动态导入
import importlib
# 获取模块列表
import sys

description_list = []
flags = {}

if __name__ == '__main':
    enable_generate_signatures = False
    enable_generate_signatures_with_default_value = False
    enable_generate_field_with_type = False
    enable_generate_field_with_default_value = False
    enable_recursive = False

    print('导出API的包名 : ')
    package_name = input()
    print('对于函数API 是否需要生成函数签名? Y/N')
    a = input()
    print('对于函数API 是否还需要生成带有默认值与类型的签名? Y/N')
    ab = input()
    print('对于变量API 是否生成带有类型的签名')
    b = input()
    print('对于变量API 是否生成带有类型与默认值的签名')
    ba = input()


    if a is 'Y' or a is 'y':
        enable_generate_signatures = True
    else:
        enable_generate_signatures = False

    if enable_generate_signatures and (ab is 'Y' or ab is 'y'):
        enable_generate_signatures_with_default_value = True
    else:
        enable_generate_signatures_with_default_value = False

    if b is 'Y' or b is 'y':
        enable_generate_field_with_type = True
    else:
        enable_generate_field_with_type = False

    if enable_generate_field_with_type and (ba is 'Y' or ba is 'y'):
        enable_generate_field_with_default_value = True
    else:
        enable_generate_field_with_default_value = False

    flags = {
        'fun_sig': enable_generate_signatures,
        'fun_sig_dv': enable_generate_signatures_with_default_value,
        'attr_gt': enable_generate_field_with_type,
        'attr_gt_dv': enable_generate_field_with_default_value
    }

    importlib.import_module(package_name)
    package_module_object = sys.modules[package_name]

    # 获取模块及子模块信息
    package_infos = [itr for itr in sys.modules.items() if itr[0].startswith(package_name) and '_' not in itr[0]]



    def generate_description(pk_obj):
        # 判断基础类型 tuple list dict str bool float int
        if isinstance(pk_obj,(tuple,list,dict,str,int,float)):
            pass
        elif inspect.isfunction(pk_obj):
            pass


    def __internal_object_is_class(fake_type) -> bool:
        """
        类型检查 返回 'fun'、'var'、'class'、'module'
        :param fake_class:
        :return:
        """
        # Trump say: bpy.app is fake news(class)
        return False

