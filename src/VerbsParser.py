# coding=utf-8
import wikitextparser

import IConfig


class VerbsParser:
    valid_entry_text = '{{Wortart|Verb|Deutsch}}'
    conjugations_template_name = 'Deutsch Verb Übersicht'
    infinitive_form_name = 'Infinitive'

    def __init__(self, config: IConfig):
        self.config = config().get_config()
        namespace = self.config.get('general').get('dump_namespace')
        self.namespace = [namespace] if namespace is not None else None

    def parse_entries(self, entries):
        results = []
        for entry in entries:
            parsed_entry = self.parse_entry(entry)

            if parsed_entry:
                results.append(parsed_entry)

        return results

    def parse_entry(self, entry):
        body = self.__get_entry_body(entry)

        if not self.__is_verb_entry(body):
            return False

        parsed_wiki_entry = wikitextparser.parse(body)

        return self.__get_entry_conjugations(self.__get_entry_title(entry), parsed_wiki_entry)

    def __is_verb_entry(self, body):
        return body is not None and self.valid_entry_text in body

    def __get_entry_title(self, entry):
        return entry.find('title', self.namespace).text

    def __get_entry_body(self, entry):
        return entry.find('revision', self.namespace).find('text', self.namespace).text

    def __get_entry_conjugations(self, title, entry):
        template = self.__get_parsed_wiki_entry_template_by_name(entry, self.conjugations_template_name)

        if not template:
            return False

        conjugations = {
            self.infinitive_form_name: title
        }

        for conjugation in template.arguments:
            conjugations.update({conjugation.name.strip(): conjugation.value.strip()})

        return conjugations

    def __get_parsed_wiki_entry_template_by_name(self, entry, name):
        for template in entry.templates:
             if template.name.strip() == name:
                 return template





    # @staticmethod
    # def extract_element_template(entry, template_name):
    #     for template in entry.templates:
    #         if template.name.strip() == template_name:
    #             return template
    #
    # def parse_element(self, element):
    #     title = element.find(self.__get_field_name('title')).text
    #     text = element.find(self.__get_field_name('revision')).find(self.__get_field_name('text')).text
    #
    #     if text is not None and '{{Wortart|Verb|Deutsch}}' in text:
    #         entry = wtp.parse(text)
    #
    #         conjugations = self.extract_conjugations(entry)
    #
    #         if conjugations is None:
    #             return
    #
    #         conjugations.update({'Infinitive': title})
    #
    #         return conjugations
    #
    # def parse_pages(self):
    #     with open('output/verbs.csv', 'w') as csvfile:
    #         fieldnames = [
    #             'Infinitive', 'Präsens_ich', 'Präsens_du', 'Präsens_er, sie, es', 'Präteritum_ich', 'Partizip II',
    #             'Konjunktiv II_ich', 'Imperativ Singular', 'Imperativ Plural', 'Hilfsverb'
    #         ]
    #
    #         writer = csv.DictWriter(csvfile, restval='-', fieldnames=fieldnames, extrasaction='ignore')
    #
    #         writer.writeheader()
    #
    #
    # def extract_conjugations(self, entry):
    #     conjugations_template = self.extract_element_template(entry, 'Deutsch Verb Übersicht')
    #
    #     if not conjugations_template:
    #         return
    #
    #     conjugations = {}
    #
    #     for conjugation_entry in conjugations_template.arguments:
    #         conjugations.update({conjugation_entry.name.strip(): conjugation_entry.value.strip()})
    #
    #     return conjugations
