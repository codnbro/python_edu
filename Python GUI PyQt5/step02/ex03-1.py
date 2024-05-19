import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.setEnabled(True)
        self.line_edit.setText("Hello")
        self.line_edit.move(10, 10)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
