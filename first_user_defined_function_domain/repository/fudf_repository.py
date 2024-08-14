from abc import abstractmethod, ABC


class FudfRepository(ABC):
    @abstractmethod
    def justForTest(self, *args, **kwargs):
        pass
