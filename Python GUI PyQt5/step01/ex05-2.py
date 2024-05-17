import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("버튼", self)
        btn.move(10, 10)
        btn.clicked.connect(self.buy)

    def buy(self):
        print("몽땅 매수")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
