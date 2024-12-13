import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
import test2
class Example(QMainWindow, test2.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open('media_types.json', 'r') as file:
            ListOfTypes = json.load(file)
            ListOfTypes.sort()
        with open('genres.json', 'r') as file:
            ListOfGenres = json.load(file)
            ListOfGenres.sort()
        with open('ratings.json', 'r') as file:
            ListOfAgeRatings = json.load(file)
            ListOfAgeRatings.sort()
        with open('studios.json', 'r') as file:
            ListOfStudios = json.load(file)
            ListOfStudios.sort()
        self.Type_Combobox.addItems(ListOfTypes)#коллекция для типа
        self.AgeRating_Combobox.addItems(ListOfAgeRatings)#коллекция для возраста
               
        HelperLayout = QVBoxLayout()
        for i in range(0,len(ListOfGenres)):
            GenreLabel = QCheckBox(ListOfGenres[i], self)
            HelperLayout.addWidget(GenreLabel)
        HelperWidget = QWidget()
        HelperWidget.setLayout(HelperLayout)
        self.GenreArea.setWidget(HelperWidget)
        self.GenreArea.show()

        HelperLayout = QVBoxLayout()
        for i in range(0,len(ListOfStudios)):
            StudioLabel = QCheckBox(ListOfStudios[i], self)
            HelperLayout.addWidget(StudioLabel)
        HelperWidget = QWidget()
        HelperWidget.setLayout(HelperLayout)
        self.StudiosArea.setWidget(HelperWidget)
        self.StudiosArea.show()

        self.Estimation_button.clicked.connect(self.Estimateclicked)# событие нажатия на кнопку
    def Estimateclicked(self):
        self.Estimation_label.setText('3.3')
        ListOfSelectedGenres = []
        ListOfSelectedStudios = []
        for i in range(0,self.GenreArea.widget().layout().count()):
            if (self.GenreArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedGenres.append(self.GenreArea.widget().layout().itemAt(i).widget().text())
        for i in range(0,self.StudiosArea.widget().layout().count()):
            if (self.StudiosArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedStudios .append(self.StudiosArea.widget().layout().itemAt(i).widget().text())
        print(ListOfSelectedGenres)
        print(ListOfSelectedStudios )
stylesheet = """
    QMainWindow {
        background-image: url("fon1.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
    QLabel {
        font: 20pt Segoe UI Semibold;
    }
    QLabel#Estimation_label {
        font: 20pt Segoe UI Semibold;
        background-color: #ddfff7;
    }
    QPushButton {
        font: 15pt Segoe UI Semibold;
    }
    QComboBox {
        font: 10pt Segoe UI Semibold;
    }
    QLineEdit {
        font: 10pt Segoe UI Semibold;
    }
    QDateEdit {
        font: 10pt Segoe UI Semibold;
    }
    QCheckBox {
        font: 10pt Segoe UI Semibold;
    }
"""    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    form = Example()
    form.show()
    app.exec()
