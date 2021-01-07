import unittest
from LoginMain import AdminLogin
from selenium.webdriver.support.ui import WebDriverWait
import config
import os


class AdminMenu(unittest.TestCase):
    def setUp(self):
        self.login = AdminLogin().__int__()
        self.login.signin.click()
        menu_btn = WebDriverWait(self.login.driver, 20).until(lambda driver: driver.find_element_by_id("open-menu"))
        menu_btn.click()

    def test1_click_on_user_details(self):
        try:
            expected_user_details__url = config.user_details_url
            user_details = WebDriverWait(self.login.driver, 20)\
                .until(lambda driver: driver.find_element_by_id("user-details"))
            user_details.click()
            result = WebDriverWait(self.login.driver, 20)\
                .until(lambda driver: driver.current_url == expected_user_details__url)
            if result:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_click_on_user_details"),PASSED, By clicking the User Detail option inside the menu list, User Detail page gets loaded')
            else:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_click_on_user_details"),FAILED, By clicking the User Detail option inside the menu list, User Detail page gets loaded')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_click_on_user_details"),FAILED, By clicking the User Detail option inside the menu list, User Detail page gets loaded')
        finally:
            self.login.driver.quit()

    def test2_click_on_my_profile(self):
        try:
            expected_my_profile_url = config.profile_url
            my_profile = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.find_element_by_id("profile"))
            my_profile.click()
            result = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.current_url == expected_my_profile_url)
            if result:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_click_on_my_profile"),PASSED, By clicking the Profile option inside the menu list, Profile page gets loaded')
            else:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_click_on_my_profile"),FAILED, By clicking the Profile option inside the menu list, Profile page gets loaded')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_click_on_my_profile"),FAILED, By clicking the Profile option inside the menu list, Profile page gets loaded')
        finally:
            self.login.driver.quit()

    def test3_click_on_logout(self):
        try:
            expected_logout_url = config.login_url
            logout = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.find_element_by_id("logout"))
            logout.click()
            result = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.current_url == expected_logout_url)
            if result:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_click_on_logout"),PASSED, By clicking the Logout option inside the menu list, user gets redirected to the Login Page')
            else:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_click_on_logout"),FAILED, By clicking the Logout option inside the menu list, user gets redirected to the Login Page')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_click_on_logout"),FAILED, By clicking the Logout option inside the menu list, user gets redirected to the Login Page')
        finally:
            self.login.driver.quit()


if __name__ == '__main__':
    unittest.main()
