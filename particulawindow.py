from PySide2.QtWidgets import QMainWindow
from particula_ui import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.pushButton.clicked.connect(self.agregar_click)
    @Slot()
    def agregar_click(self):
        print("CLICK")