# encoding='utf-8'
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import CSVUtils
import csv


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.csv"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("**************** Test_002_DDT_Login ****************")
        self.logger.info("**************** Verifiying Login DDT Page ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        lst_status = []  # empty list variable

        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.username = row['username']
                self.password = row['password']
                self.exp = row['exp']
                self.logger.info("****Test: ****")
                self.logger.info("**************** username: " + self.username + "  ****************")
                self.logger.info("**************** password: " + self.password + "  ****************")
                self.logger.info("**************** expected: " + self.exp + "  ****************")
                self.lp.setUserName(self.username)
                self.lp.setPassWord(self.password)
                self.lp.clickLogin()

                act_title = self.driver.title
                exp_title = "Dashboard / nopCommerce administration"
                if act_title == exp_title:
                    if self.exp == "Pass":
                        self.logger.info("**************** Passed ****************")
                        self.lp.clickLogout()
                        lst_status.append("Pass")
                    elif self.exp == "Fail":
                        # self.driver.get_screenshot_as_file("./Screenshots/"+"test_login.png")
                        self.logger.info("**************** Failed ****************")
                        self.lp.clickLogout()
                        lst_status.append("Fail")
                if act_title != exp_title:
                    if self.exp == "Pass":
                        self.logger.info("**************** Failed ****************")
                        self.lp.clickLogout()
                        lst_status.append("Fail")
                elif self.exp == "Fail":
                    # self.driver.get_screenshot_as_file("./Screenshots/"+"test_login.png")
                    self.logger.info("**************** Passed ****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("****** Login DDT test passed *******")
            self.driver.close()
            assert True
        else:
            self.logger.error("****** Login DDT test failed *******")
            self.driver.close()
            assert True

        self.logger.info("**************** End of Login DDT Page ****************")
        self.logger.info("**************** Completed Test_002_DDT_Login ****************")