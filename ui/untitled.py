# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 352)
        MainWindow.setMinimumSize(QSize(719, 297))
        icon = QIcon()
        icon.addFile(u":/res/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(30, 30))
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_change_printer = QComboBox(self.groupBox)
        self.comboBox_change_printer.addItem("")
        self.comboBox_change_printer.setObjectName(u"comboBox_change_printer")

        self.verticalLayout.addWidget(self.comboBox_change_printer)

        self.comboBox_change_printer_2 = QComboBox(self.groupBox)
        self.comboBox_change_printer_2.addItem("")
        self.comboBox_change_printer_2.setObjectName(u"comboBox_change_printer_2")

        self.verticalLayout.addWidget(self.comboBox_change_printer_2)

        self.checkBox_is_printing_now = QCheckBox(self.groupBox)
        self.checkBox_is_printing_now.setObjectName(u"checkBox_is_printing_now")

        self.verticalLayout.addWidget(self.checkBox_is_printing_now)

        self.checkBox_is_clear = QCheckBox(self.groupBox)
        self.checkBox_is_clear.setObjectName(u"checkBox_is_clear")

        self.verticalLayout.addWidget(self.checkBox_is_clear)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lineEdit_input_text = QLineEdit(self.centralwidget)
        self.lineEdit_input_text.setObjectName(u"lineEdit_input_text")
        self.lineEdit_input_text.setMinimumSize(QSize(400, 71))
        self.lineEdit_input_text.setMaximumSize(QSize(0, 71))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_input_text.setFont(font1)
        self.lineEdit_input_text.setInputMethodHints(Qt.InputMethodHint.ImhUppercaseOnly)
        self.lineEdit_input_text.setMaxLength(64)
        self.lineEdit_input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_input_text)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.pushButton_set_print = QPushButton(self.centralwidget)
        self.pushButton_set_print.setObjectName(u"pushButton_set_print")
        icon1 = QIcon()
        icon1.addFile(u":/res/images/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_set_print.setIcon(icon1)
        self.pushButton_set_print.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButton_set_print)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_qr = QPushButton(self.centralwidget)
        self.pushButton_qr.setObjectName(u"pushButton_qr")
        self.pushButton_qr.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/res/images/qr1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_qr.setIcon(icon2)
        self.pushButton_qr.setIconSize(QSize(120, 120))
        self.pushButton_qr.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_qr)

        self.pushButton_code_no_text = QPushButton(self.centralwidget)
        self.pushButton_code_no_text.setObjectName(u"pushButton_code_no_text")
        icon3 = QIcon()
        icon3.addFile(u":/res/images/scancode1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_code_no_text.setIcon(icon3)
        self.pushButton_code_no_text.setIconSize(QSize(120, 120))
        self.pushButton_code_no_text.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_code_no_text)

        self.pushButton_code_with_text = QPushButton(self.centralwidget)
        self.pushButton_code_with_text.setObjectName(u"pushButton_code_with_text")
        icon4 = QIcon()
        icon4.addFile(u":/res/images/scancode1 with text.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_code_with_text.setIcon(icon4)
        self.pushButton_code_with_text.setIconSize(QSize(120, 120))
        self.pushButton_code_with_text.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_code_with_text)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 22))
        self.menu_info = QMenu(self.menubar)
        self.menu_info.setObjectName(u"menu_info")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_info.menuAction())
        self.menu_info.addAction(self.action_info)

        self.retranslateUi(MainWindow)

        self.pushButton_qr.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0438\u043d\u0442\u0435\u0440 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440 \u0431\u0443\u043c\u0430\u0433\u0438:", None))
        self.comboBox_change_printer.setItemText(0, QCoreApplication.translate("MainWindow", u"godex", None))

        self.comboBox_change_printer.setCurrentText(QCoreApplication.translate("MainWindow", u"godex", None))
        self.comboBox_change_printer.setPlaceholderText("")
        self.comboBox_change_printer_2.setItemText(0, QCoreApplication.translate("MainWindow", u"58x20", None))

        self.comboBox_change_printer_2.setCurrentText(QCoreApplication.translate("MainWindow", u"58x20", None))
        self.comboBox_change_printer_2.setPlaceholderText("")
        self.checkBox_is_printing_now.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0441\u0440\u0430\u0437\u0443 \u043f\u0440\u0438 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u043a\u0435", None))
        self.checkBox_is_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0449\u0430\u0442\u044c \u043f\u043e\u043b\u0435 \u043f\u043e\u0441\u043b\u0435 \u043a\u0430\u0436\u0434\u043e\u0439 \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.lineEdit_input_text.setText("")
        self.lineEdit_input_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438:", None))
        self.pushButton_set_print.setText("")
        self.pushButton_qr.setText("")
        self.pushButton_code_no_text.setText("")
        self.pushButton_code_with_text.setText("")
        self.menu_info.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
    # retranslateUi

