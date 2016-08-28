import sublime, sublime_plugin

from CSS.completions import completions as CSS

class Completions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "source.css"):
            return CSS.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.scss"):
            return CSS.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.sass"):
            return CSS.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.less"):
            return CSS.completions(self, view, prefix, locations);

        return None;
