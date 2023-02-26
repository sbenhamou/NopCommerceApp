from selenium.webdriver.common.by import By


class DashBoard:

    def __init__(self, driver):
        self.driver = driver
        self.lnkCustomers_menu = self.driver.find_element(By.CLASS_NAME, "fa-user")
        self.lnkCustomers_menuitem = self.driver.find_element(By.XPATH,  "//a[@href='/Admin/Customer/List']")