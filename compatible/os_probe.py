# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-06 13:39:18
@description: BLT 完全版插件
@email: 994679395@qq.com
"""

# 独立于 blender 而调用 python 标准库，避免 blender 版本更新导致API修改而致使失败
import os
import sys


class os_probe(object):
    """
    os_probe 负责负责系统探测
    get_platform 返回OS类型
    get_current_os_user 返回当前OS运行blender的用户
    get_platform_tmp_dir 返回OS推荐tmp目录
    """
    def __init__(self):
        # 获取运行平台 'win32' 'darwin' 'linux'
        self.platform = sys.platform
        # 获取系统当前用户
        self.current_os_user = self.get_current_os_user()
        # 获取当前OS推荐的tmp文件目录
        self.platform_tmp_dir = ''

    def get_platform(self):
        """
        返回OS类型 'linux' 'darwin' 'win32'
        """
        # 加快运行
        if self.platform is not None and len(self.platform):
            return self.platform
        self.platform = sys.platform
        return self.platform

    def get_current_os_user(self):
        """
        返回当前登录系统的用户
        Returns:
        """
        # 加快运行
        if self.current_os_user is not None and len(self.current_os_user):
            return self.current_os_user

        if 'linux' in self.platform:
            self.current_os_user = os.getenv('USER')
        elif 'darwin' in self.platform:
            self.current_os_user = os.getenv('USER')
        elif 'win32' in self.platform:
            self.current_os_user = os.getenv('UserName')
        else:
            self.__internal_warning()
        return self.current_os_user

    def get_platform_tmp_dir(self):
        """
        返回平台推荐的临时目录
        如:
            linux(posix)    => /tmp
                            (这是由linux文件系统层次结构标准FHS所规定)
            win32(windows)  => C:\Users\${UserName}\AppData\Local\Temp
                            (由于windows的问题会存在路径改变，这是fallback机制造成的)
            darwin(MACOSX)  => 由环境变量提供$TMPDIR
                            (虽然提供了支持，但不推荐MACOSX平台,原因是Apple对于文件系统结构设计不合理)
        Returns:
        """
        if self.platform_tmp_dir is not None and len(self.platform_tmp_dir):
            return self.platform_tmp_dir

        if 'linux' in self.platform:
            self.platform_tmp_dir = '/tmp'
            return '/tmp'
        elif 'darwin' in self.platform:
            self.platform_tmp_dir = os.getenv('TMPDIR')
            return self.platform_tmp_dir
        elif 'win32' in self.platform:
            self.platform_tmp_dir = os.getenv('TEMP')
            return self.platform_tmp_dir
        else:
            self.__internal_warning()

    def __internal_warning(self):
        print('ERROR => 该系统' + self.platform + '不在支持范围内')
        raise Exception('ERROR => 该系统' + self.platform + '不在支持范围内')
