# coding=utf-8
import os
from lxml import etree


class ParseWiktionary:
    dump_path = os.path.abspath('../dump/dewiktionary-pages-meta-current.xml')
    dump_namespace = 'http://www.mediawiki.org/xml/export-0.10/'

    def get_field_name(self, field_name):
        return '{%s}%s' % (self.dump_namespace, field_name)

    def parse_element(self, element):
        title = element.find(self.get_field_name('title')).text
        text = element.find(self.get_field_name('revision')).find(self.get_field_name('text')).text

        if text is not None and '{{Wortart|Verb|Deutsch}}' in text:
            # parse entry
            pass

    def parse_pages(self):
        for event, element in etree.iterparse(self.dump_path, events=('end',), tag=self.get_field_name('page')):
            self.parse_element(element)
