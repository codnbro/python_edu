import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon("pie-chart.png")) 


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
