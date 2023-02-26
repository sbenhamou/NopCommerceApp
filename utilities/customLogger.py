import logging


class LogGen:
    @staticmethod
    def loggen():
        # FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
        # FORMAT = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
        FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format=FORMAT, datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
