import globalPluginHandler
import ui
from scriptHandler import script


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	@script(
		description=_("A test script"),
		gesture = "kb:nvda+<",
	)
	def script_test(self, gesture):	
		ui.message("Hello world!")
