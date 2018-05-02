import unittest

from FakeVerbsConfig import FakeVerbsConfig
from EntriesParser import EntriesParser


class ParseWiktionaryTest(unittest.TestCase):
    def test_get_field_name(self):
        parser = EntriesParser(FakeVerbsConfig)
        assert parser.get_field_name('test') == '{http://www.mediawiki.org/xml/export-0.10/}test'