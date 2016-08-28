# import module
from CSS.completions import properties as prop
import sublime, re

# Completions Flag
flag = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

# 查找最近字符
def findLastChar(code):
    p = len(code) - 1

    while p > -1:
        ch = code[p]

        if ch == ':' or ch == '@':
            return ch;

        p -= 1
        continue

    return ''

# 【CSS】补全方法
def completions(self, view, prefix, locations):

    # 获取当前位置
    pt = locations[0] - len(prefix)

    # 获取内容
    ch = view.substr(sublime.Region(0, pt)).rstrip()
    ed = ch[-1]

    if ed == '@':
        return prop.extends_style, flag

    if ed == '{':
        return prop.names + prop.tag, flag

    if ed == ';':
        ch = findLastChar(ch)

        if ch == ':':
            return prop.names + prop.tag, flag
        else:
            return prop.tag, flag

    line = view.substr(sublime.Region(view.line(pt).begin(), pt))
    m = re.search(re.compile("([-a-zA-Z]+):[^;]*$"), line)

    if m:
        style = m.group(1)

        if style in prop.value_for_name:
            return prop.value_for_name[style] + prop.default_value, flag

        return prop.default_value, flag

    return prop.tag




