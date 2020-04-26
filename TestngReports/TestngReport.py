from HTMLTestRunner import HTMLTestRunner
import unittest

from Testscripts import script_1, script_2, script_3, script_4, script_5, script_6, script_7, script_8, script_9, \
    script_10, script_11, script_12, script_13, script_14, script_15, script_16, script_40, script_17, script_18, \
    script_19, script_20, script_21, script_22, script_23, script_24, script_25, script_26, script_27, script_28, \
    script_29, script_30, script_31, script_32, script_33, script_34, script_35, script_36, script_38, script_37, \
    script_39


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
             # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(script_1.Home_page),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_2.Blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_3.Clusters),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_4.Schools),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_5.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_6.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_7.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_8.Report_download),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_9.Home_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_10.Block_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_11.Cluster_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_12.Schools_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_13.Homebtn_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_14.Regular_user),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_15.Regular_userBack),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_16.Choose2),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_17.Choose3),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_18.Choose1),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_19.Choose4),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_20.Choose5),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_21.Choose6),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_22.Choose7),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_23.Choose8),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_24.Choose9),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_25.Choose10),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_26.Choose11),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_27.Choose12),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_28.Choose13),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_29.Choose14),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_30.Choose15),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_31.Choose16),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_32.Choose17),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_33.Choose18),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_34.Choose19),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_35.Choose20),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_36.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_37.Logerror),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_38.Log_Out),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_39.Dist_5),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_40.Hyper_link)

        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Reports.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()