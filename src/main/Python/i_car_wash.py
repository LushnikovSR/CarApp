from abc import ABC, abstractmethod


class ICarWash(ABC):
    @abstractmethod
    def wip_windshield(self):
        pass

    @abstractmethod
    def wip_headlights(self):
        pass

    @abstractmethod
    def wip_mirrors(self):
        pass
