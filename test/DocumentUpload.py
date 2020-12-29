import unittest
import config
import os
import time
from LoginMain import UserLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DocumentUpload(unittest.TestCase):
    def setUp(self):
        self.login = UserLogin().__int__()
        self.login.signin.click()
        start_translate = WebDriverWait(self.login.driver, 20) \
            .until(lambda driver: driver.find_element_by_id("start-translate"))
        start_translate.click()
        self.source_lang = self.login.driver.find_element_by_id("source-lang")
        self.target_lang = self.login.driver.find_element_by_id("target-lang")
        self.upload = self.login.driver.find_element_by_id("upload")
        self.back = self.login.driver.find_element_by_id("back")
        self.file_upload = self.login.driver.find_element_by_xpath("//input[@type='file']")
        time.sleep(3)

    def test1_upload_document(self):
        try:
            driver = self.login.driver
            self.source_lang.click()
            source_english = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id("English"))
            source_english.click()
            self.target_lang.click()
            target_hindi = WebDriverWait(driver, 20).until(lambda d: d.find_element_by_id("Hindi"))
            target_hindi.click()
            time.sleep(2)
            self.file_upload.send_keys("/home/roshan/Downloads/2c6d61e3-3a84-4f37-814e-d20f2073a05f.pdf")
            time.sleep(5)
            self.upload.click()
            result = WebDriverWait(driver, 20).until(lambda d: d.current_url == config.view_document_url)
            time.sleep(5)
            if result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_upload_document"),PASSED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test1_upload_document"),FAILED')
        finally:
            driver.quit()

    def test2_click_on_back_button(self):
        try:
            driver = self.login.driver
            self.back.click()
            result = WebDriverWait(driver, 20).until(lambda d: d.current_url == config.view_document_url)
            time.sleep(5)
            if result:
                print(
                    f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_click_on_back_button"),PASSED')
        except Exception:
            print(
                f'=HYPERLINK("{config.hyperlink_pretext}{os.path.basename(__file__)}";"test2_click_on_back_button"),FAILED')
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
