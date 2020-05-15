from HTMLTestRunner import HTMLTestRunner
import unittest

from SAR_validations import Cluster_Mathak, Arvali_district, Dangs, Dangs_clusters, District_block_clicks, \
    Districtoptions_click, Gandhinagar_district, Morbi_wise_validation, Rajkot_blockwisie, Tapi_blockwise, \
    Vallabnagar_clusters, Valsad_blockwise, Valsad_clusterwise, Jamnagar_district

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Arvali_district.District_Arvalli),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_Mathak.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dangs.Block_Dangs),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dangs_clusters.Dangs_clusters),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_block_clicks.Districts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Districtoptions_click.Districts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Gandhinagar_district.Gandhinagar_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Morbi_wise_validation.Block_morbi),
            unittest.defaultTestLoader.loadTestsFromTestCase(Rajkot_blockwisie.Block_Rajokot),
            unittest.defaultTestLoader.loadTestsFromTestCase(Tapi_blockwise.Tapi_blkwise),
            unittest.defaultTestLoader.loadTestsFromTestCase(Vallabnagar_clusters.District_Vallabnagar),
            unittest.defaultTestLoader.loadTestsFromTestCase(Valsad_blockwise.Valsad_blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(Valsad_clusterwise.Valsad_blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(Rajkot_blockwisie.Block_Rajokot),
            unittest.defaultTestLoader.loadTestsFromTestCase(Jamnagar_district.Jayva_cluster_validation),            unittest.defaultTestLoader.loadTestsFromTestCase(Valsad_clusterwise.Valsad_blocks)
        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/SAR2_validation.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing'

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()