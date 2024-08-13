from enum import Enum


class UserDefinedProtocolNumber(Enum):
    # 예약된 정보 (1, 2, 11, 12, 13, 21) 을 제외하고 사용하도록 함
    FIRST_USER_DEFINED_FUNCTION_FOR_TEST = 5

    @classmethod
    def hasValue(cls, value):
        return any(value == item.value for item in cls)
