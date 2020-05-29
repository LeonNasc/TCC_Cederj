import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from . import gui_main as gui

class GUI(gui.Ui_GUI):

    def __init__(self):
        app = QApplication(sys.argv)
        self._window = QMainWindow()
        self._instance = gui.Ui_GUI()
        self._instance.setupUi(self._window)
        self._window.show()
        sys.exit(app.exec_())


    if __name__ == '__main__':
        window()
