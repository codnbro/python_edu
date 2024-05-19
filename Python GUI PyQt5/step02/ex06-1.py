import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 1000) # 화면 시작 0, 0 화면 출력 가로 X 세로 (0,0 하면 기본)

        self.cbox = QCheckBox("미수", self)
        self.cbox.move(10, 10)
        self.cbox.stateChanged.connect(self.slot)

    def slot(self, state):
        if state == Qt.Checked:
            print("미수") 
        else:
            print("보통")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

