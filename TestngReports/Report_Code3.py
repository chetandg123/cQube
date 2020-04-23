from HTMLTestRunner import HTMLTestRunner
import unittest

from Testscripts import  script_21, script_22, script_23, script_24, script_25, script_26, script_27, script_28, \
    script_29, script_30


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            #  file name .class name

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


        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Report3.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='TestScript Execution Report',
            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()