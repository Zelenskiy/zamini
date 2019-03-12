

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel


def list_init(self, model):
    self.Dialog.resize(218, 550)
    self.Dialog.centralwidget = QtWidgets.QWidget(self.Dialog)
    self.Dialog.centralwidget.setObjectName("centralwidget")
    self.Dialog.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog.centralwidget)
    self.Dialog.verticalLayout.setObjectName("verticalLayout")
    self.Dialog.comboBox = QtWidgets.QComboBox(self.Dialog.centralwidget)
    self.Dialog.comboBox.setObjectName("comboBox")
    self.Dialog.verticalLayout.addWidget(self.Dialog.comboBox)
    self.Dialog.listView = QtWidgets.QListView(self.Dialog.centralwidget)
    self.Dialog.listView.setObjectName("listView")
    self.Dialog.verticalLayout.addWidget(self.Dialog.listView)
    self.Dialog.horizontalLayout = QtWidgets.QHBoxLayout()
    self.Dialog.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.Dialog.horizontalLayout.addItem(spacerItem)
    self.Dialog.pushButton = QtWidgets.QPushButton(self.Dialog.centralwidget)
    self.Dialog.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
    self.Dialog.pushButton.setObjectName("pushButton")
    self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton)
    self.Dialog.pushButton_2 = QtWidgets.QPushButton(self.Dialog.centralwidget)
    self.Dialog.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
    self.Dialog.pushButton_2.setObjectName("pushButton_2")
    self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton_2)
    self.Dialog.verticalLayout.addLayout(self.Dialog.horizontalLayout)
    # self.Dialog.setCentralWidget(self.Dialog.centralwidget)
    self.Dialog.menubar = QtWidgets.QMenuBar(self.Dialog)
    self.Dialog.menubar.setGeometry(QtCore.QRect(0, 0, 218, 21))
    self.Dialog.menubar.setObjectName("menubar")
    #self.Dialog.setMenuBar(self.Dialog.menubar)
    #self.Dialog.statusbar = QtWidgets.QStatusBar(self.Dialog)
    #self.Dialog.statusbar.setObjectName("statusbar")
    #self.Dialog.setStatusBar(self.Dialog.statusbar)
    """
    self.Dialog.resize(265, 300)
    self.Dialog.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog)
    self.Dialog.verticalLayout.setObjectName("verticalLayout")
    self.Dialog.listView = QtWidgets.QListView(self.Dialog)
    self.Dialog.listView.setObjectName("listView")

    self.Dialog.comboBox = QtWidgets.QComboBox(self.Dialog)
    # self.Dialog.comboBox.setGeometry(QtCore.QRect(60, 50, 181, 22))
    self.Dialog.comboBox.setObjectName("comboBox")


    self.Dialog.horizontalLayout = QtWidgets.QHBoxLayout()
    self.Dialog.verticalLayout.addWidget(self.Dialog.listView)
    self.Dialog.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.Dialog.horizontalLayout.addItem(spacerItem)
    self.Dialog.pushButton = QtWidgets.QPushButton(self.Dialog)
    self.Dialog.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
    self.Dialog.pushButton.setObjectName("pushButton")
    self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton)
    self.Dialog.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
    self.Dialog.pushButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
    self.Dialog.pushButton_2.setObjectName("pushButton_2")
    self.Dialog.horizontalLayout.addWidget(self.Dialog.pushButton_2)
    self.Dialog.verticalLayout.addLayout(self.Dialog.horizontalLayout)

    self.Dialog.pushButton.setText("1")
    self.Dialog.pushButton_2.setText("2")
    """
