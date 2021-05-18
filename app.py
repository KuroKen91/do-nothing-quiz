import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Do Nothing Quiz")
window.setFixedWidth(500)
window.setFixedHeight(500)
window.move(500, 200) #determines where window opens (x,y)
window.setStyleSheet("background: purple;")


grid = QGridLayout()


#apply grind to window
window.setLayout(grid)

window.show()
sys.exit(app.exec())


#display Logo. Move up once I have a logo
#image = QPixmap("LOGO THING GOES HERE")
#logo = QLabel() 
#logo.setPixmap(image)

#Place logo on grid
#grid.addWidget(logo, 0, 0)