import sublime
import sublime_plugin


class ToggleSidebarAndRevealFileCommand(sublime_plugin.WindowCommand):
	def run(self):
		window = self.window
		sidebar_visible = window.is_sidebar_visible()

		window.run_command("toggle_side_bar")

		if not sidebar_visible:
			# If sidebar was not visible, we're opening it, so reveal the file
			sublime.set_timeout(lambda: window.run_command("reveal_in_side_bar"))
