import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()


    def paintEvent(self, e):
        if self.do_paint:
            print(e)
            qp = QPainter()
            qp.begin(self)
            self.drawEclipse(qp)
            qp.end()


    def drawEclipse(self, qp):

        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(25 + randrange(0, 100), 25 + randrange(0, 100), randrange(0, 100), randrange(0, 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())