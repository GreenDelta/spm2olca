class Method(object):

    def __init__(self):
        self.name = ''
        self.comment = ''
        self.weighting_unit = ''
        self.impact_categories = []


class ImpactCategory(object):

    def __init__(self):
        self.name = ''
        self.factors = []


class ImpactFactor(object):

    def __init__(self):
        self.category = ''
        self.sub_category = ''
        self.name = ''
        self.cas = ''
        self.value = 0
        self.unit = ''


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
