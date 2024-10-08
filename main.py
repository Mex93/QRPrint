import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

from ui.untitled import Ui_MainWindow
from common import send_message_box, SMBOX_ICON_TYPE, get_about_text, get_rules_text
from enuuuums import QR_TYPE, PAPER_TYPE
from components.CQR import QR
from components.CPrinter import CPrinter

# pyside6-uic .\ui\untitled.ui -o .\ui\untitled.py
# pyside6-rcc .\ui\res.qrc -o .\ui\res_rc.py
# Press the green button in the gutter to run the script.


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"  # Менять при каждом обновлении любой из подпрограмм

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Печать QR Kvant 2024 v0.1')

        self.ui.pushButton_set_print.clicked.connect(self.on_user_set_print)
        self.ui.pushButton_qr.clicked.connect(lambda: self.user_changed_code_type(QR_TYPE.QR_CUB))
        self.ui.pushButton_code_no_text.clicked.connect(lambda: self.user_changed_code_type(QR_TYPE.QR_CODE_NO_TEXT))
        self.ui.pushButton_code_with_text.clicked.connect(
            lambda: self.user_changed_code_type(QR_TYPE.QR_CODE_WITH_TEXT))
        self.ui.action_info.triggered.connect(self.on_user_pressed_info)

        self.cpaper = PaperType()
        QR.set_main_window(self.ui)
        QR.set_all_flat()

        # comboBox_change_printer_2
        self.cprinter = CPrinter()
        printers = self.cprinter.get_printers()
        if printers is not None:
            unit = self.ui.comboBox_change_printer
            unit.clear()
            for index, printer in enumerate(printers, 0):
                unit.addItem(printer)

            unit.setCurrentIndex(-1)
            unit.currentIndexChanged.connect(self.on_user_changed_printer)

        # для бумаги
        unit = self.ui.comboBox_change_printer_2
        unit.clear()
        paper_names = ["58x20", "48x8.5"]
        for index, paper_name in enumerate(paper_names, 0):
            unit.addItem(paper_name)

        unit.setCurrentIndex(-1)
        unit.currentIndexChanged.connect(self.on_user_changed_paper)

        self.ui.lineEdit_input_text.returnPressed.connect(self.on_user_now_print)
        self.ui.lineEdit_input_text.setEnabled(False)

    def is_clear_field(self) -> bool:
        return self.ui.checkBox_is_clear.isChecked()

    def is_printing_now(self) -> bool:
        return self.ui.checkBox_is_printing_now.isChecked()

    def on_user_now_print(self):
        if self.is_printing_now():
            self.on_user_set_print()

    @staticmethod
    def on_user_pressed_info():
        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                         text=f"{get_about_text()}"
                              f"\n"
                              f"\n"
                              f"{get_rules_text()}",
                         title="О программе",
                         variant_yes="Закрыть", variant_no="")

    def on_user_changed_paper(self):
        text = self.ui.comboBox_change_printer_2.currentText()
        if text == "58x20":
            self.cpaper.set_paper_type(PAPER_TYPE.PAPER_BIG)
        elif text == "48x8.5":
            self.cpaper.set_paper_type(PAPER_TYPE.PAPER_SMALL)
        else:
            self.cpaper.set_paper_type(PAPER_TYPE.PAPER_NONE)

    def on_user_changed_printer(self):
        text = self.ui.comboBox_change_printer.currentText()
        if text:
            self.cprinter.set_printer_name(text)

    def on_user_set_print(self):
        if not self.cprinter.get_current_printer_name():
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Принтер не выбран!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return
        if self.cpaper.get_paper_type() == PAPER_TYPE.PAPER_NONE:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Тип бумаги не выбран!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return

        current_qr = QR.get_qr_type()
        if current_qr == QR_TYPE.QR_NONE:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Тип QR кода не выбран!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return

        input_text = self.ui.lineEdit_input_text.text()
        if not input_text:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Пустой текст!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return

        input_text = input_text.upper().replace(" ", "")
        if not self.cprinter.send_print_label(input_text, current_qr, self.cpaper.get_paper_type()):
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Ошибка печати!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return
        if self.is_clear_field():
            self.ui.lineEdit_input_text.clear()


    def user_changed_code_type(self, qr_type: QR_TYPE):
        QR.set_switch(qr_type)
        qr = QR.get_qr_type()
        self.ui.lineEdit_input_text.clear()
        if qr == QR_TYPE.QR_NONE:
            self.ui.lineEdit_input_text.setEnabled(False)
        else:
            self.ui.lineEdit_input_text.setEnabled(True)
            max_len = self.cprinter.get_max_text_len(qr)
            self.ui.lineEdit_input_text.setMaxLength(max_len)


class PaperType:
    def __init__(self):
        self._paper_type = PAPER_TYPE.PAPER_NONE

    def set_paper_type(self, paper_type: PAPER_TYPE):
        self._paper_type = paper_type

    def get_paper_type(self) -> PAPER_TYPE:
        return self._paper_type



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
