import unittest
from selenium.webdriver.support.ui import WebDriverWait
from LoginMain import UserLogin
import config


class UserMenu(unittest.TestCase):

    def setUp(self):
        self.login = UserLogin().__int__()
        self.login.signin.click()
        menu_btn = WebDriverWait(self.login.driver, 20).until(lambda driver: driver.find_element_by_id("open-menu"))
        menu_btn.click()

    def test1_click_on_translate_sentence(self):
        try:
            expected_instant_translate_url = config.instant_translate_url
            instant_translate = WebDriverWait(self.login.driver, 20)\
                .until(lambda driver: driver.find_element_by_id("instant-translate"))
            instant_translate.click()
            result = WebDriverWait(self.login.driver, 20)\
                .until(lambda driver: driver.current_url == expected_instant_translate_url)
            if result:
                print("UserMenu==>test1_click_on_translate_sentence,PASSED")
            else:
                print("UserMenu==>test1_click_on_translate_sentence,FAILED")
        except Exception as e:
            print("UserMenu==>test1_click_on_translate_sentence,FAILED")
        finally:
            self.login.driver.quit()

    def test2_click_on_translate_document(self):
        try:
            expected_translate_document_url = config.view_document_url

            translate_document = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.find_element_by_id("view-document"))
            translate_document.click()
            result = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.current_url == expected_translate_document_url)
            if result:
                print("UserMenu==>test2_click_on_translate_document,PASSED")
            else:
                print("UserMenu==>test2_click_on_translate_document,FAILED")
        except Exception as e:
            print("UserMenu==>test2_click_on_translate_document,FAILED")
        finally:
            self.login.driver.quit()

    def test3_click_on_my_profile(self):
        try:
            expected_my_profile_url = config.profile_url
            my_profile = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.find_element_by_id("profile"))
            my_profile.click()
            result = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.current_url == expected_my_profile_url)
            if result:
                print("UserMenu==>test3_click_on_my_profile,PASSED")
            else:
                print("UserMenu==>test3_click_on_my_profile,FAILED")
        except Exception as e:
            print("UserMenu==>test3_click_on_my_profile,FAILED")
        finally:
            self.login.driver.quit()

    def test4_click_on_logout(self):
        try:
            expected_logout_url = config.login_url
            logout = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.find_element_by_id("logout"))
            logout.click()
            result = WebDriverWait(self.login.driver, 20) \
                .until(lambda driver: driver.current_url == expected_logout_url)
            if result:
                print("UserMenu==>test4_click_on_logout,PASSED")
            else:
                print("UserMenu==>test4_click_on_logout,FAILED")
        except Exception as e:
            print("UserMenu==>test4_click_on_logout,FAILED")
        finally:
            self.login.driver.quit()


if __name__ == '__main__':
    unittest.main()
