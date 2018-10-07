import sublime
import sublime_plugin
import re


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for region in view.sel():
			s = view.substr(region)
			text = s.replace("&", "&#00038;").replace("-", "&#00045;").replace("®","&#00174;").replace("©","&#00169;").replace('"',"&#00034;").replace("™","&#08482;").replace("≤","&#08804;").replace("≥","&#08805;").replace("<","&#00060;").replace(">","&#00062;").replace("*","&#00042;").replace("•","&#08226;").replace("ï","&#00239;").replace("–","&#08211;").replace("’","&#08217;").replace("±","&#00177;").replace("—","&#08212;").replace("~","&#00126;").replace("―","&#08213;").replace("†","&#08224;").replace("‡","&#08225;").replace("§","&#00167;").replace("'", "&#00039;")
			self.view.replace(edit, region, text)