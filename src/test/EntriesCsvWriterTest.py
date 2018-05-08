import os
import csv
import unittest

from EntriesCsvWriter import EntriesCsvWriter


class EntriesCsvWriterTest(unittest.TestCase):
    test_output_file = 'test_output/test.csv'
    maxDiff = None

    def tearDown(self):
        try:
            os.remove(self.test_output_file)
        except OSError:
            pass

    def test_write_one_entry(self):
        test_entry = {'Infinitive': 'lieben', 'Präsens_ich': 'liebe', 'Präsens_du': 'liebst', 'Präsens_er, sie, es': 'liebt',
             'Präteritum_ich': 'liebte', 'Partizip II': 'geliebt', 'Konjunktiv II_ich': 'liebte',
             'Imperativ Singular': 'liebe', 'Imperativ Plural': 'liebt', 'Hilfsverb': 'haben'}

        writer = EntriesCsvWriter(self.test_output_file)

        writer.write([test_entry])

        written_info = self.__get_written_csv_file()

        self.assertEqual(
            ['Infinitive', 'Präsens_ich', 'Präsens_du', 'Präsens_er, sie, es', 'Präteritum_ich', 'Partizip II',
             'Konjunktiv II_ich', 'Imperativ Singular', 'Imperativ Plural', 'Hilfsverb'],
            written_info['fieldnames']
        )

        self.assertDictEqual(test_entry, written_info['rows'][0])

    def test_write_two_entries(self):
        test_entries = [
            {'Infinitive': 'lieben', 'Präsens_ich': 'liebe', 'Präsens_du': 'liebst', 'Präsens_er, sie, es': 'liebt',
             'Präteritum_ich': 'liebte', 'Partizip II': 'geliebt', 'Konjunktiv II_ich': 'liebte',
             'Imperativ Singular': 'liebe', 'Imperativ Plural': 'liebt', 'Hilfsverb': 'haben'},
            {'Infinitive': 'klieben', 'Präsens_ich': 'kliebe', 'Präsens_du': 'kliebst', 'Präsens_er, sie, es': 'kliebt',
             'Präteritum_ich': 'klob', 'Partizip II': 'gekloben', 'Konjunktiv II_ich': 'klöbe',
             'Imperativ Singular': 'kliebe', 'Imperativ Plural': 'kliebt', 'Hilfsverb': 'haben'}
        ]

        writer = EntriesCsvWriter(self.test_output_file)

        writer.write(test_entries)

        written_info = self.__get_written_csv_file()

        self.assertEqual(
            ['Infinitive', 'Präsens_ich', 'Präsens_du', 'Präsens_er, sie, es', 'Präteritum_ich', 'Partizip II',
             'Konjunktiv II_ich', 'Imperativ Singular', 'Imperativ Plural', 'Hilfsverb'],
            written_info['fieldnames']
        )

        self.assertDictEqual(test_entries[0], written_info['rows'][0])
        self.assertDictEqual(test_entries[1], written_info['rows'][1])

    def __get_written_csv_file(self):
        result = {
            'fieldnames': None,
            'rows': []
        }

        with open(self.test_output_file) as csvfile:
            reader = csv.DictReader(csvfile)

            result['fieldnames'] = reader.fieldnames

            for row in reader:
                result['rows'].append(row)

        return result
