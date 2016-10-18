import sublime, sublime_plugin, re

r_args = re.compile(r',\s*')
r_inject = re.compile(r'([\$\w]+)(,\s*|$)')
r_func = re.compile('^\s*function\s*\((.*?)\)', re.S)

class AngularInjectCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        for region in view.sel():

            if not region.empty():
                inject = self.injectArguments(view.substr(region))

                if inject:
                    view.replace(edit, region, inject)


    def injectArguments(self, text):
        m = re.search(r_func, text)

        if m:
            args = m.group(1)

            if args:
                args = re.sub(r_args, ', ', args)
                inject = re.sub(r_inject, "'\\1', ", args)

                return text.replace(m.group(0), '[\n\t' + inject + '\n\tfunction (' + args + ')')
