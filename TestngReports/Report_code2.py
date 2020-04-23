from HTMLTestRunner import HTMLTestRunner
import unittest

from Testscripts import  script_11, script_12, script_13, script_14, script_15, script_16, script_40, script_17, script_18, \
    script_19, script_20


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            #  file name .class name

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


        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Report2.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='TestScript Execution Report',
            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()