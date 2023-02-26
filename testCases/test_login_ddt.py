# encoding='utf-8'
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from utilities import CSVUtils


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("**************** Test_002_DDT_Login ****************")
        self.logger.info("**************** Verifiying Login DDT Page ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Demo')
        # self.rows = XLUtils.getRowCount(self.path)
        print("Number of Rows in the Excel:", self.rows)

        lst_status = [] #empty list variable
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'Demo', r, 1)
            self.password = XLUtils.readData(self.path, 'Demo', r, 2)
            self.exp = XLUtils.readData(self.path, 'Demo', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            # time.sleep(5)

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


