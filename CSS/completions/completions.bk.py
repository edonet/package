# import module
from CSS.completions import properties as prop
import sublime, re

# Completions Flag
flag = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

# 提取代码片段
def filterCode(code):
    s = ""
    st = len(code) - 1

    while st > -1:
        ch = code[st]

        if ch == '}' or ch == '@':
            s += ch
            return s, code[st:]

        if ch == '{':
            s += ch

        st -= 1
        continue

    return s, code


# 【CSS】补全方法
def completions(self, view, prefix, locations):

    pt = locations[0] - len(prefix)
    text = view.substr(sublime.Region(0, pt)).rstrip()
    text = re.compile("\s*\/\*.*\*\/\s*").sub('', text)

    m = filterCode(text)
    ch = m[0]
    text = m[1]

    if not text:
        return prop.tag

    ed = text[-1]
    print(ch, ed)

    if ch == '@' and ed == ';':
        return prop.tag, flag;

    if ch == '{' or ch == '{}' or ch == '{{@':
        if ed == '{' or ed == ';':
            return prop.names, flag

        m = re.search(re.compile("([-a-zA-Z]+):[-a-zA-Z0-9_.,()/!%$\s]*$"), text)
        if m:
            style = m.group(1)

            if style in prop.value_for_name:
                return prop.value_for_name[style] + prop.default_value, flag

            return prop.default_value, flag
        else:
            return prop.names, flag

    if ed == '@':
        return prop.extends_style, flag

    if ed == ':':
        return prop.pseude_class, flag

    if ch == '{@':
        if re.match(re.compile("@keyframes\s"), text):
            return prop.keyframes_style, flag

    return prop.tag
