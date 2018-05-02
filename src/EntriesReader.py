import xmltodict


class EntriesReader():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file(self):
        with open(self.file_name) as fd:
            return xmltodict.parse(fd.read())