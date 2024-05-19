import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.balance = 0  # balance 초기화
        self.timer = QTimer(self)
        self.timer.singleShot(3000, self.login_callback)
        self.check_balance()


    def login_callback(self):
        self.balance = 100
        print("Login completed.")  # 로그인 콜백이 호출되었음을 확인하기 위한 출력

    def check_balance(self):
        print(self.balance)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()     # main event loop
