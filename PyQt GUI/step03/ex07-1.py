import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton('button01')
        btn2 = QPushButton('button02')

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setCentralWidget(widget)

        # QWidgte->QVBoxLayout->QPushButton
        vbox = widget.findChildren(QVBoxLayout)[0]
        btn = vbox.itemAt(0).widget()
        print(btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
