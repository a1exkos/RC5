# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_RC5(object):
    def setupUi(self, RC5):
        if not RC5.objectName():
            RC5.setObjectName(u"RC5")
        RC5.setWindowModality(Qt.NonModal)
        RC5.resize(639, 397)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RC5.sizePolicy().hasHeightForWidth())
        RC5.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/encryption.ico", QSize(), QIcon.Normal, QIcon.Off)
        RC5.setWindowIcon(icon)
        self.gridLayout = QGridLayout(RC5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.label_6 = QLabel(RC5)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setPixmap(QPixmap(u":/images/rc5.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)

        self.label = QLabel(RC5)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(RC5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(RC5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(RC5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(RC5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(RC5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/enc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(RC5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setFont(font1)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(38, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(RC5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.radioButton = QRadioButton(RC5)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(RC5)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(RC5)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.label_5 = QLabel(RC5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.spinBox = QSpinBox(RC5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(45, 0))
        self.spinBox.setFont(font1)
        self.spinBox.setReadOnly(False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(RC5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_3, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(RC5)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(RC5)
    # setupUi

    def retranslateUi(self, RC5):
        RC5.setWindowTitle(QCoreApplication.translate("RC5", u"RC5 by Alexander Kostynchuk AI-173", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("RC5", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442:", None))
        self.label_2.setText(QCoreApplication.translate("RC5", u"\u041a\u043b\u044e\u0447 (0-2040 \u0431\u0438\u0442):", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("RC5", u"\u0412\u0432\u043e\u0434", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("RC5", u"\u0412\u0432\u043e\u0434", None))
        self.label_3.setText(QCoreApplication.translate("RC5", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 (16 \u0441\u0441):", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("RC5", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435 / \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("RC5", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("RC5", u"\u0414\u043b\u0438\u043d\u0430 \u0431\u043b\u043e\u043a\u0430 \u0432 \u0431\u0438\u0442\u0430\u0445:", None))
        self.radioButton.setText(QCoreApplication.translate("RC5", u"32", None))
        self.radioButton_2.setText(QCoreApplication.translate("RC5", u"64", None))
        self.radioButton_3.setText(QCoreApplication.translate("RC5", u"128", None))
        self.label_5.setText(QCoreApplication.translate("RC5", u"\u0427\u0438\u0441\u043b\u043e \u0440\u0430\u0443\u043d\u0434\u043e\u0432 (1-255):", None))
    # retranslateUi

