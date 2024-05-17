import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 400, 400, 300)

        btn = QPushButton("Trading Start", self)
        btn.setToolTip("Trading Start <b>Button</b>")
        btn.move(10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
