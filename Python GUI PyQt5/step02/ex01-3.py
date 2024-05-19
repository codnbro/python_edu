import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("종료", self)
        btn.resize(100, 30)
        btn.setEnabled(True)          # 활성화
        #btn.setDisabled(True)         # 비활성화
        btn.clicked.connect(self.btn_clicked)
        print(btn.text())

    # 버튼이 클릭될 때 호출되는 메서드
    def btn_clicked(self):
        self.close()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
