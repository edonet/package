import sublime, sublime_plugin

from Sass.completions import completions as Sass

class Completions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "source.css"):
            return Sass.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.scss"):
            return Sass.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.sass"):
            return Sass.completions(self, view, prefix, locations);

        if view.match_selector(locations[0], "source.less"):
            return Sass.completions(self, view, prefix, locations);

        return None;
