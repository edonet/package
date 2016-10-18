import os
import subprocess

import sublime
import sublime_plugin


class SublimeListenerServer(sublime_plugin.EventListener):

    # 是否已经退出
    is_exit = False

    # 工作路径
    working_dir = os.path.dirname(__file__)

    # 初始化服务
    def __init__(self):
        sublime.set_timeout_async(lambda : self.node_command('start'))


    # 退出服务
    def on_pre_close(self, view):
        if not self.is_exit and len(sublime.windows()) == 0 :
            self.is_exit = True
            self.node_command('exit')

    # 执行命令
    def exec_command(self, cmd):
        subprocess.call(cmd, shell = True)

    # 执行【node】命令
    def node_command(self, cmd):
        cmd = os.path.join(self.working_dir, 'bin', cmd)
        self.exec_command(['node', cmd])
