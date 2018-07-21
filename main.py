'''


**Interactive Dictionary : A Desktop Application**

Language: Python3
Frameworks: PyQt5 (a wrapper around QT Framework in python)
Libraries: difflib(python3(inbuilt)

Made by :

        Abhishek Anand
        Lakshmi Narain College of Tehnology,Bhopal

        Github-id ->  https://github.com/Abhi-2109
        HackerEarth id -> https://www.hackerearth.com/@abhishek197770
        HackerRank Id -> https://www.hackerrank.com/abhishek197770
        CodeFights/ CodeSignals -> https://app.codesignal.com/profile/abhi2109

'''


from PyQt5.QtWidgets import *

import sys
import json
from difflib import get_close_matches

# Loading the data of the Json File into  a variable

data = json.load(open("076 data.json"))


# Setting MainWidget

class MainWidget():
    def setup(self, MainWindow):
        self.grid = QGridLayout()
        self.label = QLabel()
        self.inputBox = QLineEdit()
        self.searchButton = QPushButton()
        self.searchButton.setText("Search")
        self.label.setText("Type the word below to search the defination of the given word ")
        self.label.setStyleSheet('font-size: 11pt; font-family: Courier;')
        self.AnswerBox = QTextBrowser()
        self.inputBox.setPlaceholderText("Type the word here :")
        self.grid.addWidget(self.label,0,0,1,4)
        self.grid.addWidget(self.inputBox,2,0,1,3)
        self.grid.addWidget(self.searchButton,2,3,1,1)
        self.grid.addWidget(self.AnswerBox,3,0,8,4)
        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.widget)



# Setting SubWidget

