import spm2olca.model as m


class Parser(object):

    def __init__(self):
        self.methods = []

        self._method = None
        self._section = None

    def parse(self, file_path):
        with open(file_path, 'r', encoding='windows-1252') as f:
            for raw_line in f:
                line = raw_line.strip()
                self._next_line(line)

    def _next_line(self, line):
        if line == 'Method':
            self._method = m.Method()
            return
        if self._method is None:
            return
        if line == 'End':
            self._clear()
