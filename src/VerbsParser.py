# coding=utf-8
import wikitextparser

from src.ILogger import ILogger


class VerbsParser:
    valid_entry_text = '{{Wortart|Verb|Deutsch}}'
    conjugations_template_name = 'Deutsch Verb Übersicht'
    infinitive_form_name = 'Infinitive'

    def __init__(self, logger: ILogger):
        self.logger = logger()

    def parse_entries(self, entries):
        results = []
        for entry in entries:
            parsed_entry = self.parse_entry(entry)

            if parsed_entry:
                results.append(parsed_entry)

        return results

    def parse_entry(self, entry):
        try:
            body = self.__get_entry_body(entry)

            if not self.__is_verb_entry(body):
                return False

            parsed_wiki_entry = wikitextparser.parse(body)

            return self.__get_entry_conjugations(self.__get_entry_title(entry), parsed_wiki_entry)
        except AttributeError:
            self.logger.warning('Invalid entry', entry)
            return False

    def __is_verb_entry(self, body):
        return body is not None and self.valid_entry_text in body

    def __get_entry_title(self, entry):
        return entry.find('title', namespaces=entry.nsmap).text

    def __get_entry_body(self, entry):
        return entry.find('revision', namespaces=entry.nsmap).find('text', namespaces=entry.nsmap).text

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
