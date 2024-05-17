import sys 
from PyQt5.QtWidgets import * 
import PyQt5
print("PyQt5 version:", PyQt5.QtCore.QT_VERSION_STR)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
