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
               
        layout = QVBoxLayout()
        for i in range(0,len(ListOfGenres)):
            label = QCheckBox(ListOfGenres[i], self)
            layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.GenreArea.setWidget(widget)
        self.GenreArea.show()

        layout = QVBoxLayout()
        for i in range(0,len(ListOfStudios)):
            label = QCheckBox(ListOfStudios[i], self)
            layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.StudiosArea.setWidget(widget)
        self.StudiosArea.show()
        
    def buttonClicked(self):
        self.textEdit.append(self.generate_pins(10))
stylesheet = """
    QMainWindow {
        background-image: url("fon1.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
    QLabel {
        font: 20pt Segoe UI Semibold;
    }
    QLabel#label {
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
