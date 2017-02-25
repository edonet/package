import sublime
import sublime_plugin
import subprocess


# 定义【Subl】命令
class SublCommand(sublime_plugin.WindowCommand):

    # 执行【Subl】命令
    def run(self, args = []):

        # 获取【sublime】执行路径
        executable_path = sublime.executable_path()

        # 获取【OSX】下的【subl】目录
        if sublime.platform() == 'osx':
            app_path = executable_path[:executable_path.rfind(".app/") + 5]
            executable_path = app_path + "Contents/SharedSupport/bin/subl"

        # 运行【subl】命令
        subprocess.Popen([executable_path] + args)

        # 修复在【Windows】下窗口推动焦点
        if sublime.platform() == "windows":
            def fix_focus():
                window = sublime.active_window()
                view = window.active_view()
                window.run_command('focus_neighboring_group')
                window.focus_view(view)

            sublime.set_timeout(fix_focus, 300)
