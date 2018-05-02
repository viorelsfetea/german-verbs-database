import abc


class IConfig(abc.ABC):
    @abc.abstractmethod
    def get_config(self):
        pass