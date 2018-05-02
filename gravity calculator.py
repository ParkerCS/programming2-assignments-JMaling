# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a pyqt5 app with the following attributes:
# - use an App/Window class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function or custom method
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed. 
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 2 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(800, 150, 550, 300)
        # Widgets
        self.title = QLabel("Gravity Calculator") # changed the padding to center the title
        self.grid.addWidget(self.title, 1, 1, 2, 1)
        self.title.setObjectName("title")
        self.mass1 = QLabel("Enter Mass #1 (kg)")
        self.grid.addWidget(self.mass1, 2, 1, 1, 1)
        self.mass2 = QLabel("Enter Mass #2 (kg)")
        self.grid.addWidget(self.mass2, 3, 1, 1, 1)
        self.radius = QLabel("Enter Radius (m)")
        self.grid.addWidget(self.radius, 4, 1, 1, 1)
        self.mass1enter = QLineEdit()
        self.grid.addWidget(self.mass1enter, 2, 2, 1, 1)
        self.mass2enter = QLineEdit()
        self.grid.addWidget(self.mass2enter, 3, 2, 1, 1)
        self.radiusenter = QLineEdit()
        self.grid.addWidget(self.radiusenter, 4, 2, 1, 1)
        self.calc = QPushButton("Calculate Force of Gravity")
        self.grid.addWidget(self.calc, 5, 1, 1, 1)
        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 5, 2, 1, 1)

        # Signals/Slots
        self.show()
        self.style_sheet()
        self.calc.clicked.connect(self.find_grav)

        # Set Style
        # changed the background color to white and the text color to blue
        # changed the font size and style
    def style_sheet(self):
        style_sheet = "files/PYQT Gravity Calc.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())
        # Draw
    def find_grav(self):
        try:
            m1 = float(self.mass1enter.text())
            m2 = float(self.mass2enter.text())
            r = float(self.radiusenter.text())
            f = round(((.0000000000667 * (m1 * m2)) / (r ** 2)), 9)
            self.answer.setText(str(f))
        except:
            self.answer.setText("Please Enter a Valid Radius")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())

