from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(["qt01.py"])
window = MyWindow()
window.show()
app.exec_()


'''
파이썬에서 super( )는 부모클래스
MyWindow 클래스는 QMainWindow 클래스를 상속 받는데 생성자에서 부모클래스인 QMainWindow의 생성자를 호출 
이는 QMainWindow 클래스가 요구하는 사항이지 모든 클래스를 상속 받을 때 반드시 부모 클래스의 생성자를 명시적으로 호출해야하는 것은 아니며
어찌됐든 우리는 MyWindow 클래스의 생성자에서 부모 클래스인 QMainWindow 클래스의 생성자를 호출해야 한다.
'''