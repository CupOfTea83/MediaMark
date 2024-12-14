# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 870)
        font = QtGui.QFont()
        font.setPointSize(30)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"        background-color: #F0F0F0FF;\n"
"        background-repeat: no-repeat; \n"
"        background-position: center;\n"
"    }\n"
"    QLabel {\n"
"        font: 10pt Segoe UI Semibold;\n"
"    }\n"
"    QLabel#Estimation_label {\n"
"        font: 20pt Segoe UI Semibold;\n"
"        background-color: #ddfff7;\n"
"        border: 2px solid black;\n"
"    }\n"
"QLabel#MediaMark_main_label {\n"
"        font: 15pt Segoe UI Semibold;\n"
"    }\n"
"QLabel#FullEstimation_label {\n"
"        font: 20pt Segoe UI Semibold;\n"
"        background-color: #ddffd9;\n"
"        border: 2px solid black;\n"
"    }\n"
"    QPushButton {\n"
"        font: 15pt Segoe UI Semibold;\n"
"        border: 1px solid black;\n"
"    }\n"
"    QComboBox {\n"
"        font: 10pt Segoe UI Semibold;\n"
"    }\n"
"    QLineEdit {\n"
"        font: 10pt Segoe UI Semibold;\n"
"    }\n"
"    QDateEdit {\n"
"        font: 10pt Segoe UI Semibold;\n"
"    }\n"
"    QCheckBox {\n"
"        font: 10pt Segoe UI Semibold;\n"
"    }\n"
"    QTextEdit\n"
"{\n"
"    font: 10pt Segoe UI Semibold;\n"
"    border: 1px solid black;\n"
"}\n"
"QScrollArea\n"
"{\n"
"    border: 1px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 5, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Description_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Description_label.setFont(font)
        self.Description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Description_label.setObjectName("Description_label")
        self.gridLayout_7.addWidget(self.Description_label, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 1, 1, 1)
        self.Description_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Description_textEdit.setObjectName("Description_textEdit")
        self.gridLayout_7.addWidget(self.Description_textEdit, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_7, 5, 0, 1, 7)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Genre_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Genre_label.setFont(font)
        self.Genre_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Genre_label.setObjectName("Genre_label")
        self.gridLayout_4.addWidget(self.Genre_label, 0, 0, 1, 2)
        self.GenreArea = QtWidgets.QScrollArea(self.centralwidget)
        self.GenreArea.setWidgetResizable(True)
        self.GenreArea.setObjectName("GenreArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 191, 85))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(191, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 191, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Genres = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Genres.setContentsMargins(0, 0, 0, 0)
        self.Genres.setObjectName("Genres")
        self.GenreArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.GenreArea, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 4, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Studio_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Studio_label.setFont(font)
        self.Studio_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Studio_label.setObjectName("Studio_label")
        self.gridLayout_5.addWidget(self.Studio_label, 0, 0, 1, 1)
        self.StudiosArea = QtWidgets.QScrollArea(self.centralwidget)
        self.StudiosArea.setWidgetResizable(True)
        self.StudiosArea.setObjectName("StudiosArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 437, 85))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Studios = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Studios.setContentsMargins(0, 0, 0, 0)
        self.Studios.setObjectName("Studios")
        self.StudiosArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.addWidget(self.StudiosArea, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 4, 4, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        self.MediaMark_main_label = QtWidgets.QLabel(self.centralwidget)
        self.MediaMark_main_label.setEnabled(True)
        self.MediaMark_main_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.MediaMark_main_label.setFont(font)
        self.MediaMark_main_label.setObjectName("MediaMark_main_label")
        self.gridLayout.addWidget(self.MediaMark_main_label, 0, 1, 1, 6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Name_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Name_label.setFont(font)
        self.Name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_label.setObjectName("Name_label")
        self.gridLayout_3.addWidget(self.Name_label, 0, 0, 1, 1)
        self.Name_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Name_textEdit.setObjectName("Name_textEdit")
        self.gridLayout_3.addWidget(self.Name_textEdit, 1, 0, 1, 5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 0, 2, 1, 1)
        self.Date_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Date_label.setFont(font)
        self.Date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Date_label.setObjectName("Date_label")
        self.gridLayout_3.addWidget(self.Date_label, 3, 0, 1, 3)
        self.EpisodeCount_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.EpisodeCount_label.setFont(font)
        self.EpisodeCount_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EpisodeCount_label.setObjectName("EpisodeCount_label")
        self.gridLayout_3.addWidget(self.EpisodeCount_label, 4, 0, 1, 3)
        self.Type_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.Type_Label.setFont(font)
        self.Type_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Type_Label.setObjectName("Type_Label")
        self.gridLayout_3.addWidget(self.Type_Label, 5, 0, 1, 3)
        self.AgeRating_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.AgeRating_label.setFont(font)
        self.AgeRating_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AgeRating_label.setObjectName("AgeRating_label")
        self.gridLayout_3.addWidget(self.AgeRating_label, 6, 0, 1, 3)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 3, 3, 1, 2)
        self.EpisodeCount_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EpisodeCount_lineEdit.setObjectName("EpisodeCount_lineEdit")
        self.gridLayout_3.addWidget(self.EpisodeCount_lineEdit, 4, 3, 1, 2)
        self.Type_Combobox = QtWidgets.QComboBox(self.centralwidget)
        self.Type_Combobox.setObjectName("Type_Combobox")
        self.gridLayout_3.addWidget(self.Type_Combobox, 5, 3, 1, 2)
        self.AgeRating_Combobox = QtWidgets.QComboBox(self.centralwidget)
        self.AgeRating_Combobox.setObjectName("AgeRating_Combobox")
        self.gridLayout_3.addWidget(self.AgeRating_Combobox, 6, 3, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem13, 2, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 4, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem15, 3, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem16, 6, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem18, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 2, 1, 1)
        self.Estimation_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.Estimation_button.setFont(font)
        self.Estimation_button.setObjectName("Estimation_button")
        self.gridLayout_6.addWidget(self.Estimation_button, 6, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 6, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem20, 6, 3, 1, 1)
        self.Estimation_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        self.Estimation_label.setFont(font)
        self.Estimation_label.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";")
        self.Estimation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Estimation_label.setObjectName("Estimation_label")
        self.gridLayout_6.addWidget(self.Estimation_label, 1, 1, 4, 3)
        self.FullEstimation_label = QtWidgets.QLabel(self.centralwidget)
        self.FullEstimation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.FullEstimation_label.setObjectName("FullEstimation_label")
        self.gridLayout_6.addWidget(self.FullEstimation_label, 5, 1, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_6, 2, 5, 1, 2)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 6, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem22, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.Load_action = QtWidgets.QAction(MainWindow)
        self.Load_action.setObjectName("Load_action")
        self.Save_action = QtWidgets.QAction(MainWindow)
        self.Save_action.setObjectName("Save_action")
        self.menu.addAction(self.Load_action)
        self.menu.addAction(self.Save_action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Description_label.setText(_translate("MainWindow", "<html><head/><body><p>Описание</p></body></html>"))
        self.Genre_label.setText(_translate("MainWindow", "Жанры"))
        self.Studio_label.setText(_translate("MainWindow", "Студия"))
        self.MediaMark_main_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">MediaMark</span></p></body></html>"))
        self.Name_label.setText(_translate("MainWindow", "Название"))
        self.Date_label.setText(_translate("MainWindow", "Год выхода"))
        self.EpisodeCount_label.setText(_translate("MainWindow", "Количество эпизодов"))
        self.Type_Label.setText(_translate("MainWindow", "<html><head/><body><p>Тип медиаконтента</p></body></html>"))
        self.AgeRating_label.setText(_translate("MainWindow", "Возрастной рейтинг"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_2.setText(_translate("MainWindow", "Оценка"))
        self.Estimation_button.setText(_translate("MainWindow", "Оценить"))
        self.Estimation_label.setText(_translate("MainWindow", "0.00"))
        self.FullEstimation_label.setText(_translate("MainWindow", "0.00"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.Load_action.setText(_translate("MainWindow", "Загрузить"))
        self.Save_action.setText(_translate("MainWindow", "Сохранить как"))