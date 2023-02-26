from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
import random


class Functions:

    def __init__(self, driver):
        self.driver = driver

    def save_screenshot(self, path):
        self.driver.get_screenshot_as_file(path)

    def insert_key(self, txt_key):
        self.driver.find_element_by_tag_name('html').send_keys(Keys.txt_key)

    def accept_alert(self):
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        self.driver.switch_to_alert().dismiss()

    def upload_file(self, path):
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)

    def getMessageBody(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

