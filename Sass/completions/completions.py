# import module
from Sass.completions import properties as prop
import sublime, re

# default
prop_default = prop.names + prop.tag

# Completions Flag
flag = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS


# 【CSS】补全方法
def completions(self, view, prefix, locations):

    # 获取当前位置
    pt = locations[0] - len(prefix)

    # 获取属性值
    if view.match_selector(pt, 'meta.property-value.sass'):
        line = view.substr(sublime.Region(view.line(pt).begin(), pt))
        m = re.search(re.compile('(?:-webkit-|-moz-|-ms-|-o-)?([-a-zA-Z]+):[^;]*$'), line)

        if m:
            style = m.group(1)

            if style in prop.value_for_name:
                return prop.value_for_name[style] + prop.default_value, flag

            return prop.default_value, flag

        return prop.names, flag

    if view.match_selector(pt, 'meta.parameter-value.sass'):
        return flag

    # 获取当前字符
    ch = view.substr(sublime.Region(pt - 1, pt))

    # at-rule
    if ch == '@':
        return prop.extends_style, flag

    # 伪类
    if ch == ':':
        return prop.pseude_class, flag

    # 变量
    if ch == '$':
        return flag

    line = view.substr(sublime.Region(view.line(pt).begin(), pt))

    # 属性
    if re.search(re.compile('^\s*$'), line):
        return prop_default, flag

    # 标签
    return prop.tag, flag
