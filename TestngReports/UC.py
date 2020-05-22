from HTMLTestRunner import HTMLTestRunner
import unittest

from User_create import user_pwd_click, click_on_usercreate, Fillup_user, Negative_changepwd, set_new_password


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(user_pwd_click.Click_on_pwd),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_usercreate.Click_create),
            unittest.defaultTestLoader.loadTestsFromTestCase(Fillup_user.Fillup_user),
            unittest.defaultTestLoader.loadTestsFromTestCase(Negative_changepwd.Click_ChangePwd),
            unittest.defaultTestLoader.loadTestsFromTestCase(set_new_password.Click_ChangePassword),
        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/User_validation.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing for User creation '

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()