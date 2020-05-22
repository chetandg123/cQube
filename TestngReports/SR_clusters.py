import time

from HTMLTestRunner import HTMLTestRunner
import unittest

from Semester_Assessment.Clusterwise_validation import Amreli, Amreli_District, Anand_test, Arvalli_district, \
    Banaskanth_test, Bharuch_amodtest, Bhavnagar_test, Botad_district, Chota_district, clickon_Clusterbtn, \
    Cluster_Chatrali, Cluster_validation, Dangs, Gandhinagar_test, Girsomanath_test, home_icon, Jamnagar_test, \
    Juna_district, junagadh_Mendarda, Kheda, Mahesana_test, Mahisagar, Navsari, Panch_mahals, Sabarkant_district, \
    Surat_test, Surendranagar_district, Tapi_district, Vadodara_test, Valsad_test


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Amreli.Amreli_district),
            unittest.defaultTestLoader.loadTestsFromTestCase(Amreli_District.Amreli_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Anand_test.Anand_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Arvalli_district.Aravalli_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Banaskanth_test.Banskanth_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Bharuch_amodtest.Amod_block),
            unittest.defaultTestLoader.loadTestsFromTestCase(Bhavnagar_test.Bhavnagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Botad_district.Botad_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Chota_district.chhota_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(clickon_Clusterbtn.blockbtn_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_Chatrali.Chatrali_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_validation.Ahmedabad_amc),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dangs.Dangs_district),
            unittest.defaultTestLoader.loadTestsFromTestCase(Gandhinagar_test.Ghandinagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Girsomanath_test.Gir_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(home_icon.Home_icon),
            unittest.defaultTestLoader.loadTestsFromTestCase(Jamnagar_test.Jamnagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Juna_district.Juna_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(junagadh_Mendarda.Panch_mahals),
            unittest.defaultTestLoader.loadTestsFromTestCase(Kheda.kheda_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mahesana_test.Home_page),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mahisagar.Mahisagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Navsari.Navsari_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Panch_mahals.Panch_mahals),
            unittest.defaultTestLoader.loadTestsFromTestCase(Sabarkant_district.sabarkaanth_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Surat_test.Surat_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Surendranagar_district.surendranagar_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Tapi_district.Tapi_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Vadodara_test.Vadodara_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Valsad_test.Valsad_District)







        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/SRcluster.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing of Semester Assessment'

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()