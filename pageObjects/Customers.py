from selenium.webdriver.common.by import By


class Customers:

    def __init__(self, driver):
        self.driver = driver
        self.btnAddnew = self.driver.find_element(By.CLASS_NAME, "fa-plus-square")
        # self.btnAddnew = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add new']")