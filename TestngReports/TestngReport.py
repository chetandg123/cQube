from HTMLTestRunner import HTMLTestRunner
import unittest

from POM import Blocks, Clusters, District, Schools
from Testscripts import login_page, click_block, click_clusters, click_schools, click_on_District, District_options, \
    click_Dashboard, click_download, Dots_mouseover, \
    Mouse_over_homepage, mouseover_clusters, mouseover_schools, block_home, click_regularuser, Regular_user, \
    click_districts, click_on_hyperlink, Test_on_District, click_on_district, \
    test_District, District_operations, mouseover_District, mouseover_on_District, mouse_over, mouseover_dots, \
    District_test, District_tests, Dist_options, District_details, \
    mouse_hover_on_dots, click_over_schools, District2, Random_district, District_18_click, Dist_mousehover, Data_test, \
    click_on_crcreports, log_in_out, Error_msg, \
    dots_hover, defect_1, defect_2, defect_3, defect_4, defect_5, defect_6, defect_7


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Regression_test = unittest.TestSuite()
        Regression_test.addTests([
             # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_page.Home_page),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_block.Blocks),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_clusters.Clusters),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_schools.Schools),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_District.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_options.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_Dashboard.District),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_download.Report_download),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dots_mouseover.Home_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mouse_over_homepage.Block_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouseover_clusters.Cluster_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouseover_schools.Schools_Dots),
            unittest.defaultTestLoader.loadTestsFromTestCase(block_home.Homebtn_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_regularuser.Regular_user),
            unittest.defaultTestLoader.loadTestsFromTestCase(Regular_user.Regular_userBack),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_districts.Choose2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_on_District.Choose3),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_district.Choose1),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_District.Choose4),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_operations.Choose5),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouseover_District.Choose6),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouseover_on_District.Choose7),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over.Choose8),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouseover_dots.Choose9),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_test.Choose10),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_tests.Choose11),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_options.Choose12),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_details.Choose13),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_hover_on_dots.Choose14),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_over_schools.Choose15),
            unittest.defaultTestLoader.loadTestsFromTestCase(District2.Choose16),
            unittest.defaultTestLoader.loadTestsFromTestCase(Random_district.Choose17),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_18_click.Choose18),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_mousehover.Choose19),
            unittest.defaultTestLoader.loadTestsFromTestCase(Data_test.Choose20),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_crcreports.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(Error_msg.Logerror),
            unittest.defaultTestLoader.loadTestsFromTestCase(log_in_out.Log_Out),
            unittest.defaultTestLoader.loadTestsFromTestCase(dots_hover.Dist_5),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_hyperlink.Hyper_link),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_1.defect_one),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_2.defect_two),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_3.defect_three),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_4.defect_four),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_5.defect_five),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_6.defect_six),
            unittest.defaultTestLoader.loadTestsFromTestCase(defect_7.defect_seven),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks.Blocks_button),
            unittest.defaultTestLoader.loadTestsFromTestCase(Clusters.Clusters_button),
            unittest.defaultTestLoader.loadTestsFromTestCase(District.Districts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools.Schools_button),

        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/Dummy.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Regression Tests'

        )

        runner1.run(Regression_test)

if __name__ == '__main__':
    unittest.main()