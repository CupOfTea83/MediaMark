import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
import mainwindow
from importexport import * 
from model import Model


class Application(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open('media_types.json', 'r') as file:
            list_of_types = json.load(file)
            list_of_types.sort()
        with open('genres.json', 'r') as file:
            list_of_genres = json.load(file)
            list_of_genres.sort()
        with open('ratings.json', 'r') as file:
            list_of_age_ratings = json.load(file)
            list_of_age_ratings.sort()
        with open('studios.json', 'r') as file:
            list_of_studios = json.load(file)
            list_of_studios.sort()
        self.type_combobox.addItems(list_of_types)
        self.age_rating_combobox.addItems(list_of_age_ratings)
               
        helper_layout = QVBoxLayout()
        for i in range(0,len(list_of_genres)):
            genre_label = QCheckBox(list_of_genres[i], self)
            helper_layout.addWidget(genre_label)
        helper_widget = QWidget()
        helper_widget.setLayout(helper_layout)
        self.genre_area.setWidget(helper_widget)
        self.genre_area.show()

        helper_layout = QVBoxLayout()
        for i in range(0,len(list_of_studios)):
            studio_label = QCheckBox(list_of_studios[i], self)
            helper_layout.addWidget(studio_label)
        helper_widget = QWidget()
        helper_widget.setLayout(helper_layout)
        self.studios_area.setWidget(helper_widget)
        self.studios_area.show()

        self.estimation_button.clicked.connect(self.estimate_clicked)
        self.load_action.triggered.connect(self.select_file)
        self.save_action.triggered.connect(self.save_clicked)
        self.model = Model()
    def estimate_clicked(self):
        list_of_selected_genres = []
        list_of_selected_studios = []
        for i in range(0, self.genre_area.widget().layout().count()):
            if (self.genre_area.widget().layout().itemAt(i).widget().isChecked()):
                list_of_selected_genres.append(self.genre_area.widget().layout().itemAt(i).widget().text())
        for i in range(0, self.studios_area.widget().layout().count()):
            if (self.studios_area.widget().layout().itemAt(i).widget().isChecked()):
                list_of_selected_studios .append(self.studios_area.widget().layout().itemAt(i).widget().text())
        score = self.model.getscore(name=self.name_text_edit.toPlainText(),
                               genres=list_of_selected_genres,
                               media_type=self.type_combobox.currentText(),
                               episodes=int(self.episode_count_lineEdit.text()) if len(self.episode_count_lineEdit.text()) > 0 else 0,
                               year=int(self.date_edit.date().year()),
                               description=self.description_text_edit.toPlainText(),
                               rating=self.age_rating_combobox.currentText(),
                               studios=list_of_selected_studios
                               )
        self.estimation_label.setText(str(round(score[0], 2)))
        self.full_estimation_label.setText(str(round(score[0], 6)))
    def save_clicked(self):
        res = QFileDialog.getSaveFileName()
        list_of_selected_genres = []
        list_of_selected_studios = []
        for i in range(0, self.genre_area.widget().layout().count()):
            if (self.genre_area.widget().layout().itemAt(i).widget().isChecked()):
                list_of_selected_genres.append(self.genre_area.widget().layout().itemAt(i).widget().text())
                
        for i in range(0, self.studios_area.widget().layout().count()):
            if (self.studios_area.widget().layout().itemAt(i).widget().isChecked()):
                list_of_selected_studios .append(self.studios_area.widget().layout().itemAt(i).widget().text())
       
        export(path=res[0],
               name = self.name_text_edit.toPlainText(),
                               genres=list_of_selected_genres,
                               media_type=self.type_combobox.currentText(),
                               episodes=int(self.episode_count_lineEdit.text()) if len(self.episode_count_lineEdit.text()) > 0 else 0,
                               year=int(self.date_edit.date().year()),
                               description=self.description_text_edit.toPlainText(),
                               rating=self.age_rating_combobox.currentText(),
                               studios=list_of_selected_studios

               )
    def select_file(self):
        res = QFileDialog.getOpenFileName()
        per = import_(path=res[0])
        if per:
            self.description_text_edit.setPlainText(per["description"])
            self.name_text_edit.setPlainText(per["name"])
            self.episode_count_lineEdit.setText(str(per["episodes"]))
            self.age_rating_combobox.setCurrentIndex(self.age_rating_combobox.findText(per["rating"]))
            self.type_combobox.setCurrentIndex(self.type_combobox.findText(per["media_type"]))
            self.date_edit.setDateTime(QDateTime(per["year"], 1, 1, 1, 1))
            print(len(per["genres"]))
            for i in range(0, self.genre_area.widget().layout().count()):
                if (self.genre_area.widget().layout().itemAt(i).widget().isChecked()):
                    self.genre_area.widget().layout().itemAt(i).widget().setChecked(False)
            list_of_selected_genres = per["genres"]
            for i in range(0, self.genre_area.widget().layout().count()):
                if (self.genre_area.widget().layout().itemAt(i).widget().text() in list_of_selected_genres):
                    self.genre_area.widget().layout().itemAt(i).widget().setChecked(True)

            for i in range(0, self.studios_area.widget().layout().count()):
                if (self.studios_area.widget().layout().itemAt(i).widget().isChecked()):
                    self.studios_area.widget().layout().itemAt(i).widget().setChecked(False)        
            list_of_selected_studios = per["studios"]
            for i in range(0, self.studios_area.widget().layout().count()):
                if (self.studios_area.widget().layout().itemAt(i).widget().text() in list_of_selected_studios):
                    self.studios_area.widget().layout().itemAt(i).widget().setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('stylesheet.css', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    form = Application()
    form.show()
    app.exec()
