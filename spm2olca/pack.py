import json
import spm2olca.model as model
import zipfile as zipf


class Pack(object):

    def __init__(self, methods):
        self.methods = methods

    def to(self, zip_file):
        pack = zipf.ZipFile(zip_file, mode='a', compression=zipf.ZIP_DEFLATED)
        for method in self.methods:
            self._method(method, pack)
        pack.close()

    def _method(self, method: model.Method, pack: zipf.ZipFile):
        obj = {
            '@type': 'ImpactMethod',
            '@id': method.uid,
            'name': method.name,
            'description': method.comment,
            'impactCategories': []
        }
        for category in method.impact_categories:
            ref = {'@type': 'ImpactCategory', '@id': category.uid}
            obj['impactCategories'].append(ref)
            self._impact_category(category, pack)
        dump(obj, 'lcia_methods', pack)

    def _impact_category(self, category: model.ImpactCategory, pack):
        obj = {
            '@type': 'ImpactCategory',
            '@id': category.uid,
            'name': category.name,
            'referenceUnitName': category.ref_unit,
            'impactFactors': []
        }
        dump(obj, 'lcia_categories', pack)


def dump(obj, folder, pack):
    path = '%s/%s.json' % (folder, obj['@id'])
    s = json.dumps(obj)
    pack.writestr(path, s)