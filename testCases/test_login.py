# encoding='utf-8'
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info("**************** Verifiying Home Page Title ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("**************** Home Page Title is passed ****************")
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file("./Screenshots/"+"test_homePageTitle.png")
            self.logger.error("**************** Home Page Title is failed ****************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("**************** Verifiying Login Page ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**************** Login Page is passed ****************")
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file("./Screenshots/"+"test_login.png")
            self.logger.error("**************** Login Page is failed ****************")
            self.driver.close()
            assert False
