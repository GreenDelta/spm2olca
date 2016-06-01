import csv
from .data import data_dir


class UnitEntry(object):

    def __init__(self, csv_row):
        self.unit_name = csv_row[0]
        self.unit_id = csv_row[1]
        self.property_name = csv_row[2]
        self.property_id = csv_row[3]


class UnitMap(object):

    def __init__(self):
        self.mappings = {}
        path = data_dir+'/units.csv'
        with open(path, 'r', encoding='utf-8', newline='\n') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # skip first line
            for line in reader:
                entry = UnitEntry(line)
                self.mappings[entry.unit_name] = entry

    def get(self, unit_name: str) -> UnitEntry:
        if unit_name in self.mappings:
            return self.mappings[unit_name]
        return None
