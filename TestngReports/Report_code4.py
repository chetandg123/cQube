from HTMLTestRunner import HTMLTestRunner
import unittest

from Testscripts import script_31, script_32, script_33, script_34, script_35, script_36, script_38, script_37, \
    script_40, script_39


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(script_31.Choose16),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_32.Choose17),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_33.Choose18),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_34.Choose19),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_35.Choose20),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_36.CRC_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_37.Logerror),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_38.Log_Out),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_39.Dist_5),
            unittest.defaultTestLoader.loadTestsFromTestCase(script_40.Hyper_link),

        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Report4.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Testscript Execution Report',
            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()