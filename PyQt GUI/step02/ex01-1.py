import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("종료", self)
        self.btn.move(20, 20)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
