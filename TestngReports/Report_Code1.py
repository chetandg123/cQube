from HTMLTestRunner import HTMLTestRunner
import unittest

from Testscripts import script_1, script_2, script_3, script_4, script_5, script_6, script_7, script_8, script_9, \
    script_10, script_11, script_12, script_13, script_14, script_15, script_16, script_40, script_17, script_18, \
    script_19, script_20, script_21, script_22, script_23, script_24, script_25, script_26, script_27, script_28, \
    script_29, script_30, script_31, script_32, script_33, script_34, script_35, script_36, script_38, script_37


class MyTestSuite1(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([

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

        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Report1.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Test script Execution Report'

        )
        runner.run(smoke_test)

if __name__ == '__main__':
    unittest.main()