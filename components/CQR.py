from enuuuums import QR_TYPE
from ui.untitled import Ui_MainWindow


class QR:
    main: Ui_MainWindow = None

    current_selected_type: QR_TYPE = QR_TYPE.QR_NONE

    @classmethod
    def set_main_window(cls, mw):
        cls.main = mw

    @classmethod
    def get_main_window(cls) -> Ui_MainWindow:
        return cls.main

    @classmethod
    def set_current_type(cls, qr_type: QR_TYPE):
        cls.current_selected_type = qr_type

    @classmethod
    def get_qr_type(cls) -> QR_TYPE:
        return cls.current_selected_type

    @classmethod
    def set_switch(cls, new_qr_type: QR_TYPE):
        old_qr = cls.get_qr_type()
        if old_qr == new_qr_type:
            cls.set_visual_effect_for_btn(old_qr, True)
            new_qr_type = QR_TYPE.QR_NONE
        else:
            cls.set_visual_effect_for_btn(old_qr, True)
            cls.set_visual_effect_for_btn(new_qr_type, False)

        cls.set_current_type(new_qr_type)

    @classmethod
    def set_all_flat(cls):
        for item in QR_TYPE:
            cls.set_visual_effect_for_btn(item, True)

    @classmethod
    def set_visual_effect_for_btn(cls, qr_type: QR_TYPE, status: bool):
        main_window = cls.get_main_window()
        match qr_type:
            case QR_TYPE.QR_CUB:
                main_window.pushButton_qr.setFlat(status)
            case QR_TYPE.QR_CODE_NO_TEXT:
                main_window.pushButton_code_no_text.setFlat(status)
            case QR_TYPE.QR_CODE_WITH_TEXT:
                main_window.pushButton_code_with_text.setFlat(status)

