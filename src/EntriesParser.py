# coding=utf-8
import csv
import wikitextparser as wtp

import IConfig


class EntriesParser:
    def __init__(self, config: IConfig, entries: dict):
        self.config = config().get_config()
        self.entries = entries

    def get_field_name(self, field_name):
        return '{%s}%s' % (self.config.get('general').get('dump_namespace'), field_name)

    @staticmethod
    def extract_element_template(entry, template_name):
        for template in entry.templates:
            if template.name.strip() == template_name:
                return template

    def parse_element(self, element):
        title = element.find(self.get_field_name('title')).text
        text = element.find(self.get_field_name('revision')).find(self.get_field_name('text')).text

        if text is not None and '{{Wortart|Verb|Deutsch}}' in text:
            entry = wtp.parse(text)

            conjugations = self.extract_conjugations(entry)

            if conjugations is None:
                return

            conjugations.update({'Infinitive': title})

            return conjugations

    def parse_pages(self):
        with open('output/verbs.csv', 'w') as csvfile:
            fieldnames = [
                'Infinitive', 'Präsens_ich', 'Präsens_du', 'Präsens_er, sie, es', 'Präteritum_ich', 'Partizip II',
                'Konjunktiv II_ich', 'Imperativ Singular', 'Imperativ Plural', 'Hilfsverb'
            ]

            writer = csv.DictWriter(csvfile, restval='-', fieldnames=fieldnames, extrasaction='ignore')

            writer.writeheader()

            for event, element in etree.iterparse(self.config.general.dump_path, events=('end',), tag=self.get_field_name('page')):
                parsed_element = self.parse_element(element)
                if parsed_element is not None:
                    writer.writerow(parsed_element)

    def extract_conjugations(self, entry):
        conjugations_template = self.extract_element_template(entry, 'Deutsch Verb Übersicht')

        if not conjugations_template:
            return

        conjugations = {}

        for conjugation_entry in conjugations_template.arguments:
            conjugations.update({conjugation_entry.name.strip(): conjugation_entry.value.strip()})

        return conjugations
