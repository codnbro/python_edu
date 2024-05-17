import sys 
from PyQt5.QtWidgets import *
import pyqtgraph as pg 


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(title="Basic Plot w/ symbol") 
        x = [1, 2, 3, 4]
        y = [1, 2, 3, 4]
        w.plot(x=x, y=y, symbol='o')
        w.setBackground('w')
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
