import logging
import datetime
import os
import sys


class Logclass:
    def getLogs(self):
        directory = os.getcwd()
        LOG_PATH = os.environ.get('LOG_PATH')
        if LOG_PATH is None:
            LOG_PATH = directory
        if sys.platform == 'win32':
            if not os.path.exists(rf"{LOG_PATH}\automation-report"):
                os.makedirs(rf"{LOG_PATH}\automation-report")
            if not os.path.exists(rf"{LOG_PATH}\automation-report\logs"):
                os.makedirs(rf"{LOG_PATH}\automation-report\logs")
        else:
            if not os.path.exists(f"{LOG_PATH}/automation-report"):
                os.mkdir(f"{LOG_PATH}/automation-report")
            if not os.path.exists(f"{LOG_PATH}/automation-report/logs"):
                os.mkdir(f"{LOG_PATH}/automation-report/logs")
        logger = logging.getLogger()
        filehandler = logging.FileHandler(
            f"{LOG_PATH}/automation-report/logs/" + datetime.datetime.now().strftime(
                "%d-%m-%Y") + ".log", mode="w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.ERROR)
        # logger.debug("Debug message")
        # logger.info("Information regarding the test case")
        # logger.warning("Test case pass but with a Warning message")
        # logger.error("Test case fail")
        # logger.critical("Important test case fail on which other test case depends")
        return logger
