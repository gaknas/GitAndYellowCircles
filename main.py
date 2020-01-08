import sys
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.draw = False
        self.k = 20
        self.coordinates = []
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')

        self.pushButton.clicked.connect(self.run)

    def run(self):
        k = random.randint(10, 100)
        x_pos = random.randint(10, 556)
        y_pos = random.randint(10, 332)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.coordinates.append([x_pos, y_pos, k, r, g, b])
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        for i in self.coordinates:
            qp.setBrush(QColor(i[3], i[4], i[5]))
            qp.drawEllipse(i[0], i[1], i[2], i[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
