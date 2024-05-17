import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)

        # line
        painter.setPen(QColor(255, 0, 0))
        painter.drawLine(QPoint(85, 10), QPoint(85, 90)) 

        # rect
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(QRect(80, 20, 10, 60))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
