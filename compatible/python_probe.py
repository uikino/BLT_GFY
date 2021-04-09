# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-06 10:10:18
@description: BLT 完全版插件
@email: 994679395@qq.com
"""
import inspect

try:
    import importlib
except RuntimeError as e:
    print('Python 标准库: importlib 不存在，请检查Python是否损坏\n')
    raise RuntimeError('importlib包 不存在')

try:
    import pkg_resources
except RuntimeError as e:
    print('Python 包: pkg_resources 不存在，请检查是否已经安装setuptools')
    raise RuntimeError('Python 包: pkg_resources 不存在，请检查是否已经安装setuptools')

import sys


class python_probe(object):
    def __init__(self):
        self.python_installed_packages = [(pkg.project_name, pkg.version) for pkg in pkg_resources.working_set]

    def get_package_installed_list(self):
        return self.python_installed_packages

    def is_installed(self, pkg_name: str, version=None):
        if version:
            return (pkg_name, version) in self.python_installed_packages
        else:
            return pkg_name in [itr for itr in self.python_installed_packages]

    @staticmethod
    def is_loaded(pkg_name: str):
        return pkg_name in sys.modules.keys()

    @staticmethod
    def import_module(pkg_name: str):
        importlib.import_module(pkg_name)

    @staticmethod
    def reload_module(pkg_name: str):
        if python_probe.is_loaded(pkg_name):
            importlib.reload(importlib.util.find_spec(pkg_name))
        else:
            importlib.import_module(pkg_name)

    def exist_object(self, pkg_name, obj_name) -> dict:
        if not self.is_loaded(pkg_name):
            return {'status': False, 'message': 'module not loaded'}
        if hasattr(sys.modules[pkg_name], obj_name):
            return {'status': True}
        else:
            return {'status': False, 'message': '{}.{} not found'.format(pkg_name, obj_name)}

    def exist_var(self, obj_name, attr_name) -> dict:
        rs = self.exist_object(obj_name, attr_name)
        if rs['status']:
            is_f = inspect.isfunction(getattr(sys.modules[obj_name], attr_name))
            return {'status': not is_f}
        else:
            return rs

    def exist_method(self, obj_name, method_name) -> dict:
        rs = self.exist_object(obj_name, method_name)
        if rs['status']:
            is_f = inspect.isfunction(getattr(sys.modules[obj_name], method_name))
            return {'status': is_f}
        else:
            return rs
