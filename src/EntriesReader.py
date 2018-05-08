from lxml import etree


class EntriesReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_xml_entries_by_tag(self, tag, callback):
        key_found = False

        for event, element in etree.iterparse(self.file_name, events=('end',), tag=tag):
            callback(element)
            key_found = True

        if not key_found:
            raise KeyError("Desired tag '{tag}' not found".format(tag=tag))
