from PySide2 import QtWidgets
from PySide2.QtGui import QIcon

from GUI.dialogs.plugins_dialog import PluginsDialog
from Plugins.widgets.main_screen import MainScreen


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, pm=None):
        super().__init__(parent)
        self.setWindowTitle("Festivity")
        self.setWindowIcon(QIcon("resources/icons/anchor.png"))
        self.resize(500, 200)

        # initialize the login widget
        self.mainScreen = MainScreen()

        self.plugin_manager = pm
        self.action_dict = {
            "users": QtWidgets.QAction(QIcon("resources/icons/users.png"), "&Show users"),
            "plugin_settings":  QtWidgets.QAction(QIcon("resources/icons/puzzle.png"), "&Plugin settings")
        }
        # set the mainScreen as central Widget
        self.setCentralWidget(self.mainScreen)
        self.show()

    def set_central_widget(self, symbolic_name: str):
        """
        Podesava centralni widget glavnog prozora, na osnovu simboličkog imena se dobija plugin
        koji će se smestiti u centralni deo glavnog prozora.

        :param symbolic_name: Simbolicko ime plugina koji želimo da instanciramo.
        """
        try:

            plugin = self.plugin_manager.get_by_symbolic_name(symbolic_name)
            widgets = plugin.get_widget()
            self.setCentralWidget(widgets[0])
            if widgets[1] is not None:
                self.tool_bar.addSeparator()
                self.tool_bar.addActions(widgets[1].actions())
            self.menu_bar.addMenu(
                widgets[2]) if widgets[2] is not None else None
        except IndexError:
            print("Ne postoji ni jedan plugin sa zadatim simboličkim imenom!")
