import sublime
import sublime_plugin
import os
import codecs
import re


# 加载【Json】文件数据
def load_json_data(fpath, encoding = 'utf-8'):

    if os.path.exists(fpath):

        # 读取文件内容
        f = codecs.open(fpath, 'r', encoding)
        content = f.read()

        # 获取内容数据
        try:
            data = sublime.decode_value(content)
        except:
            raise

        # 关闭文件
        f.close()

    return data or {}


# 加载项目数据
def load_project():

    # 获取【Session】文件路径
    fdir = sublime.packages_path()
    fpath = os.path.join(os.path.dirname(fdir), 'Local', 'Session.sublime_session')

    # 获取【Session】数据
    if os.path.exists(fpath):
        data = load_json_data(fpath)
    else:
        return []

    # 获取项目数据
    if 'workspaces' in data:
        data = data['workspaces']
    else:
        return []

    # 获取最近项目数据
    if 'recent_workspaces' in data:
        data = data['recent_workspaces']

        # 格式化数据
        if data and len(data):
            return [format_project(x) for x in data]
        else:
            return []

    # 返回空列表
    return []


# 格式化项目数据
def format_project(data):

    # 获取项目文件名
    name = re.sub('\.[\w\-]+?$', '', os.path.basename(data))

    # 替换项目文件路径
    path = re.sub('\.sublime-workspace$', '.sublime-project', data)

    # 获取用户文件夹目录
    upath = os.path.expanduser('~')

    # 返回项目信息
    return { 'desc': [name, path.replace(upath, '~')], 'path': path }


# 定义切换项目命令
class SwitchProjectCommand(sublime_plugin.WindowCommand):

    projects = None
    current_project = None

    # 选择项目回调函数
    def on_select_project(self, index, project):

        # 未选择项目时直接退出
        if index == -1:
            return None

        # 获取项目文件路径
        fpath = project['path']

        # 选择的不是当前项目时执行
        if fpath != self.current_project:
            self.window.run_command('close_workspace')
            self.window.run_command('open_recent_project_or_workspace', { 'index': index })
            self.projects.insert(0, self.projects.pop(index))


    # 执行切换项目命令
    def run(self):

        # 此脚本只对【OSX】有效
        if sublime.platform() != 'osx':
            return None

        # 获取项目数据
        if self.projects == None:
            self.projects = load_project()

        # 当存在项目时执行
        if len(self.projects):

            # 保存当前项目
            self.current_project = self.window.project_file_name()

            # 显示项目选择列表
            self.window.show_quick_panel(
                items = [ x['desc'] for x in self.projects ],
                on_select = lambda idx: self.on_select_project(idx, self.projects[idx])
            )




