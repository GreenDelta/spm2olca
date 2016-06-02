from .util import make_uuid, flow_uuid
from .mappings import compartment


class Method(object):

    def __init__(self):
        self.name = ''
        self.comment = ''
        self.weighting_unit = ''
        self.impact_categories = []

    @property
    def uid(self):
        return make_uuid('ImpactMethod', self.name)


class ImpactCategory(object):

    def __init__(self, line):
        parts = [p.strip() for p in line.split(';')]
        self.name = parts[0]
        self.ref_unit = parts[1]
        self.factors = []

    @property
    def uid(self):
        return make_uuid('ImpactCategory', self.name)


class ImpactFactor(object):

    def __init__(self):
        self.category = ''
        self.sub_category = ''
        self.name = ''
        self.cas = ''
        self.value = 0
        self.unit = ''

    @property
    def flow_uid(self):
        return flow_uuid(self.category, self.sub_category, self.name, self.unit)

    @property
    def flow_category_uid(self):
        return make_uuid('Category', self.category)

    @property
    def flow_sub_category_uid(self):
        return make_uuid('Category', self.category, self.sub_category)


def parse_factor(line: str) -> ImpactFactor:
    f = ImpactFactor()
    parts = [p.strip() for p in line.split(';')]
    f.category = compartment(parts[0])
    f.sub_category = compartment(parts[1])
    f.name = parts[2]
    f.cas = parts[3]
    f.value = float(parts[4].replace(',', '.'))
    f.unit = parts[5]
    return f
