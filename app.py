import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Do Nothing Quiz")
window.setFixedWidth(750)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()


window.setLayout(grid)

window.show()
sys.exit(app.exec())
#display Logo
#image = QPixmap("LOGO THING GOES HERE")
#logo = QLabel() 
#logo.setPixmap(image)

#Place logo on grid
#grid.addWidget(logo, 0, 0)