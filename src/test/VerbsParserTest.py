import unittest
from lxml import etree
from helpers.FakeVerbsConfig import FakeVerbsConfig
from helpers.FakeLogger import FakeLogger
from VerbsParser import VerbsParser


class VerbsParserTest(unittest.TestCase):
    def test_parse_entry(self):
        test_entry = etree.ElementTree().parse('dump/wiktionary_entry.xml')

        FakeVerbsConfig.dump_namespace = None
        parser = VerbsParser(FakeVerbsConfig, FakeLogger)

        result = parser.parse_entry(test_entry)

        self.assertDictEqual(
            {'Infinitive': 'lieben', 'Präsens_ich': 'liebe', 'Präsens_du': 'liebst', 'Präsens_er, sie, es': 'liebt',
             'Präteritum_ich': 'liebte', 'Partizip II': 'geliebt', 'Konjunktiv II_ich': 'liebte',
             'Imperativ Singular': 'liebe', 'Imperativ Plural': 'liebt', 'Hilfsverb': 'haben'},
            result
        )

    def test_parse_entries(self):
        parser = VerbsParser(FakeVerbsConfig, FakeLogger)
        test_entries = []

        for event, element in etree.iterparse('dump/wiktionary_dump.xml', events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page'):
            test_entries.append(element)

        result = parser.parse_entries(test_entries)

        self.assertEqual(2, len(result))

        self.assertDictEqual(
            {'Infinitive': 'lieben', 'Präsens_ich': 'liebe', 'Präsens_du': 'liebst', 'Präsens_er, sie, es': 'liebt',
             'Präteritum_ich': 'liebte', 'Partizip II': 'geliebt', 'Konjunktiv II_ich': 'liebte',
             'Imperativ Singular': 'liebe', 'Imperativ Plural': 'liebt', 'Hilfsverb': 'haben'},
            result[0]
        )

        self.assertDictEqual(
            {'Infinitive': 'klieben', 'Präsens_ich': 'kliebe', 'Präsens_du': 'kliebst', 'Präsens_er, sie, es': 'kliebt',
             'Präteritum_ich': 'klob', 'Präteritum_ich*': 'kliebte', 'Partizip II': 'gekloben',
             'Partizip II*': 'gekliebt', 'Konjunktiv II_ich': 'klöbe', 'Konjunktiv II_ich*': 'kliebte',
             'Imperativ Singular': 'kliebe', 'Imperativ Plural': 'kliebt', 'Hilfsverb': 'haben'},
            result[1]
        )

    def test_parse_entries_no_entries(self):
        parser = VerbsParser(FakeVerbsConfig, FakeLogger)
        test_entries = []

        result = parser.parse_entries(test_entries)

        self.assertEqual(0, len(result))

    def test_parse_entries_no_valid_entries(self):
        parser = VerbsParser(FakeVerbsConfig, FakeLogger)
        test_entries = [etree.ElementTree().parse('dump/simple_dump.xml')]

        result = parser.parse_entries(test_entries)

        self.assertEqual(0, len(result))