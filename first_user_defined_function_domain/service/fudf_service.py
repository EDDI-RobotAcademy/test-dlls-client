from abc import ABC, abstractmethod


class FudfService(ABC):
    @abstractmethod
    def justForTest(self, *args, **kwargs):
        pass
