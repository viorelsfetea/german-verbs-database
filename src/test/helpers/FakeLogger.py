from ILogger import ILogger


class FakeLogger(ILogger):
    def __init__(self):
        pass

    def info(self, *args):
        print('>>>>>> INFO', args)

    def warning(self, *args):
        print('>>>>>> WARNING', args)

    def error(self, *args):
        print('>>>>>> ERROR', args)
