import csv


class EntriesCsvWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, entries):
        total_rows = 0

        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, restval='-', fieldnames=self.__get_fieldnames(entries), extrasaction='ignore')
            writer.writeheader()

            for entry in entries:
                writer.writerow(entry)
                total_rows += 1

        return total_rows

    def __get_fieldnames(self, entries):
        return entries[0].keys()