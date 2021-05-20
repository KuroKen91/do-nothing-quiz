import sys
import json
import socket
import getpass
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor

#get data from seperate file
file = open('data.json')
file_data = json.load(file)

#get IP address of user. If you do not want to reveal this, comment out lines 14 - 23 and uncomment line 24
def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('10.255.255.255', 1))
        IP = sock.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        sock.close()
    return IP
    # return IP = '1.1.1.1'

#load the data from custom json file. Can try backend here!
def load_data():
     question = (file_data["question"])
     options = (file_data["options"])
     answers = (file_data['answer'])

     data['question'].append(question)
     data["answer"].append(answers)
     data["option1"].append(options[0])
     data["option2"].append(options[1])
     data["IP"] = get_ip()

data = {
    "question": [],
    "option1": [],
    "option2": [],
    "answer": [],
    "score": [0],
    "q_number": 0,
    "IP": ''
}


widgets = {
    "temp": [],
    "button": [],
    "score": [],
    "question": [],
    "option1": [],
    "option2": [],
    "message": [],
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Do Nothing Quiz")
window.setFixedWidth(700)
window.setFixedHeight(700)
window.move(400, 100) #determines where window opens (x,y)
window.setStyleSheet("background: purple;")


grid = QGridLayout()

load_data()

#remove widgets off GUI
def remove_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

#reset the parameters


def return_to_title():
    remove_widgets()
    data["score"] = [0]
    data["q_number"] = 0
    data["question"]
    titleScreen()

def start_game():
    remove_widgets()
    load_data()
    titleScreen()

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
    button.clicked.connect(lambda n: is_correct(answer))
    return button

#checking if answer is correct
def is_correct(answer):
    temp_score = data["score"][-1]
    if answer == data["answer"][0][data["q_number"]]:
        #replace score with new one
        data["score"].pop()
        data["score"].append(temp_score + 10)
        if temp_score == 30:
            remove_widgets()
            win_page()
        else :
            print(data["question"])
            print(answer + " is correct!")
            print(data["q_number"])
            data["q_number"] += 1
            print(data["q_number"])

            if data["q_number"] == 2: 
                widgets["score"][-1].setText(str(data["score"][-1]))
                widgets["question"][0].setText(str(data["question"][0][data["q_number"]] +  "-" + data["IP"]))

            else:
                widgets["score"][-1].setText(str(data["score"][-1]))
                widgets["question"][0].setText(data["question"][0][data["q_number"]])

    else:
        remove_widgets()
        lose_page()


#start at title screen
def titleScreen():
    print(data["IP"])
    print(data["answer"])
    print(data["question"][0])
    #make temporary logo/intro title
    # tempTitle = QtWidgets.QLabel(window)
    # tempTitle.setText('Do Nothing Quiz!')
    # tempTitle.move(90, 100)
    # tempTitle.setStyleSheet("font-size: 45px;"
    #     + "color: 'white'"
    # )
    #widgets["temp"].append(tempTitle) #replace with logo later
    # window.show()

    #make button 
    enter_button = QPushButton("ENTER")
    #indicate it is clickable
    enter_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    enter_button.setStyleSheet(
        "*{border: 5px solid 'white';"
        + "font-size: 60px;"
        + "margin: 50px 100px;"
        + "padding: 25px 0;"
        + "border-radius: 15px;}"
        + "*:hover{background: 'white';}"
    )
    enter_button.clicked.connect(begin_test)
    widgets["button"].append(enter_button) #global variable now accessible in function block. appends object to list

    #place Widgets on grid (Item, Row, Column)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)
    # grid.addWidget(widgets["temp"][-1], 1, 0, 1, 2)


#Begin testing screen
def begin_test():
    score = QLabel(str(data["score"][-1])) #set later
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-size: 35px;"
        "border: 1px solid 'white';"
        "background: 'white';"
        "border-radius: 50px;"
        "padding: 50px 25px;"
    )
    widgets["score"].append(score)
   
    
    question = QLabel(data['question'][0][data["q_number"]])
    question = QLabel(data['question'][0][data["q_number"]])

    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-size: 50px;"
        "color: 'white';"
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = make_buttons(data['option1'][0])
    button2 = make_buttons(data['option2'][0])

    widgets["option1"].append(button1)
    widgets["option2"].append(button2)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2) #row and column span
    grid.addWidget(widgets["option1"][-1], 2, 0)
    grid.addWidget(widgets["option2"][-1], 2, 1)

# WIN RESULT PAGE - LINK TO POEM perhaps?
def win_page():
    win_message = QLabel("Congrats!\n Your Final Score Was:")
    win_message.setAlignment(QtCore.Qt.AlignCenter)
    win_message.setStyleSheet(
        "font-size: 35px;"
        "color: 'white';"
    )

    final_score = QLabel(str(data["score"][-1]))
    final_score.setStyleSheet(
        "font-size: 35px;"
        "color: 'white';"
    )

    restart_button = QPushButton("Restart")
    restart_button.setStyleSheet(
        "*{border: 5px solid 'white';"
        + "font-size: 60px;"
        + "margin: 50px 100px;"
        + "padding: 25px 0;"
        + "border-radius: 15px;}"
        + "*:hover{background: 'white';}"
    )
    restart_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    restart_button.clicked.connect(return_to_title)

    widgets["message"].append(win_message)
    widgets["score"].append(final_score)
    widgets["button"].append(restart_button)

    grid.addWidget(widgets["message"][-1], 0, 1)
    grid.addWidget(widgets["score"][-1], 1, 2)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)


def lose_page():
    data["q_number"] += 1
    lose_message = QLabel("Get bent...")
    lose_message.setAlignment(QtCore.Qt.AlignCenter)
    lose_message.setStyleSheet(
        "font-size: 35px;"
        "color: 'white';"
    )

    final_score = QLabel(str(data["score"][-1]))
    final_score.setStyleSheet(
        "font-size: 35px;"
        "color: 'white';"
    )

    restart_button = QPushButton("Restart")
    restart_button.setStyleSheet(
        "*{border: 5px solid 'white';"
        + "font-size: 60px;"
        + "margin: 50px 100px;"
        + "padding: 25px 0;"
        + "border-radius: 15px;}"
        + "*:hover{background: 'white';}"
    )
    restart_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    restart_button.clicked.connect(return_to_title)

    widgets["message"].append(lose_message)
    widgets["score"].append(final_score)
    widgets["button"].append(restart_button)
    
    grid.addWidget(widgets["message"][-1], 0, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["score"][-1], 1, 0)


#beginTest()
get_ip()
titleScreen()
# win_page()

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