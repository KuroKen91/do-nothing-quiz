import sys
from PyQt5 import QtGui, QtCore, QtWidgets
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

#make temporary logo/intro title
tempTitle = QtWidgets.QLabel(window)
tempTitle.setText('Do Nothing Quiz!')
tempTitle.move(90, 100)
tempTitle.setStyleSheet("font-size: 45px;"
    + "color: 'white'"
)
window.show()

#make button 
button = QPushButton("ENTER")
#indicate it is clickable
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
    "border: 5px solid 'orange';"
    + "font-size: 60px;"
    + "color: 'white'"
)
#place Widgets on grid (Item, Row, Column)
grid.addWidget(button, 1, 0)

#apply grind to window
window.setLayout(grid)

window.show()
sys.exit(app.exec())


#display Logo. Move up once I have a logo. Place between grid = QGridLayout() and between window.setLayout(grid)
#image = QPixmap("LOGO THING GOES HERE")
#logo = QLabel() 
#logo.setPixmap(image)
#logo(QtCore.Qt.AlignCenter)
#logo.setStyleSheet("margin-top: 50px;")

#Place logo on grid
#grid.addWidget(logo, 0, 0)