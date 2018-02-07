import unittest

from parser.ParseWiktionary import ParseWiktionary


class ParseWiktionaryTest(unittest.TestCase):
    def test_get_field_name(self):
        parser = ParseWiktionary()
        assert parser.get_field_name('test') == '{http://www.mediawiki.org/xml/export-0.10/}test'