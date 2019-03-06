

from PyQt5 import QtCore,  QtWidgets


def list_init(self):
    self.Dialog.resize(265, 300)
    self.Dialog.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog)
    self.Dialog.verticalLayout.setObjectName("verticalLayout")
    self.Dialog.listWidget = QtWidgets.QListWidget(self.Dialog)
    self.Dialog.listWidget.setObjectName("listWidget")
    self.Dialog.horizontalLayout = QtWidgets.QHBoxLayout()
    self.Dialog.verticalLayout.addWidget(self.Dialog.listWidget)
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
    self.Dialog.listWidget.itemClicked.connect(self.item_clicked)
    self.Dialog.pushButton.setText("1")
    self.Dialog.pushButton_2.setText("2")