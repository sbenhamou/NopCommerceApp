# encoding='utf-8'
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustumersPageWE import AddCustomerWE
from pageObjects.DashbordPage import DashBoard
from pageObjects.Customers import Customers
from extensions.Functions import Functions
from extensions.UIActions import Actions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")
        self.dashboard = DashBoard(self.driver)
        self.function = Functions(self.driver)
        self.action = Actions()

        self.action.click_element(self.dashboard.lnkCustomers_menu)
        self.action.click_element(self.dashboard.lnkCustomers_menuitem)

        self.logger.info("************* Providing customer info **********")
        self.customers = Customers(self.driver)
        self.action.click_element(self.customers.btnAddnew)
        self.email = self.function.random_generator() + "@gmail.com"
        self.addcust = AddCustomerWE(self.driver)
        self.action.fill_element(self.addcust.txtEmail, self.email)
        self.action.fill_element(self.addcust.txtPassword, "test123")
        self.action.fill_element(self.addcust.txtFirstName, "Moi")
        self.action.fill_element(self.addcust.txtLastName, "Ceca")
        self.action.click_element(self.addcust.rdFeMaleGender)
        self.action.click_element(self.addcust.btnSave_name)
        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.function.getMessageBody()
        if 'The new customer has been added successfully.' in self.msg:
        # if 'Kuku.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.function.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False
        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")