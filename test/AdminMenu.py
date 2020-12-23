import unittest
from LoginMain import AdminLogin
from selenium.webdriver.support.ui import WebDriverWait
import config


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
                print("AdminMenu==>test1_click_on_user_details,PASSED")
            else:
                print("AdminMenu==>test1_click_on_user_details,FAILED")
        except Exception as e:
            print("AdminMenu==>test1_click_on_user_details,FAILED")
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
                print("AdminMenu==>test2_click_on_my_profile,PASSED")
            else:
                print("AdminMenu==>test2_click_on_my_profile,FAILED")
        except Exception as e:
            print("AdminMenu==>test2_click_on_my_profile,FAILED")
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
                print("AdminMenu==>test3_click_on_logout,PASSED")
            else:
                print("AdminMenu==>test3_click_on_logout,FAILED")
        except Exception as e:
            print("AdminMenu==>test3_click_on_logout,FAILED")
        finally:
            self.login.driver.quit()


if __name__ == '__main__':
    unittest.main()
