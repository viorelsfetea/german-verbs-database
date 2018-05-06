import unittest

from EntriesReader import EntriesReader


class EntriesReaderTest(unittest.TestCase):

    def setUp(self):
        self.test_get_xml_entries_callback_called = False
        self.test_get_xml_entries_callback_called_times = 0
        self.test_get_xml_entries_callback_results = []

    def test_get_xml_entries_by_tag(self):
        def callback_function(element):
            self.test_get_xml_entries_callback_called = True
            self.test_get_xml_entries_callback_called_times += 1

            self.assertEqual('some nested value', element.text.strip())

        reader = EntriesReader('dump/simple_dump.xml')

        reader.get_xml_entries_by_tag('xml', callback_function)

        self.assertTrue(self.test_get_xml_entries_callback_called)
        self.assertEquals(1, self.test_get_xml_entries_callback_called_times)

    def test_get_xml_entries_by_tag_multiple_children(self):
        def callback_function(element):
            self.test_get_xml_entries_callback_called = True
            self.test_get_xml_entries_callback_called_times += 1
            self.test_get_xml_entries_callback_results.append(element.text.strip())

        reader = EntriesReader('dump/dump_with_two_entries.xml')

        reader.get_xml_entries_by_tag('xml', callback_function)

        self.assertTrue(self.test_get_xml_entries_callback_called)
        self.assertEquals(2, self.test_get_xml_entries_callback_called_times)
        self.assertEquals('some nested value', self.test_get_xml_entries_callback_results[0])
        self.assertEquals('another nested value', self.test_get_xml_entries_callback_results[1])

    def test_get_xml_entries_by_tag_not_found(self):
        def callback_function(element):
            self.test_get_xml_entries_callback_called = True

        reader = EntriesReader('dump/simple_dump.xml')

        self.assertFalse(self.test_get_xml_entries_callback_called)
        self.assertRaises(KeyError, reader.get_xml_entries_by_tag, 'not xml', callback_function)
