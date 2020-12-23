import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/roshan/Downloads/chromedriver')
        self.driver.get("http://localhost:3000/forgot-password")
        self.driver.maximize_window()
        self.email = self.driver.find_element_by_id("outlined-required")
        self.submit = self.driver.find_element_by_id("submit")

    def test1_incorrect_email_format(self):
        try:
            self.email.send_keys("roshan.shah@")
            self.submit.click()
            alert_msg = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            if alert_msg:
                print("ForgotPassword==>test1_incorrect_email_format,PASSED")
        except Exception as e:
            print("ForgotPassword==>test1_incorrect_email_format,FAILED")
        finally:
            self.driver.quit()

    def test2_correct_email_format(self):
        try:
            self.email.send_keys("roshan.shah@tarento.com")
            self.submit.click()
            expected_msg = "Successfully sent forgot password link. Please check your email for setting password"
            actual_msg = WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_id("client-snackbar").text)
            if expected_msg == actual_msg:
                print("ForgotPassword==>test2_correct_email_format,PASSED")
            else:
                print("ForgotPassword==>test2_correct_email_format,FAILED")
        except Exception as e:
            print("ForgotPassword==>test2_correct_email_format,FAILED")
        finally:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
