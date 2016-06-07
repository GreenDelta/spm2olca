import spm2olca.mappings as maps
import spm2olca.model as model
import unittest


class MappingTest(unittest.TestCase):

    def test_get_mapped_flow(self):
        flow_map = maps.FlowMap.create()
        line = 'Raw;(unspecified);Occupation, arable;;0.42;m2a'
        factor = model.parse_impact_factor(line)
        mapped_flow = flow_map.get(factor.flow_uid)
        self.assertIsNotNone(mapped_flow)

if __name__ == '__main__':
    unittest.main()