
from PyQt6 import   QtWidgets
from MainWindowEx import MainWindowEx

import sys

app = QtWidgets.QApplication(sys.argv)
window = MainWindowEx()
window.show()
sys.exit(app.exec())