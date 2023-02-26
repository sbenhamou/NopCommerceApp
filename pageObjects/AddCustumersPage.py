import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:

    lnkCustomers_menu_class = "fa-user"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_class = "fa-plus-square"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    txtCPF_id = "customer_attribute_1"
    txtCPFName_id = "customer_attribute_2"
    IstaxExcempt_id = "IsTaxExempt"
    lstNewsletter_xpath = "/(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    lstCustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    drpMgrOfVendor_id = "VendorId"

    IsActive_id = "Active"
    txtAdminContent_id = "AdminComment"
    btnSave_name = "save"
    msg = "body"

    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.CLASS_NAME, self.lnkCustomers_menu_class).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.CLASS_NAME, self.btnAddnew_class).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.lstCustomerRoles_xpath).click()
        # time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            # time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        # time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drpMgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.ID, self.txtDob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID, self.txtCompanyName_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.ID, self.txtAdminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.NAME, self.btnSave_name).click()

    def getMessage(self):
        return self.driver.find_element(By.TAG_NAME, self.msg).text
