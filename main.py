import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindows(QMainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("gaga")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("gaga")
        self.label.move(20, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you press the button")




def window():
    app = QApplication(sys.argv)
    win = MyWindows()

    win.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #    print_hi('PyCharm')
    window()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
