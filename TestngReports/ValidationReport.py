from HTMLTestRunner import HTMLTestRunner
import unittest

from Validations import Amreli_district, Block_Halvad, Block_memnagar, Block_Nernyanagar, blockdata_check, Blocks_Check, \
    Chandloadiacluster, Check_dist_blk, cluster_jaliya, Cluster_vankiya, Clusters_check, DBP_schoolwise, \
    Dist_morbi, District_DevBhoomi, District_Gir, District_random, district_Vadodara, Home_map, Khedadist, \
    Schools_check, Simar_Una_test, una_block, validation_distblockcuster, AMH_schoollevel
from SAR_validations import Cluster_Mathak


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
             # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(Amreli_district.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_Halvad.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_memnagar.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_Nernyanagar.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(blockdata_check.Blockdata_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_Check.Block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Chandloadiacluster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Check_dist_blk.cityblock_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_jaliya.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_Mathak.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_vankiya.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Clusters_check.Clusters_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(DBP_schoolwise.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_morbi.Morbi_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_DevBhoomi.Gir_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_Gir.Gir_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_random.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(district_Vadodara.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_map.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Khedadist.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_check.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Simar_Una_test.Gir_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(una_block.Gir_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(validation_distblockcuster.Schools_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(AMH_schoollevel.AMH_schools),

        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Data_validation.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Functional Testing'

        )

        runner1.run(functional_test)

if __name__ == '__main__':
    unittest.main()