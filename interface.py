import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import test2
class Example(QMainWindow, test2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ListOfTypes = ['Фильм','ova']
        ListOfGenres = ['Фильм','ova','ova','ova','ova','ova','ova','ova','ova'
                        ,'ova','ova','ova','ova','ova','ova','ova','ova']
        ListOfStudios = ['Tridgger','UfoTable','Mappa']
        ListOfAgeRatings = ['R','14+','0+']
        self.Type_Combobox.addItems(ListOfTypes)
        self.Studio_Combobox.addItems(ListOfStudios)
        self.AgeRating_Combobox.addItems(ListOfAgeRatings)
        layout = QVBoxLayout()
        for i in range(0,len(ListOfGenres)):
            label = QCheckBox(ListOfGenres[i], self)
            layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.scrollArea.setWidget(widget)
        self.scrollArea.show()


    def generate_pins(self, size=6, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    def buttonClicked(self):
        self.textEdit.append(self.generate_pins(10))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()
