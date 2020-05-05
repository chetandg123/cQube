import unittest

from HTMLTestRunner import HTMLTestRunner

from Defects import defect_1, defect_2, defect_3, defect_4, defect_6, defect_5, defect_7


class MyTestSuite1(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(defect_1.defect_one),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_2.defect_two),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_3.defect_three),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_4.defect_four),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_5.defect_five),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_6.defect_six),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_7.defect_seven),


        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Defects/DefectReport.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Test script Execution Report'

        )
        runner.run(smoke_test)

if __name__ == '__main__':
    unittest.main()