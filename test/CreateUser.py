import unittest
from LoginMain import AdminLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import config
import os
import time


class CreateUser(unittest.TestCase):
    def setUp(self):
        self.login = AdminLogin().__int__()
        self.login.signin.click()
        create_user = WebDriverWait(self.login.driver, 20) \
            .until(lambda driver: driver.find_element_by_id("create-user"))
        create_user.click()
        self.name = self.login.driver.find_element_by_id("name")
        self.email = self.login.driver.find_element_by_id("email")
        self.password = self.login.driver.find_element_by_id("password")
        self.roles = self.login.driver.find_element_by_id("roles")
        self.hide_show = self.login.driver.find_element_by_id("hide-show")
        self.save = self.login.driver.find_element_by_id("save")
        self.reset = self.login.driver.find_element_by_id("reset")
        time.sleep(3)

    def test1_create_existing_user_with_admin_role(self):
        driver = self.login.driver
        try:
            expected_result = "The username already exists. Please use a different username"
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail.com")
            self.password.send_keys("Test@11")
            self.roles.click()
            admin = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('ADMIN'))
            admin.click()
            self.save.click()
            actual_result = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id("client-snackbar").text)
            if actual_result == expected_result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_create_existing_user_with_admin_role"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_create_existing_user_with_admin_role"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_create_existing_user_with_admin_role"),FAILED')
        finally:
            self.login.driver.quit()

    def test2_create_existing_user_with_translator_role(self):
        driver = self.login.driver
        try:
            expected_result = "The username already exists. Please use a different username"
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail.com")
            self.password.send_keys("Test@11")
            self.roles.click()
            translator = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('TRANSLATOR'))
            translator.click()
            self.save.click()
            actual_result = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id("client-snackbar").text)
            if actual_result == expected_result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_create_existing_user_with_translator_role"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_create_existing_user_with_translator_role"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_create_existing_user_with_translator_role"),FAILED')
        finally:
            self.login.driver.quit()

    def test3_create_user_with_incorrect_email(self):
        driver = self.login.driver
        try:
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail")
            self.password.send_keys("Test@11")
            self.roles.click()
            translator = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('TRANSLATOR'))
            translator.click()
            self.save.click()
            actual_result = WebDriverWait(driver, 20).until(ec.alert_is_present())
            time.sleep(2)
            if actual_result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_create_user_with_incorrect_email"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_create_user_with_incorrect_email"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test3_create_user_with_incorrect_email"),FAILED')
        finally:
            self.login.driver.quit()

    def test4_create_user_with_incorrect_password(self):
        driver = self.login.driver
        try:
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail.com")
            self.password.send_keys("test@11")
            self.roles.click()
            translator = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('TRANSLATOR'))
            translator.click()
            self.save.click()
            actual_result = WebDriverWait(driver, 20).until(ec.alert_is_present())
            time.sleep(2)
            if actual_result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test4_create_user_with_incorrect_password"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test4_create_user_with_incorrect_password"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test4_create_user_with_incorrect_password"),FAILED')
        finally:
            self.login.driver.quit()

    def test5_click_on_show_password(self):
        driver = self.login.driver
        try:
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail")
            self.password.send_keys("test@11")
            self.roles.click()
            translator = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('TRANSLATOR'))
            translator.click()
            self.hide_show.click()
            password_type = self.password.get_attribute("type")
            time.sleep(2)
            if password_type == "text":
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test5_click_on_show_password"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test5_click_on_show_password"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test5_click_on_show_password"),FAILED')
        finally:
            self.login.driver.quit()

    def test6_click_on_reset(self):
        driver = self.login.driver
        try:
            self.name.send_keys("Sajish")
            self.email.send_keys("sajish11@gmail")
            self.password.send_keys("test@11")
            self.roles.click()
            translator = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id('TRANSLATOR'))
            translator.click()
            self.reset.click()
            time.sleep(2)
            if not self.name.get_attribute("value") and not self.email.get_attribute(
                    "value") and not self.password.get_attribute("value") and not self.roles.get_attribute(
                    "value"):
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test6_click_on_reset"),PASSED')
            else:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test6_click_on_reset"),FAILED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test6_click_on_reset"),FAILED')
        finally:
            self.login.driver.quit()


if __name__ == '__main__':
    unittest.main()
