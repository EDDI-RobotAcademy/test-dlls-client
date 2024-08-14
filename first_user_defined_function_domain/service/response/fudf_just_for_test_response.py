from user_defined_protocol.protocol import UserDefinedProtocolNumber


class FudfJustForTestResponse:
    def __init__(self, responseData):
        self.protocolNumber = UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"FudfJustForTestResponse({self.__dict__})"