import sys 
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

win = QWidget()
win.show()   # 화면에 보여지게 함

app.exec_() # 이벤트 루프 시작
