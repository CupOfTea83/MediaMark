import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
import test2
from ImportExport import * 
from Model import Model
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
        self.Load_action.triggered.connect(self.SelectFile)
        self.Save_action.triggered.connect(self.SaveClicked)
        self.model = Model()
    def Estimateclicked(self):
        ListOfSelectedGenres = []
        ListOfSelectedStudios = []
        for i in range(0,self.GenreArea.widget().layout().count()):
            if (self.GenreArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedGenres.append(self.GenreArea.widget().layout().itemAt(i).widget().text())
        for i in range(0,self.StudiosArea.widget().layout().count()):
            if (self.StudiosArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedStudios .append(self.StudiosArea.widget().layout().itemAt(i).widget().text())
        score = self.model.GetScore(name = self.Name_textEdit.toPlainText(),
                               genres = ListOfSelectedGenres,
                               media_type = self.Type_Combobox.currentText(),
                               episodes = int(self.EpisodeCount_lineEdit.text()) if len(self.EpisodeCount_lineEdit.text())>0 else 0,#точно так?
                               year = int(self.dateEdit.date().year()),
                               description = self.Description_textEdit.toPlainText(),
                               rating = self.AgeRating_Combobox.currentText(),
                               studios = ListOfSelectedStudios
                               )
        self.Estimation_label.setText(str(round(score[0],2)))
        self.FullEstimation_label.setText(str(round(score[0],6)))
        print(score[0])
    def SaveClicked(self):
        #print("work")
        res = QFileDialog.getSaveFileName()
        ListOfSelectedGenres = []
        ListOfSelectedStudios = []
        for i in range(0,self.GenreArea.widget().layout().count()):
            if (self.GenreArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedGenres.append(self.GenreArea.widget().layout().itemAt(i).widget().text())
                
        for i in range(0,self.StudiosArea.widget().layout().count()):
            if (self.StudiosArea.widget().layout().itemAt(i).widget().isChecked()):
                ListOfSelectedStudios .append(self.StudiosArea.widget().layout().itemAt(i).widget().text())
       
        Export(path=res[0],
               name = self.Name_textEdit.toPlainText(),
                               genres = ListOfSelectedGenres,
                               media_type = self.Type_Combobox.currentText(),
                               episodes = int(self.EpisodeCount_lineEdit.text()) if len(self.EpisodeCount_lineEdit.text())>0 else 0,#точно так?
                               year = int(self.dateEdit.date().year()),
                               description = self.Description_textEdit.toPlainText(),
                               rating = self.AgeRating_Combobox.currentText(),
                               studios = ListOfSelectedStudios

               )
    def SelectFile(self):
        #print("work")
        res = QFileDialog.getOpenFileName()
        per = Import(path=res[0])
        print(per)
        if per != False:
            self.Description_textEdit.setPlainText(per["description"])
            self.Name_textEdit.setPlainText(per["name"])
            self.EpisodeCount_lineEdit.setText(str(per["episodes"]))
            self.AgeRating_Combobox.setCurrentIndex(self.AgeRating_Combobox.findText(per["rating"]))
            self.Type_Combobox.setCurrentIndex(self.Type_Combobox.findText(per["media_type"]))
            self.dateEdit.setDateTime(QDateTime(per["year"],1,1,1,1))
            print(len(per["genres"]))
            for i in range(0,self.GenreArea.widget().layout().count()):
                if (self.GenreArea.widget().layout().itemAt(i).widget().isChecked()):
                    self.GenreArea.widget().layout().itemAt(i).widget().setChecked(False)
            ListOfSelectedGenres = per["genres"]
            for i in range(0,self.GenreArea.widget().layout().count()):
                if (self.GenreArea.widget().layout().itemAt(i).widget().text() in ListOfSelectedGenres):
                    self.GenreArea.widget().layout().itemAt(i).widget().setChecked(True)

            for i in range(0,self.StudiosArea.widget().layout().count()):
                if (self.StudiosArea.widget().layout().itemAt(i).widget().isChecked()):
                    self.StudiosArea.widget().layout().itemAt(i).widget().setChecked(False)        
            ListOfSelectedStudios = per["studios"]
            for i in range(0,self.StudiosArea.widget().layout().count()):
                if (self.StudiosArea.widget().layout().itemAt(i).widget().text() in ListOfSelectedStudios):
                    self.StudiosArea.widget().layout().itemAt(i).widget().setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()
