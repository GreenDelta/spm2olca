import json
import spm2olca.mappings as mappings
import spm2olca.model as model
import zipfile as zipf


class Pack(object):
    def __init__(self, methods):
        self.methods = methods
        self.unit_map = mappings.UnitMap()
        self._gen_categories = {}

    def to(self, zip_file):
        pack = zipf.ZipFile(zip_file, mode='a', compression=zipf.ZIP_DEFLATED)
        for method in self.methods:
            self._method(method, pack)
        pack.close()

    def _method(self, method: model.Method, pack: zipf.ZipFile):
        obj = {'@type': 'ImpactMethod',
               '@id': method.uid,
               'name': method.name,
               'description': method.comment,
               'impactCategories': []}
        for category in method.impact_categories:
            ref = {'@type': 'ImpactCategory', '@id': category.uid}
            obj['impactCategories'].append(ref)
            self._impact_category(category, pack)
        dump(obj, 'lcia_methods', pack)

    def _impact_category(self, category: model.ImpactCategory, pack):
        obj = {'@type': 'ImpactCategory',
               '@id': category.uid,
               'name': category.name,
               'referenceUnitName': category.ref_unit,
               'impactFactors': []}
        for factor in category.factors:
            obj['impactFactors'].append(self._factor(factor, pack))
        dump(obj, 'lcia_categories', pack)

    def _factor(self, factor: model.ImpactFactor, pack):
        self._flow_category(factor, pack)
        unit_entry = self.unit_map.get(factor.unit)
        if unit_entry is None:
            print('ERROR: unknown unit ' + factor.unit)
            print('  skipped factor ...')
            return

    def _flow_category(self, factor: model.ImpactFactor, pack) -> str:
        sub_uid = factor.flow_sub_category_uid
        if sub_uid in self._gen_categories:
            return sub_uid
        parent_uid = factor.flow_category_uid
        if parent_uid not in self._gen_categories:
            obj = {'@type': 'Category', '@id': parent_uid,
                   'name': factor.category, 'modelType': 'FLOW'}
            dump(obj, 'categories', pack)
            self._gen_categories[parent_uid] = True
        obj = {'@type': 'Category',
               '@id': sub_uid,
               'name': factor.sub_category,
               'modelType': 'FLOW',
               'category': {'@type': 'Category', '@id': parent_uid}}
        dump(obj, 'categories', pack)
        self._gen_categories[sub_uid] = True
        return sub_uid


def dump(obj, folder, pack):
    path = '%s/%s.json' % (folder, obj['@id'])
    s = json.dumps(obj)
    pack.writestr(path, s)
