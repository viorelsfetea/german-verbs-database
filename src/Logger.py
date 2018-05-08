from ILogger import ILogger
import logging


class Logger(ILogger):
    def __init__(self):
        self.logger = logging.getLogger('app')

    def info(self, *args):
        self.logger.info(args)

    def warning(self, *args):
        self.logger.warning(args)

    def error(self, *args):
        self.logger.error(args)
