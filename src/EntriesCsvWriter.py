import csv


class EntriesCsvWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, entries):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, restval='-', fieldnames=self.__get_fieldnames(entries), extrasaction='ignore')
            writer.writeheader()

            for entry in entries:
                writer.writerow(entry)

    def __get_fieldnames(self, entries):
        return entries[0].keys()