class SubWidget1():
    def setup(self,MainWindow,words,searched_word):
        self.grid = QGridLayout()
        self.label = QLabel()
        self.AnswerBox = QTextBrowser()
        self.AnswerBox.setText("You searched for {} :\n\n\tThe word does not exits in dictionary data. Please recheck it".format(searched_word))
        self.label.setStyleSheet('font-size: 11pt; font-family: Courier;')
        self.inputBox = QLineEdit()
        self.searchButton = QPushButton()
        self.searchButton.setText("Search")
        self.inputBox.setPlaceholderText("Type the word here :")
        self.label.setText("Type the word below to search the defination of the given word ")
        self.Question = QLabel()
        self.Question.setStyleSheet('font-size: 12pt; font-family: Courier;')
        self.Question.setText("Did you mean? Click on the alternatives")
        self.grid.addWidget(self.label,0,0,1,4)
        self.grid.addWidget(self.inputBox,2,0,1,3)
        self.grid.addWidget(self.searchButton,2,3,1,1)
        self.alter = QLabel()
        self.line = QLabel()
        self.line.setText('-'*135)
        self.grid.addWidget(self.AnswerBox,3,0,1,4)
        self.grid.addWidget(self.Question,4,0,1,4)
        self.grid.addWidget(self.alter,5,0,1,1)
        row = 6
        col = 0
        i = 0
        self.option = []
        while row < 13 and len(words)!=0:
            if col == 4:
                col = 0
                row += 1
            option = QPushButton()
            option.setText(words[0])
            self.option.append(option)

            words = words[1:]
            self.grid.addWidget(self.option[-1],row,col,1,1)
            col+=1
        row+=1
        while row <13:
            self.grid.addWidget(self.alter,row,1,1,4)
            row+=1






        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.widget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Dictionary")
        self.MainWidget = MainWidget()
        self.SubWidget1 = SubWidget1()
        self.startMainWidget()
    def startMainWidget(self):
        self.MainWidget.setup(self)
        self.MainWidget.searchButton.clicked.connect(self.change1)
        self.MainWidget.inputBox.returnPressed.connect(self.change1)
        self.show()
    def startWidget1(self, words,searched_word):
        self.SubWidget1.setup(self, words,searched_word)
        self.SubWidget1.inputBox.returnPressed.connect(lambda : self.change2(self.SubWidget1.inputBox.text()))
        self.SubWidget1.searchButton.clicked.connect(lambda: self.change2(self.SubWidget1.inputBox.text()))
        self.SubWidget1.option[0].clicked.connect(lambda: self.change2(self.SubWidget1.option[0].text()))
        self.SubWidget1.option[1].clicked.connect(lambda : self.change2(self.SubWidget1.option[1].text()))
        self.SubWidget1.option[2].clicked.connect(lambda: self.change2(self.SubWidget1.option[2].text()))
        self.SubWidget1.option[3].clicked.connect(lambda: self.change2(self.SubWidget1.option[3].text()))
        self.SubWidget1.option[4].clicked.connect(lambda: self.change2(self.SubWidget1.option[4].text()))
        self.SubWidget1.option[5].clicked.connect(lambda: self.change2(self.SubWidget1.option[5].text()))
        self.SubWidget1.option[6].clicked.connect(lambda: self.change2(self.SubWidget1.option[6].text()))
        self.SubWidget1.option[7].clicked.connect(lambda: self.change2(self.SubWidget1.option[7].text()))
        self.SubWidget1.option[8].clicked.connect(lambda: self.change2(self.SubWidget1.option[8].text()))
        self.SubWidget1.option[9].clicked.connect(lambda: self.change2(self.SubWidget1.option[9].text()))
        self.SubWidget1.option[10].clicked.connect(lambda: self.change2(self.SubWidget1.option[10].text()))
        self.SubWidget1.option[11].clicked.connect(lambda: self.change2(self.SubWidget1.option[11].text()))
        self.SubWidget1.option[12].clicked.connect(lambda: self.change2(self.SubWidget1.option[12].text()))
        self.SubWidget1.option[13].clicked.connect(lambda: self.change2(self.SubWidget1.option[13].text()))
        self.SubWidget1.option[14].clicked.connect(lambda: self.change2(self.SubWidget1.option[14].text()))
        self.SubWidget1.option[15].clicked.connect(lambda: self.change2(self.SubWidget1.option[15].text()))
        self.SubWidget1.option[16].clicked.connect(lambda: self.change2(self.SubWidget1.option[16].text()))
        self.SubWidget1.option[17].clicked.connect(lambda: self.change2(self.SubWidget1.option[17].text()))
        self.SubWidget1.option[18].clicked.connect(lambda: self.change2(self.SubWidget1.option[18].text()))
        self.SubWidget1.option[19].clicked.connect(lambda: self.change2(self.SubWidget1.option[19].text()))

        self.show()

    def change2(self,word):
        self.startMainWidget()
        self.MainWidget.inputBox.setText(word)
        self.change1()


    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Review",
            "Do You Like this Appliaction?",
            QMessageBox.Yes | QMessageBox.No| QMessageBox.Cancel)
        if reply == QMessageBox.Yes or reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()

    def change1(self):
        if self.MainWidget.inputBox.text() == "":
            self.startMainWidget()
        else:
            if self.MainWidget.inputBox.text() in data :
                j=1
                s = self.MainWidget.inputBox.text() + ': \n\n'
                for i in data[self.MainWidget.inputBox.text()]:
                    s = s + '  ' + str(j)+'. ' + i+'\n\n'
                    j+=1
                self.MainWidget.AnswerBox.setText(s)
            elif self.MainWidget.inputBox.text().lower() in data:
                s = self.MainWidget.inputBox.text().lower() + ': \n\n'
                j = 1
                for i in data[self.MainWidget.inputBox.text().lower()]:
                    s = s + '  ' + str(j) + '. ' + i + '\n\n'
                    j += 1
                self.MainWidget.AnswerBox.setText(s)
            elif self.MainWidget.inputBox.text().title() in data:
                s = self.MainWidget.inputBox.text().title() + ': \n\n'
                j = 1
                for i in data[self.MainWidget.inputBox.text().title()]:
                    s = s + '  ' + str(j) + '. ' + i + '\n\n'
                    j += 1
                self.MainWidget.AnswerBox.setText(s)
            elif self.MainWidget.inputBox.text().upper() in data:
                s = self.MainWidget.inputBox.text().upper() + ': \n\n'
                j = 1
                for i in data[self.MainWidget.inputBox.text().upper()]:
                    s = s + '  ' + str(j) + '. ' + i + '\n\n'
                    j += 1
                self.MainWidget.AnswerBox.setText(s)
            else :
                a = get_close_matches(self.MainWidget.inputBox.text(),data,cutoff=0.01,n=20)
                if len(a) == 0 :
                    self.MainWidget.AnswerBox.setText("You searched for {} \n\n\tThe word does not exits in dictionary data. Please recheck it".format(self.MainWidget.inputBox.text()))
                else:
                    self.startWidget1(a,self.MainWidget.inputBox.text())

            self.MainWidget.inputBox.setText("")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedHeight(400)
    window.setFixedWidth(600)
    sys.exit(app.exec_())
