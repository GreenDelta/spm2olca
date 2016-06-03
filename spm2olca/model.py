from .util import make_uuid, flow_uuid
from .mappings import compartment


class Method(object):
    def __init__(self):
        self.name = ''
        self.comment = ''
        self.weighting_unit = ''
        self.impact_categories = []
        self.nw_sets = []

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


class NwSet(object):
    def __init__(self, name):
        self.name = name
        self.normalisations = []
        self.weightings = []

    @property
    def uid(self):
        return make_uuid('NwSet', self.name)

    @property
    def impact_categories(self):
        """ Returns the names of LCIA categories in this normalisation and
            weighting set.
        """
        factors = self.normalisations + self.weightings
        names = []
        for f in factors:
            if f.impact_category not in names:
                names.append(f.impact_category)
        return names

    def get_weighting_factor(self, impact_category):
        for f in self.weightings:
            if f.impact_category == impact_category:
                return f.factor
        return None

    def get_normalisation_factor(self, impact_category):
        for f in self.normalisations:
            if f.impact_category == impact_category:
                return f.factor
        return None


class NwFactor(object):
    def __init__(self):
        self.impact_category = ''
        self.factor = 0.0


def parse_impact_factor(line: str) -> ImpactFactor:
    f = ImpactFactor()
    parts = [p.strip() for p in line.split(';')]
    f.category = compartment(parts[0])
    f.sub_category = compartment(parts[1])
    f.name = parts[2]
    f.cas = parts[3]
    f.value = float(parts[4].replace(',', '.'))
    f.unit = parts[5]
    return f


def parse_nw_factor(line: str) -> NwFactor:
    f = NwFactor()
    parts = [p.strip() for p in line.split(';')]
    f.impact_category = parts[0]
    f.factor = float(parts[1])
    return f
