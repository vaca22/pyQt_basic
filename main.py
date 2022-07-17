import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("gaga")

    label = QtWidgets.QLabel(win)
    label.setText("gaga")
    label.move(200, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #    print_hi('PyCharm')
    window()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
