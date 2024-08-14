from abc import abstractmethod, ABC

from first_user_defined_function_domain.repository.fudf_repository import FudfRepository


class FudfRepositoryImpl(FudfRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def justForTest(self, *args, **kwargs):
        sum = 0
        for index, argument in enumerate(args, 1):
            sum += argument

        list1 = [1, 2, 33, 4, 5]
        list2 = ['a', 'b', 'c']
        simpleIntValue = 77
        anotherStringValue = "example"

        return {
            "sum": sum,
            "list1": list1,
            "list2": list2,
            "simpleIntValue": simpleIntValue,
            "anotherStringValue": anotherStringValue
        }
    