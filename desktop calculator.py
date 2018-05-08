import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#  Make a desktop calculator app with pyqt  (40pts)
#  Calculator will have the following functions and buttons. 
#     Answer label where your equation and answer will appear.  It will be nicely formatted and update properly with every button push. (10pts)
#     Clear button to zero your answer Label.  (2pts)
#     buttons 0 through 9.   (5pts)
#     *, /, -, and + buttons (5pts)
#     = button to evaluate the current answer label. (5pts)
#     Decimal button to add float capability (2pts)
#     All buttons, columns, and rows will be of same relative size. (3pts)
#     Use a stylesheet to change the color, font and size to approximately match the built in OS calulator app. (5pts)
#     Add one or more additional functional button to your calculator (square, sqrt, pi, memory, trig, or whatever you choose) (3pts)

#  Model your calculator after the built in calc on your operating system.  (minus the +/- and % buttons)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.eqn = ""
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(800, 150, 300, 300)
        # Widgets
        self.display = QLabel("0")
        self.grid.addWidget(self.display, 1, 1, 1, 4)

        self.button1 = QPushButton("9")
        self.grid.addWidget(self.button1, 3, 3, 1, 1)

        self.button2 = QPushButton("8")
        self.grid.addWidget(self.button2, 3, 2, 1, 1)

        self.button3 = QPushButton("7")
        self.grid.addWidget(self.button3, 3, 1, 1, 1)

        self.button4 = QPushButton("6")
        self.grid.addWidget(self.button4, 4, 3, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 4, 2, 1, 1)

        self.button6 = QPushButton("4")
        self.grid.addWidget(self.button6, 4, 1, 1, 1)

        self.button7 = QPushButton("3")
        self.grid.addWidget(self.button7, 5, 3, 1, 1)

        self.button8 = QPushButton("2")
        self.grid.addWidget(self.button8, 5, 2, 1, 1)

        self.button9 = QPushButton("1")
        self.grid.addWidget(self.button9, 5, 1, 1, 1)

        self.button10 = QPushButton("0")
        self.grid.addWidget(self.button10, 6, 1, 1, 2)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 6, 4, 1, 1)
        self.button_equal.setObjectName("basicfunc")

        self.button_clear = QPushButton("AC")
        self.grid.addWidget(self.button_clear, 2, 3, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 2, 4, 1, 1)
        self.button_add.setObjectName("basicfunc")

        self.button_subtract = QPushButton("-")
        self.grid.addWidget(self.button_subtract, 3, 4, 1, 1)
        self.button_subtract.setObjectName("basicfunc")

        self.button_multiply = QPushButton("x")
        self.grid.addWidget(self.button_multiply, 4, 4, 1, 1)
        self.button_multiply.setObjectName("basicfunc")

        self.button_divide = QPushButton("/")
        self.grid.addWidget(self.button_divide, 5, 4, 1, 1)
        self.button_divide.setObjectName("basicfunc")

        self.button_decimal = QPushButton(".")
        self.grid.addWidget(self.button_decimal, 6, 3, 1, 1)


        self.button_leftparenth = QPushButton("(")
        self.grid.addWidget(self.button_leftparenth, 2, 1, 1, 1)

        self.button_rightparenth = QPushButton(")")
        self.grid.addWidget(self.button_rightparenth, 2, 2, 1, 1)

        # Signals and Slots
        self.button1.clicked.connect(lambda: self.concat("9"))
        self.button2.clicked.connect(lambda: self.concat("8"))
        self.button3.clicked.connect(lambda: self.concat("7"))
        self.button4.clicked.connect(lambda: self.concat("6"))
        self.button5.clicked.connect(lambda: self.concat("5"))
        self.button6.clicked.connect(lambda: self.concat("4"))
        self.button7.clicked.connect(lambda: self.concat("3"))
        self.button8.clicked.connect(lambda: self.concat("2"))
        self.button9.clicked.connect(lambda: self.concat("1"))
        self.button10.clicked.connect(lambda: self.concat("0"))

        self.button_add.clicked.connect(lambda: self.concat("+"))
        self.button_subtract.clicked.connect(lambda: self.concat("-"))
        self.button_multiply.clicked.connect(lambda: self.concat("*"))
        self.button_divide.clicked.connect(lambda: self.concat("/"))
        self.button_decimal.clicked.connect(lambda: self.concat("."))
        self.button_leftparenth.clicked.connect(lambda: self.concat("("))
        self.button_rightparenth.clicked.connect(lambda: self.concat(")"))
        self.button_equal.clicked.connect(self.equal)
        self.button_clear.clicked.connect(self.clear)

        # Style
        self.style_sheet()
        self.show()

        # Set Style
    def style_sheet(self):
        style_sheet = "files/desktop calculator.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())
        # Draw
    def concat(self, val):
        self.eqn += val
        self.display.setText(self.eqn)
    def equal(self):
        try:
            answer = eval(self.eqn)
            self.display.setText(str(round(answer, 5)))
        except:
            self.display.setText("ERROR")
            self.eqn = ""
    def clear(self):
        self.display.setText("")
        self.eqn = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())