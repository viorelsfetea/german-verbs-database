import unittest
from lxml import etree
from FakeVerbsConfig import FakeVerbsConfig
from VerbsParser import VerbsParser


class VerbsParserTest(unittest.TestCase):
    def test_parse_entry(self):
        test_entry = etree.ElementTree().parse('dump/wiktionary_entry.xml')

        FakeVerbsConfig.dump_namespace = None
        parser = VerbsParser(FakeVerbsConfig)

        result = parser.parse_entry(test_entry)

        self.assertDictEqual(
            {'Infinitive': 'lieben', 'Präsens_ich': 'liebe', 'Präsens_du': 'liebst', 'Präsens_er, sie, es': 'liebt',
             'Präteritum_ich': 'liebte', 'Partizip II': 'geliebt', 'Konjunktiv II_ich': 'liebte',
             'Imperativ Singular': 'liebe', 'Imperativ Plural': 'liebt', 'Hilfsverb': 'haben'},
            result
        )

    def test_parse_entries(self):
        parser = VerbsParser(FakeVerbsConfig)
        test_entries = []

        for event, element in etree.iterparse('dump/wiktionary_dump.xml', events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page'):
            test_entries.append(element)

        result = parser.parse_entries(test_entries)

        pass