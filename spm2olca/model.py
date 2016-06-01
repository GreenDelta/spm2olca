import uuid


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
        return make_uuid('Flow', self.category, self.sub_category, self.name,
                         self.unit)

    @property
    def flow_category_uid(self):
        return make_uuid('Category', self.category)

    @property
    def flow_sub_category_uid(self):
        return make_uuid('Category', self.category, self.sub_category)


def parse_factor(line: str) -> ImpactFactor:
    f = ImpactFactor()
    parts = [p.strip() for p in line.split(';')]
    f.category = parts[0]
    f.sub_category = parts[1]
    f.name = parts[2]
    f.cas = parts[3]
    f.value = float(parts[4].replace(',', '.'))
    f.unit = parts[5]
    return f


def make_uuid(*args: list) -> str:
    path = as_path(*args)
    return str(uuid.uuid3(uuid.NAMESPACE_OID, path))


def as_path(*args: list) -> str:
    strings = []
    for arg in args:
        if arg is None:
            continue
        strings.append(str(arg).lower())
    return "/".join(strings)