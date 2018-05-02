import unittest

from EntriesReader import EntriesReader


class EntriesReaderTest(unittest.TestCase):
    def test_get_file(self):
        reader = EntriesReader('dump/simple_dump.xml')

        file = reader.get_file()

        self.assertEqual(file.get('sample').get('xml'), 'some nested value')