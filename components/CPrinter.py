import clr
import sys
import os
import win32print

from enuuuums import QR_TYPE


class CPrinter:
    def __init__(self):
        self.__printer_name = None
        # Добавьте путь к вашей DLL
        sys.path.append(r'../LabelPrinterLibrary.dll')
        # Загрузите вашу DLL:
        clr.AddReference('LabelPrinterLibrary')
        self.__folder_name = "barcode_templates"

    @classmethod
    def get_max_text_len(cls, qr_type: QR_TYPE) -> int:
        match qr_type:
            case QR_TYPE.QR_CUB:
                return 57
            case QR_TYPE.QR_CODE_NO_TEXT:
                return 19
            case QR_TYPE.QR_CODE_WITH_TEXT:
                return 19

    def set_printer_name(self, pr_name: str):
        self.__printer_name = pr_name

    def get_current_printer_name(self) -> str | None:
        return self.__printer_name

    def __print_label(self, barcode_text):
        from LabelPrinterLibrary import LabelPrinter
        result = LabelPrinter.PrintBarcode(self.__printer_name, barcode_text)
        return result

    @classmethod
    def get_printers(cls) -> list | None:
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        printer_cleared_data_list = list()
        for printer in printers:
            target_printer = printer[2]
            if isinstance(target_printer, str):
                if len(target_printer) > 0:
                    if (target_printer.find("Microsoft") != -1 or
                            target_printer.find("AnyDesk") != -1 or
                            target_printer.find("Adobe") != -1 or
                            target_printer.find("Fax") != -1):
                        continue

                    printer_cleared_data_list.append(target_printer)
        if len(printer_cleared_data_list) > 0:
            return printer_cleared_data_list

    def get_barcode_file_name(self, qr_type: QR_TYPE) -> str | None:
        match qr_type:
            case QR_TYPE.QR_CUB:
                return "barcode_template_qr"
            case QR_TYPE.QR_CODE_NO_TEXT:
                return "barcode_template_no_text"
            case QR_TYPE.QR_CODE_WITH_TEXT:
                return "barcode_template_with_text"

    def send_print_label(self, text: str, qr_type: QR_TYPE) -> bool:
        if not self.get_current_printer_name():
            return False
        print(1)
        if len(text) > 0:
            if os.path.exists(self.__folder_name):
                current_file = self.get_barcode_file_name(qr_type)
                if current_file:
                    with open(f'{self.__folder_name}/{current_file}.txt', 'r') as file:
                        ezpl_data = file.read()
                        if len(ezpl_data):
                            match qr_type:
                                case QR_TYPE.QR_CUB:
                                    ezpl_data = ezpl_data.replace("REPLACE_TEXT", text)
                                    ezpl_data = ezpl_data.replace("REPLACE_COUNT", str(len(text)))
                                    print(ezpl_data)
                                case QR_TYPE.QR_CODE_NO_TEXT:
                                    ezpl_data = ezpl_data.replace("REPLACE_TEXT", text)
                                case QR_TYPE.QR_CODE_WITH_TEXT:
                                    ezpl_data = ezpl_data.replace("REPLACE_TEXT", text)
                                case _:
                                    return False

                            self.__print_label(ezpl_data)
                            return True
                # нельзя впереди этикетки что бы были пробелы!!!!!!
                # в документе должен быть пробел в самом конце после E


        return False
