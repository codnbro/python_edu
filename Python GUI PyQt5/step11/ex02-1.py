import sys 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import qdarkstyle


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("button", self)
        button.move(10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    win = MyWindow()
    win.show()
    app.exec_()
