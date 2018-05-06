from IConfig import IConfig


class FakeVerbsConfig(IConfig):
    dump_namespace = 'http://www.mediawiki.org/xml/export-0.10/'

    def get_config(self):
        return {
            'general': {
                'dump_path': 'dump/dewiktionary-pages-meta-current.xml',
                'dump_namespace': self.dump_namespace
            }
        }