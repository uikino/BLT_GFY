# -*- coding: utf-8 -*-
"""
@author: discaz
@date: 2021-04-10 15:09:34
@description: BLT 异步任务
@email: 994679395@qq.com
"""

import asyncio
import functools
import threading


class TaskManager(object):
    def __init__(self):
        self.events_loop = asyncio.new_event_loop()
        self.events_loop_thread = threading.Thread(target=self.__internal_event_loop_run)

    def __internal_event_loop_run(self):
        self.events_loop.run_forever()

    async def __internal_task_wrapper(self, params, callback):
        future = callback['task'](**params)
        rp = await future
        callback['callback'](rp)

    def append_task(self, params_pack: dict = None, callback_pack: dict = None):
        if callback_pack is None:
            return
        else:
            asyncio.run_coroutine_threadsafe(self.__internal_task_wrapper(params_pack, callback_pack), self.events_loop)
            pass
