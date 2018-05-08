import abc


class ILogger(abc.ABC):
    @abc.abstractmethod
    def info(self, **args):
        pass

    @abc.abstractmethod
    def warning(self, **args):
        pass

    @abc.abstractmethod
    def error(self, **args):
        pass
