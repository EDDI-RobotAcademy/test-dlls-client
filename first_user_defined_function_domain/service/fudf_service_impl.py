from first_user_defined_function_domain.repository.fudf_repository_impl import FudfRepositoryImpl
from first_user_defined_function_domain.service.fudf_service import FudfService


class FudfServiceImpl(FudfService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__fudfRepository = FudfRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def justForTest(self, *args, **kwargs):
        return self.__fudfRepository.justForTest(*args, **kwargs)
    