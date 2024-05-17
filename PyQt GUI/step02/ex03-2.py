import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(10, 10)
        self.line_edit.textChanged.connect(self.text_changed)       # 텍스트 입력이 변경될 때

    def text_changed(self):
        text = self.line_edit.text()    # QLineEdit 위젯에 입력된 텍스트 가져오기
        print(text)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
