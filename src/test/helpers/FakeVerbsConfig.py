from IConfig import IConfig


class FakeVerbsConfig(IConfig):
    def get_config(self):
        return {
            'general': {
                'dump_path': 'dump/dewiktionary-pages-meta-current.xml',
                'dump_namespace': 'http://www.mediawiki.org/xml/export-0.10/'
            }
        }