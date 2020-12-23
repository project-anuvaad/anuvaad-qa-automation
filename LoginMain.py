from selenium import webdriver
import config


class UserLogin:
    def __int__(self):
        self.path = config.chrome_driver_path
        self.driver = webdriver.Chrome(config.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get(config.login_url)
        self.email = self.driver.find_element_by_id("email")
        self.password = self.driver.find_element_by_id("passowrd")
        self.signin = self.driver.find_element_by_id("signin-btn")
        self.email.send_keys("sajish@gmail.com")
        self.password.send_keys("Test@12")
        return self


class AdminLogin:
    def __int__(self):
        self.path = config.chrome_driver_path
        self.driver = webdriver.Chrome(config.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get(config.login_url)
        self.email = self.driver.find_element_by_id("email")
        self.password = self.driver.find_element_by_id("passowrd")
        self.signin = self.driver.find_element_by_id("signin-btn")
        self.email.send_keys("kumar.deepak@tarento.com")
        self.password.send_keys("Kd@123")
        return self