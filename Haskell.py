import sublime
import sublime_plugin
import subprocess
import os.path

class StylishHaskell(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		file = view.file_name()
		if view.is_scratch() or file[-3:] != '.hs':
			return

		subprocess.call(['stylish-haskell', '-i', file], cwd = os.path.dirname(file))
