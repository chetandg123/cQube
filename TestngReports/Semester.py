import time

from HTMLTestRunner import HTMLTestRunner
import unittest

from Semester_Assessment import Ahmedabad_Bavla, Amc, Arvali_district, Block_btn, Cluster_btn, Dangs, Dev_test, \
    dist_check, District_block_clicks, District_dataTest, DistrictNames, Gandhinagar_district, Jamnagar_district, \
    Jamnagar_Lalpur, Login_Page, Mahesana_dist, Mahisagar_test, Morbi_blocks, Morbi_wise_validation, Rajkot_blockwisie, \
    SR_Home, Tapi_blockwise, Vallabnagar_clusters, scbtn


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Ahmedabad_Bavla.District_Arvalli),
            unittest.defaultTestLoader.loadTestsFromTestCase(Amc.District_Ahmedabad),
            unittest.defaultTestLoader.loadTestsFromTestCase(Arvali_district.District_Arvalli),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_btn.blockbtn_click),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_btn.blockbtn_click),

            unittest.defaultTestLoader.loadTestsFromTestCase(Dangs.District_TheDangs),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dev_test.District_Dev),
            unittest.defaultTestLoader.loadTestsFromTestCase(dist_check.Semester_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_block_clicks.Districts),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_dataTest.Semester_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(DistrictNames.Semester_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(Gandhinagar_district.Gandhinagar_dist_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Jamnagar_district.Jamnagar_block),
            unittest.defaultTestLoader.loadTestsFromTestCase(Jamnagar_Lalpur.Jamnaagar_block),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login_Page.Semester_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mahesana_dist.Mahesana_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mahisagar_test.Mahisagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Morbi_blocks.Morbhi),
            unittest.defaultTestLoader.loadTestsFromTestCase(Morbi_wise_validation.Morbhi),
            unittest.defaultTestLoader.loadTestsFromTestCase(Rajkot_blockwisie.Rajkot_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(scbtn.School_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(SR_Home.Semester_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(Tapi_blockwise.Tapi_blkwise),
            unittest.defaultTestLoader.loadTestsFromTestCase(Vallabnagar_clusters.Vallabnagar_dist),


        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/SemesterReport.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing of Semester Assessment'

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()