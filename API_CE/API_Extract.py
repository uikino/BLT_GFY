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

if __name__ == '__main':
    enable_generate_signatures = False
    enable_generate_signatures_with_default_value = False
    enable_generate_field_with_type = False
    enable_generate_field_with_default_value = False
    enable_recursive = False

    print('导出API的包名 : ')
    package_name = input()
    print('是否允许递归导出? Y/N')
    package_recursive = input()
    print('对于函数API 是否需要生成函数签名? Y/N')
    a = input()
    print('对于函数API 是否还需要生成带有默认值与类型的签名? Y/N')
    ab = input()
    print('对于变量API 是否生成带有类型的签名')
    b = input()
    print('对于变量API 是否生成带有类型与默认值的签名')
    ba = input()

    if package_recursive is 'Y' or package_recursive is 'y':
        enable_recursive = True
    else:
        enable_recursive = False

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

    importlib.import_module(package_name)
    package_module_object = sys.modules[package_name]
    for itr in dir(package_module_object):
        # 跳过魔法函数，魔法变量
        if '__' in itr[0:2]:
            continue
        if inspect.ismodule(getattr(package_module_object,itr)):
            pass
        elif inspect.isfunction(getattr(package_module_object,itr)):
            pass
        else:
            pass

    pass
