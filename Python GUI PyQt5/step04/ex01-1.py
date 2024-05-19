import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)

        self.text = QPlainTextEdit(self)
        self.text.move(10, 10)
        self.text.resize(280, 180)

        # 텍스트 출력
        self.text.appendPlainText("Hello\n")
        self.text.appendPlainText("Python\n")
        self.text.appendPlainText("PlaneText\n")
        # self.text = QPlainTextEdit(self)
        # self.text.setReadOnly(True)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
