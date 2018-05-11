import argparse
import sys

from src.EntriesReader import EntriesReader
from src.VerbsParser import VerbsParser
from src.EntriesCsvWriter import EntriesCsvWriter
from src.Logger import Logger

parser = argparse.ArgumentParser()
parser.add_argument("--dump_path", help="the relative path to the dewiktionary dump")
parser.add_argument("--output_path", help="the relative path to where to save the output")
args = parser.parse_args()

if not args.dump_path and not args.output_path:
    print("Missing parameters")

entries = []


def save_entry(entry):
    entries.append(entry)
    pass

try:
    entries_reader = EntriesReader(args.dump_path)
    verbs_parser = VerbsParser(Logger)
    entries_csv_writer = EntriesCsvWriter(args.output_path)

    entries_reader.get_xml_entries_by_tag('page', save_entry)

    parsed_entries = verbs_parser.parse_entries(entries)

    total_rows_written = entries_csv_writer.write(entries)

    print('Script finished with {} rows written'.format(total_rows_written))
except Exception as err:
    print('Script erorred:', err)