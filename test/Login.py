import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import config
import os


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(config.chrome_driver_path)
        self.driver.get(config.login_url)
        self.driver.maximize_window()
        self.email = self.driver.find_element_by_id("email")
        self.password = self.driver.find_element_by_id("passowrd")
        self.signin = self.driver.find_element_by_id("signin-btn")
        self.forgotpwd = self.driver.find_element_by_id("forgotpassword")
        self.signup = self.driver.find_element_by_id("signup")

    def test1_login_with_user_credentials(self):
        try:
            self.email.send_keys("sajish@gmail.com")
            self.password.send_keys("Test@12")
            self.signin.click()
            expected_url = config.view_document_url
            actual_url = WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == expected_url)
            if actual_url:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_login_with_user_credentials"),PASSED')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_login_with_user_credentials"),FAILED')
        finally:
            self.driver.quit()

    def test2_login_with_incorrect_credentials(self):
        try:
            self.email.send_keys("sajish@gmail.com")
            self.password.send_keys("Test@1")
            self.signin.click()
            actual_msg = WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_id("client-snackbar"))
            if actual_msg:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_login_with_incorrect_credentials"),PASSED')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_login_with_incorrect_credentials"),FAILED')
        finally:
            self.driver.quit()

    def test3_click_on_forgot_password(self):
        try:
            self.forgotpwd.click()
            expected_url = config.forgot_password_url + '#'
            actual_url = WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == expected_url)
            if actual_url:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_click_on_forgot_password"),PASSED')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_click_on_forgot_password"),FAILED')
        finally:
            self.driver.quit()

    def test4_click_on_sign_up(self):
        try:
            self.signup.click()
            expected_url = config.signup_url + '#'
            actual_url = WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == expected_url)
            if actual_url:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test4_click_on_sign_up"),PASSED')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test4_click_on_sign_up"),FAILED')
        finally:
            self.driver.quit()

    def test5_login_with_admin_credentials(self):
        try:
            self.email.send_keys("kumar.deepak@tarento.com")
            self.password.send_keys("Kd@123")
            self.signin.click()
            expected_url = config.user_details_url
            actual_url = WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == expected_url)
            if actual_url:
                print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test5_login_with_admin_credentials"),PASSED')
        except Exception as e:
            print(f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test5_login_with_admin_credentials"),FAILED')
        finally:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()