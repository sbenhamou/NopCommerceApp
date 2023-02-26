from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomerWE:

    def __init__(self, driver):
        self.driver = driver
        self.txtEmail = self.driver.find_element(By.ID, "Email")
        self.txtPassword = self.driver.find_element(By.ID, "Password")
        self.txtFirstName = self.driver.find_element(By.ID, "FirstName")
        self.txtLastName = self.driver.find_element(By.ID, "LastName")
        self.rdMaleGender = self.driver.find_element(By.ID, "Gender_Male")
        self.rdFeMaleGender = self.driver.find_element(By.ID, "Gender_Female")
        self.txtDob = self.driver.find_element(By.ID, "DateOfBirth")
        self.txtCompanyName = self.driver.find_element(By.ID, "Company")
        # self.txtCPF = self.driver.find_element(By.ID, "customer_attribute_1")
        # self.txtCPFName = self.driver.find_element(By.ID,"customer_attribute_2")
        self.IstaxExcempt = self.driver.find_element(By.ID, "IsTaxExempt")
        # self.lstNewsletter = self.driver.find_element(By.XPATH, "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']//div[@role='listbox']")
        self.lstNewsletter = self.driver.find_element(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]")
        self.lstCustomerRoles = self.driver.find_element(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
        self.drpMgrOfVendor = self.driver.find_element(By.ID, "VendorId")
        self.IsActive = self.driver.find_element(By.ID, "Active")
        self.txtAdminContent = self.driver.find_element(By.ID, "AdminComment")
        self.btnSave_name = self.driver.find_element(By.NAME, "save")
        self.lstitemAdministrators = self.driver.find_element(By.XPATH, "//li[contains(text(),'Administrators')]")
        self.lstitemRegistered = self.driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]")
        self.lstitemGuests = self.driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]")
        self.lstitemVendors = self.driver.find_element(By.XPATH, "//li[contains(text(),'Vendors')]")