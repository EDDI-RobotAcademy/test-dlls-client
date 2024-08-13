import os
import sys

from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from template.custom_protocol.service.custom_protocol_service_impl import CustomProtocolServiceImpl
from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:
    @staticmethod
    def registerUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        # 디폴트 프로토콜 등록을 여기서 했음
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest
        )
