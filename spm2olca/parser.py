import spm2olca.model as m


class Parser(object):
    def __init__(self):
        self.methods = []

        self._method = None
        self._section = None
        self._category = None

    def parse(self, file_path):
        with open(file_path, 'r', encoding='windows-1252') as f:
            for raw_line in f:
                line = raw_line.strip()
                self._next_line(line)

    def _next_line(self, line):

        if line == 'Method':
            # start of a new method
            self._method = m.Method()
            return

        if self._method is None:
            return

        if line == '':
            # empty lines are section separators
            if self._category is not None and self._section == 'Substances':
                self._category = None
            self._section = None
            return

        if line == 'End':
            self._end()

        if self._section is None:
            self._section = line
            return

        self._data_row(line)

    def _end(self):
        if self._method is not None:
            self.methods.append(self._method)
        self._method = None
        self._section = None

    def _data_row(self, line):
        if self._section == 'Name':
            self._method.name = line
            return

        if self._section == 'Comment':
            self._method.comment = line
            return

        if self._section == 'Weighting unit':
            self._method.weighting_unit = line
            return

        if self._section == 'Impact category':
            self._category = m.ImpactCategory()
            self._category.name = line
            self._method.impact_categories.append(self._category)
            return

        if self.section == 'Substances' and self._category is not None:
            f = m.parse_factor(line)
            self._category.factors.append(f)
