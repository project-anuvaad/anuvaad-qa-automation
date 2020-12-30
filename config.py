import os

if os.name == 'posix':
    chrome_driver_path = "./ChromeDriver/Linux/chromedriver"
else:
    chrome_driver_path = "/ChromeDriver/Windows/chromedriver.exe"


login_url = "https://developers.anuvaad.org/"
view_document_url = "https://developers.anuvaad.org/view-document"
user_details_url = "https://developers.anuvaad.org/user-details"
forgot_password_url = "https://developers.anuvaad.org/forgot-password"
signup_url = "https://developers.anuvaad.org/signup"
instant_translate_url = "https://developers.anuvaad.org/instant-translate"
profile_url = "https://developers.anuvaad.org/profile"
hyperlink_pretext = "https://raw.githubusercontent.com/project-anuvaad/anuvaad-qa-automation/master/test/"
