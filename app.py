import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor

widgets = {
    "temp": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Do Nothing Quiz")
window.setFixedWidth(700)
window.setFixedHeight(700)
window.move(400, 100) #determines where window opens (x,y)
window.setStyleSheet("background: purple;")


grid = QGridLayout()

#remove widgets off GUI
def remove_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def start_game():
    remove_widgets()
    beginTest()

#make the buttons 
def make_buttons(answer):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(200)
    button.setStyleSheet(
        "*{border: 5px solid 'white';"
        + "font-size: 20px;"
        + "padding: 25px 0;"
        + "margin-bottom: 120px;"
        + "border-radius: 15px;}"
        + "*:hover{background: 'white';}"
    )
    return button


#start at title screen
def titleScreen():

    #make temporary logo/intro title
    # tempTitle = QtWidgets.QLabel(window)
    # tempTitle.setText('Do Nothing Quiz!')
    # tempTitle.move(90, 100)
    # tempTitle.setStyleSheet("font-size: 45px;"
    #     + "color: 'white'"
    # )
    # #widgets["temp"].append(tempTitle) #replace with logo later
    # window.show()

    #make button 
    enterButton = QPushButton("ENTER")
    #indicate it is clickable
    enterButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    enterButton.setStyleSheet(
        "*{border: 5px solid 'white';"
        + "font-size: 60px;"
        + "margin: 50px 100px;"
        + "padding: 25px 0;"
        + "border-radius: 15px;}"
        + "*:hover{background: 'white';}"
    )
    enterButton.clicked.connect(start_game)
    widgets["button"].append(enterButton) #global variable now accessible in function block. appends object to list

    #place Widgets on grid (Item, Row, Column)
    grid.addWidget(widgets["button"][-1], 1, 0)
    #grid.addWidget(widgets["temp"][-1], 1, 0)

#titleScreen() #call the title screen
#Begin testing screen
def beginTest():
    score = QLabel("Score: 80") #set later
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-size: 35px;"
        "border: 1px solid 'white';"
        "background: 'white';"
        "border-radius: 50px;"
        "padding: 50px 25px;"
    )
    widgets["score"].append(score)

    question = QLabel("QUESTION GOES HERE")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-size: 50px;"
        "color: 'white';"
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = make_buttons("answer1")
    button2 = make_buttons("answer2")

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2) #row and column span
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)

#beginTest()
titleScreen()

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