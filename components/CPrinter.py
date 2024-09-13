import clr
import sys

import win32print
import win32ui
class CPrinter:
    def __init__(self):
        self.__printer_name = None
        # Добавьте путь к вашей DLL
        sys.path.append(r'../LabelPrinterLibrary.dll')
        # Загрузите вашу DLL:
        clr.AddReference('LabelPrinterLibrary')

        self.standart_ezpl = "\
                ^Q8,3\n\
                ^W48\n\
                ^H10\n\
                ^P1\n\
                ^S2\n\
                ^AT\n\
                ^C1\n\
                ^R0\n\
                ~Q+0\n\
                ^O0\n\
                ^D0\n\
                ^E18\n\
                ~R255\n\
                ^L\n\
                Dy2-me-dd\n\
                Th:m:s\n\
                Y37,153,Image3-97\n\
                Y37,153,Image2-72\n\
                Y33,10,WindowText1-17\n\
                BQ,92,8,2,5,20,0,3,THIS_TEST\n\
                E\n\n"
        self.standart_ezpl = self.standart_ezpl.replace(" ", "")

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


    def send_print_label(self, tricolor_key: str) -> bool:
        if not self.__printer_name:
            return False

        if len(tricolor_key) > 0:

            with open('../barcode_template.txt', 'w+') as file:
                ezpl_data = file.read()
                if not len(ezpl_data):
                    file.write(self.standart_ezpl)
                    ezpl_data = self.standart_ezpl
                ezpl_data = ezpl_data.replace("THIS_TEST", tricolor_key)

            # нельзя впереди этикетки что бы были пробелы!!!!!!
            # в документе должен быть пробел в самом конце после E

            self.__print_label(ezpl_data)
            return True
