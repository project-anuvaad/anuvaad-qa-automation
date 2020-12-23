import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import config

class SignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(config.chrome_driver_path)
        self.driver.get(config.signup_url)
        self.driver.maximize_window()
        self.firstname = self.driver.find_element_by_id("first-name")
        self.email = self.driver.find_element_by_id("email")
        self.password = self.driver.find_element_by_id("passowrd")
        self.re_password = self.driver.find_element_by_id("re-password")
        self.checkbox = self.driver.find_element_by_id("privacy-policy-checkbox")
        self.signup = self.driver.find_element_by_id("signup-btn")
        self.login = self.driver.find_element_by_id("login")

    def test1_new_credentials(self):
        try:
            self.firstname.send_keys("Roshan")
            self.email.send_keys("rosh.shah@tarento.com")
            self.password.send_keys("Welcome@46")
            self.re_password.send_keys("Welcome@46")
            self.checkbox.click()
            self.signup.click()
            expected_msg = "Successfully created the account. Please check your email for account verification"
            actual_msg = WebDriverWait(self.driver, 20)\
                .until(lambda driver: driver.find_element_by_id("client-snackbar").text)
            if expected_msg == actual_msg:
                print("SignUp==>test1_new_credentials,PASSED")
            else:
                print("SignUp==>test1_new_credentials,FAILED")
        except Exception as e:
            print("SignUp==>test1_new_credentials,FAILED")
        finally:
            self.driver.quit()

    def test2_existing_credentials(self):
        try:
            self.firstname.send_keys("Roshan")
            self.email.send_keys("roshan.shah@tarento.com")
            self.password.send_keys("Welcome@123")
            self.re_password.send_keys("Welcome@123")
            self.checkbox.click()
            self.signup.click()
            expected_msg = "The username already exists. Please use a different username"
            actual_msg = WebDriverWait(self.driver, 20)\
                .until(lambda driver: driver.find_element_by_id("client-snackbar").text)
            if expected_msg == actual_msg:
                print("SignUp==>test2_existing_credentials,PASSED")
            else:
                print("SignUp==>test2_existing_credentials,FAILED")
        except Exception as e:
            print("SignUp==>test2_existing_credentials,FAILED")
        finally:
            self.driver.quit()

    def test3_incorrect_email(self):
        try:
            self.firstname.send_keys("Roshan")
            self.email.send_keys("roshan.shah@")
            self.password.send_keys("Welcome@123")
            self.re_password.send_keys("Welcome@123")
            self.checkbox.click()
            self.signup.click()
            alert_msg = WebDriverWait(self.driver, 20).until(
                ec.alert_is_present())
            if alert_msg:
                self.driver.switch_to.alert.accept()
                print('SignUp==>test3_incorrect_email,PASSED')
            else:
                print('SignUp==>test3_incorrect_email,FAILED')
        except Exception as e:
            print("SignUp==>test3_incorrect_email,FAILED")
        finally:
            self.driver.quit()

    def test4_password_format(self):
        try:
            self.firstname.send_keys("Roshan")
            self.email.send_keys("rosh.shah@tarento.com")
            self.password.send_keys("Welcome")
            self.re_password.send_keys("Welcome")
            self.checkbox.click()
            self.signup.click()
            alert_msg = WebDriverWait(self.driver, 20).until(
                ec.alert_is_present())
            if alert_msg:
                self.driver.switch_to.alert.accept()
                print('SignUp==>test4_password_format,PASSED')
            else:
                print('SignUp==>test4_password_format,FAILED')
        except Exception as e:
            print("SignUp==>test4_password_format,FAILED")
        finally:
            self.driver.quit()

    def test5_click_on_login(self):
        try:
            self.login.click()
            expected_url = config.login_url + '#'
            login_page = WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == expected_url)
            if login_page:
                print("SignUp==>test5_click_on_login,PASSED")
            else:
                print("SignUp==>test5_click_on_login,FAILED")
        except Exception as e:
            print("SignUp==>test5_click_on_login,FAILED")
        finally:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
