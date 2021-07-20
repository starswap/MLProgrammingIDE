# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setStyleSheet("background-color:rgb(115, 210, 22);")
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 0, 0, 1, 1)
        self.runCommandBox = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.runCommandBox.setFont(font)
        self.runCommandBox.setText("")
        self.runCommandBox.setObjectName("runCommandBox")
        self.gridLayout.addWidget(self.runCommandBox, 0, 2, 1, 2)
        self.outputWindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.outputWindow.setFont(font)
        self.outputWindow.setStyleSheet("background-color:black;color:white;")
        self.outputWindow.setReadOnly(True)
        self.outputWindow.setPlainText("Code output is displayed here.")
        self.outputWindow.setPlaceholderText("")
        self.outputWindow.setObjectName("outputWindow")
        self.gridLayout.addWidget(self.outputWindow, 4, 1, 1, 3)
        self.shellInputBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.shellInputBox.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.shellInputBox.setFont(font)
        self.shellInputBox.setStyleSheet("background-color: rgb(46, 52, 54); color: rgb(255, 255, 255)")
        self.shellInputBox.setPlainText("")
        self.shellInputBox.setObjectName("shellInputBox")
        self.gridLayout.addWidget(self.shellInputBox, 3, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EfficacyHexagon = Hexagon(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EfficacyHexagon.sizePolicy().hasHeightForWidth())
        self.EfficacyHexagon.setSizePolicy(sizePolicy)
        self.EfficacyHexagon.setMinimumSize(QtCore.QSize(150, 0))
        self.EfficacyHexagon.setObjectName("EfficacyHexagon")
        self.verticalLayout.addWidget(self.EfficacyHexagon)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(150, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.EfficiencyHexagon = Hexagon(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EfficiencyHexagon.sizePolicy().hasHeightForWidth())
        self.EfficiencyHexagon.setSizePolicy(sizePolicy)
        self.EfficiencyHexagon.setMinimumSize(QtCore.QSize(150, 0))
        self.EfficiencyHexagon.setObjectName("EfficiencyHexagon")
        self.verticalLayout.addWidget(self.EfficiencyHexagon)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(150, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.EleganceHexagon = Hexagon(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EleganceHexagon.sizePolicy().hasHeightForWidth())
        self.EleganceHexagon.setSizePolicy(sizePolicy)
        self.EleganceHexagon.setMinimumSize(QtCore.QSize(150, 0))
        self.EleganceHexagon.setObjectName("EleganceHexagon")
        self.verticalLayout.addWidget(self.EleganceHexagon)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(150, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.ReadabilityHexagon = Hexagon(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReadabilityHexagon.sizePolicy().hasHeightForWidth())
        self.ReadabilityHexagon.setSizePolicy(sizePolicy)
        self.ReadabilityHexagon.setMinimumSize(QtCore.QSize(150, 0))
        self.ReadabilityHexagon.setObjectName("ReadabilityHexagon")
        self.line_5 = QtWidgets.QFrame(self.ReadabilityHexagon)
        self.line_5.setGeometry(QtCore.QRect(0, 0, 3, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.ReadabilityHexagon)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QtCore.QSize(150, 0))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(6, 5)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(9, 5)
        self.verticalLayout.setStretch(10, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 5, 1)
        self.listOfFilesMenu = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.listOfFilesMenu.sizePolicy().hasHeightForWidth())
        self.listOfFilesMenu.setSizePolicy(sizePolicy)
        self.listOfFilesMenu.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listOfFilesMenu.setTextElideMode(QtCore.Qt.ElideNone)
        self.listOfFilesMenu.setProperty("isWrapping", False)
        self.listOfFilesMenu.setObjectName("listOfFilesMenu")
        self.gridLayout.addWidget(self.listOfFilesMenu, 1, 0, 4, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.appendNewline = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.appendNewline.setFont(font)
        self.appendNewline.setChecked(True)
        self.appendNewline.setObjectName("appendNewline")
        self.gridLayout_2.addWidget(self.appendNewline, 2, 0, 1, 1)
        self.inputButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.inputButton.setStyleSheet("background-color: rgb(252, 233, 79)")
        self.inputButton.setObjectName("inputButton")
        self.gridLayout_2.addWidget(self.inputButton, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 3, 1, 1)
        self.activeFileTextbox = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.activeFileTextbox.sizePolicy().hasHeightForWidth())
        self.activeFileTextbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.activeFileTextbox.setFont(font)
        self.activeFileTextbox.setStyleSheet("")
        self.activeFileTextbox.setTabStopWidth(40)
        self.activeFileTextbox.setAcceptRichText(False)
        self.activeFileTextbox.setObjectName("activeFileTextbox")
        self.gridLayout.addWidget(self.activeFileTextbox, 1, 2, 2, 1)
        self.lineNumberArea_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.lineNumberArea_2.sizePolicy().hasHeightForWidth())
        self.lineNumberArea_2.setSizePolicy(sizePolicy)
        self.lineNumberArea_2.setStyleSheet("background-color:rgb(211, 215, 207)")
        self.lineNumberArea_2.setObjectName("lineNumberArea_2")
        self.gridLayout.addWidget(self.lineNumberArea_2, 1, 1, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 3, 2, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 45)
        self.gridLayout.setColumnStretch(3, 20)
        self.gridLayout.setColumnStretch(4, 20)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuUnit_Tests = QtWidgets.QMenu(self.menubar)
        self.menuUnit_Tests.setObjectName("menuUnit_Tests")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionAdd_File_to_Project = QtWidgets.QAction(MainWindow)
        self.actionAdd_File_to_Project.setObjectName("actionAdd_File_to_Project")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind_Replace = QtWidgets.QAction(MainWindow)
        self.actionFind_Replace.setObjectName("actionFind_Replace")
        self.actionFormat_Code = QtWidgets.QAction(MainWindow)
        self.actionFormat_Code.setObjectName("actionFormat_Code")
        self.actionExecute_Project = QtWidgets.QAction(MainWindow)
        self.actionExecute_Project.setObjectName("actionExecute_Project")
        self.actionEnter_Unit_Tests = QtWidgets.QAction(MainWindow)
        self.actionEnter_Unit_Tests.setObjectName("actionEnter_Unit_Tests")
        self.actionDisplay_Test_Results = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Test_Results.setObjectName("actionDisplay_Test_Results")
        self.actionShow_Tutorial = QtWidgets.QAction(MainWindow)
        self.actionShow_Tutorial.setObjectName("actionShow_Tutorial")
        self.actionClose_IDE = QtWidgets.QAction(MainWindow)
        self.actionClose_IDE.setObjectName("actionClose_IDE")
        self.actionOpen_Settings = QtWidgets.QAction(MainWindow)
        self.actionOpen_Settings.setObjectName("actionOpen_Settings")
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionAdd_File_to_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_IDE)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionFind_Replace)
        self.menuEdit.addAction(self.actionFormat_Code)
        self.menuRun.addAction(self.actionExecute_Project)
        self.menuUnit_Tests.addAction(self.actionEnter_Unit_Tests)
        self.menuUnit_Tests.addAction(self.actionDisplay_Test_Results)
        self.menuHelp.addAction(self.actionShow_Tutorial)
        self.menuPreferences.addAction(self.actionOpen_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuUnit_Tests.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Programming IDE"))
        self.runButton.setText(_translate("MainWindow", "Run Program"))
        self.runCommandBox.setPlaceholderText(_translate("MainWindow", "Type the command to be run when your program is executed"))
        self.shellInputBox.setPlaceholderText(_translate("MainWindow", "Type input to the program here and press send. Works when program running."))
        self.EfficacyHexagon.setProperty("hexColor", _translate("MainWindow", "#00FF00"))
        self.EfficacyHexagon.setProperty("mainColor", _translate("MainWindow", "#00FF00"))
        self.label.setText(_translate("MainWindow", "Efficacy"))
        self.EfficiencyHexagon.setProperty("hexColor", _translate("MainWindow", "#0000FF"))
        self.EfficiencyHexagon.setProperty("mainColor", _translate("MainWindow", "#0000FF"))
        self.label_2.setText(_translate("MainWindow", "Efficiency"))
        self.EleganceHexagon.setProperty("hexColor", _translate("MainWindow", "#f542ad"))
        self.EleganceHexagon.setProperty("mainColor", _translate("MainWindow", "#f542ad"))
        self.label_3.setText(_translate("MainWindow", "Elegance"))
        self.ReadabilityHexagon.setProperty("hexColor", _translate("MainWindow", "#FF0000"))
        self.ReadabilityHexagon.setProperty("mainColor", _translate("MainWindow", "#FF0000"))
        self.label_4.setText(_translate("MainWindow", "Readability"))
        self.appendNewline.setText(_translate("MainWindow", "Append enter"))
        self.inputButton.setText(_translate("MainWindow", "Send Input"))
        self.activeFileTextbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.activeFileTextbox.setPlaceholderText(_translate("MainWindow", "Type your code here"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is where the AI\'s comments will go</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Dismiss Suggestion"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Second AI suggestion etc.    </p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Dismiss Suggestion"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuUnit_Tests.setTitle(_translate("MainWindow", "Unit Tests"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionOpen_Project.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionSave_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_Project.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionNew_File.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAdd_File_to_Project.setText(_translate("MainWindow", "Add File to Project"))
        self.actionAdd_File_to_Project.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionFind_Replace.setText(_translate("MainWindow", "Find/Replace"))
        self.actionFind_Replace.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionFormat_Code.setText(_translate("MainWindow", "Format Code"))
        self.actionFormat_Code.setShortcut(_translate("MainWindow", "F6"))
        self.actionExecute_Project.setText(_translate("MainWindow", "Execute Project"))
        self.actionExecute_Project.setShortcut(_translate("MainWindow", "F5"))
        self.actionEnter_Unit_Tests.setText(_translate("MainWindow", "Enter Unit Tests"))
        self.actionEnter_Unit_Tests.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionDisplay_Test_Results.setText(_translate("MainWindow", "Display Test Results"))
        self.actionDisplay_Test_Results.setShortcut(_translate("MainWindow", "Ctrl+F5"))
        self.actionShow_Tutorial.setText(_translate("MainWindow", "Show Tutorial"))
        self.actionShow_Tutorial.setShortcut(_translate("MainWindow", "F12"))
        self.actionClose_IDE.setText(_translate("MainWindow", "Close IDE"))
        self.actionClose_IDE.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionOpen_Settings.setText(_translate("MainWindow", "Open Settings"))
        self.actionOpen_Settings.setShortcut(_translate("MainWindow", "F11"))
from Objects.HexagonObject import Hexagon
