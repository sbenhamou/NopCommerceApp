import configparser

config = configparser.RawConfigParser()
configFilePath = r'C:\Users\sbenhamou\PycharmProjects\nopcommerceApp\Configurations\config.ini'
config.read(configFilePath)


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password