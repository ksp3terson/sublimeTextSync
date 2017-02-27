import sublime_plugin


class Folding(sublime_plugin.EventListener):

    def on_load(self, view):
        print("Size is " + str(view.size()))
        view.run_command("fold_comments")
        if view.size() > 10000:
            view.run_command("fold_by_level", {"level": 1})
