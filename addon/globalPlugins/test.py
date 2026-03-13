import globalPluginHandler
import ui
from scriptHandler import script
import inputCore


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(
		description=_("A test script"),
		gesture="kb:nvda+<",
	)
	def script_test(self, gesture: inputCore.InputGesture):
		ui.message("Hello world!")
