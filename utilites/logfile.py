# import logging
# import datetime
# import os
# import sys
# from sys import platform
# from dotenv import load_dotenv
#
# if platform == 'win32':
#     # windows
#     load_dotenv(r"..\.env")
# if platform == "linux" or platform == "linux2":
#     # linux
#     load_dotenv("../.env")
# elif platform == "darwin":
#     # OS X
#     load_dotenv()
#
# LOG_PATH = os.getenv('LOG_PATH')
#
#
# class Logclass:
#     def getLogs(self):
#         if sys.platform == 'win32':
#             if not os.path.exists(rf"{LOG_PATH}\logs"):
#                 os.makedirs(rf"{LOG_PATH}\logs")
#         else:
#             if not os.path.exists(f"{LOG_PATH}/logs"):
#                 os.mkdir(f"{LOG_PATH}/logs")
#         logger = logging.getLogger()
#         filehandler = logging.FileHandler(
#             f"{LOG_PATH}/logs/" + datetime.datetime.now().strftime(
#                 "%d-%m-%Y") + ".log", mode="w")
#         formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
#                                       datefmt='%d/%m/%Y %I:%M:%S %p')
#         filehandler.setFormatter(formatter)
#         logger.addHandler(filehandler)
#         logger.setLevel(logging.ERROR)
#         # logger.debug("Debug message")
#         # logger.info("Information regarding the test case")
#         # logger.warning("Test case pass but with a Warning message")
#         # logger.error("Test case fail")
#         # logger.critical("Important test case fail on which other test case depends")
#         return logger
