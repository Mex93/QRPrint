from enum import IntEnum, auto


class SMBOX_ICON_TYPE(IntEnum):
    ICON_NONE = auto(),
    ICON_WARNING = auto(),
    ICON_ERROR = auto(),
    ICON_INFO = auto()


class QR_TYPE(IntEnum):
    QR_NONE = auto(),
    QR_CUB = auto(),
    QR_CODE_WITH_TEXT = auto(),
    QR_CODE_NO_TEXT = auto(),

class PAPER_TYPE(IntEnum):
    PAPER_NONE = auto(),
    PAPER_SMALL = auto(),
    PAPER_BIG = auto(),
