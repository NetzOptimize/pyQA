import pytest
import os
from datetime import datetime
from py.xml import html
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as cOP
from selenium.webdriver.firefox.options import Options as fOP
from selenium.webdriver.edge.options import Options as eOP
import sys

from sys import platform
from dotenv import load_dotenv

if platform == 'win32':
    # windows
    load_dotenv(r".env")
if platform == "linux" or platform == "linux2":
    # linux
    load_dotenv(".env")
elif platform == "darwin":
    # OS X
    load_dotenv()
REPORT_PATH = os.getenv('REPORT_PATH')

# from extra_report import generate_content
chrome_options = cOP()
firefox_options = fOP()
edge_options = eOP()
##################################################################
firefox_options.set_preference('detach', True) # keeps browser open
chrome_options.add_experimental_option("detach", True)  # keeps browser open
##################################################################
# edge_options.add_argument("--remote-debugging-port=9222")
# edge_options.add_experimental_option('useAutomationExtension', False)
# edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# edge_options.add_argument("headless")
# edge_options.add_argument('disable-gpu')
# edge_options.use_chromium = True
edge_options.use_chromium = True
edge_options.add_argument("headless")
edge_options.add_argument("disable-gpu")
##################################################################
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--profile-directory=Default')
# chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')
chrome_options.headless = True
##################################################################
# firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.headless = True
##################################################################


# TODO: add support for firefox browser (IndexError: list index out of range) for childscreen
# TODO: safari webdriver
# TODO: add screenshot to html report

# chrome_list = [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#                ]
# firefox_list = [webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
#                 ]
# edge_list = [webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
#              ]
#
# my_list = [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options),
#            webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
#            ]


# @pytest.fixture(scope="session", params=my_list, ids=["chrome", "firefox"])
# def setup(request):
#     return request.param


def pytest_addoption(parser):
    parser.addoption('--b1', action='store', help='store browser')
    parser.addoption('--b2', action='store', help='store browser')


browsers = ["chrome", "chrome-head", "firefox", "firefox-head", "edge", "edge-head"]


def pytest_generate_tests(metafunc):
    parameters = []
    ids = []
    if "browser" in metafunc.fixturenames:
        # test-name = metafunc.function.__name__
        browser1 = metafunc.config.getoption("b1")
        browser2 = metafunc.config.getoption("b2")
        ########################################################################
        # B1
        ########################################################################
        ###################################
        # CHROME
        ###################################
        if browser1 == "chrome":
            chrome_options.headless = True
            parameters += [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)]
            ids += ["chrome"]
        if browser1 == "chrome-head":
            chrome_options.headless = False
            parameters += [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)]
            ids += ["chrome-head"]
        ###################################
        # FIREFOX
        ###################################
        if browser1 == "firefox":
            firefox_options.headless = True
            parameters += [webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)]
            ids += ["firefox"]
        if browser1 == "firefox-head":
            firefox_options.headless = False
            parameters += [webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)]
            ids += ["firefox-head"]
        ###################################
        # EDGE
        ###################################
        if browser1 == "edge":
            chrome_options.headless = True
            parameters += [webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)]
            ids += ["edge"]
        if browser1 == "edge-head":
            chrome_options.headless = True
            parameters += [webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))]
            ids += ["edge-head"]
        ###################################
        ###################################
        if browser1 not in browsers and browser1 is not None:
            pytest.fail("No such browser")
        ########################################################################
        # B2
        ########################################################################
        ###################################
        # CHROME
        ###################################
        if browser2 == "chrome":
            chrome_options.headless = True
            parameters += [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)]
            ids += ["chrome"]
        if browser2 == "chrome-head":
            chrome_options.headless = False
            parameters += [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)]
            ids += ["chrome-head"]
        ###################################
        # FIREFOX
        ###################################
        if browser2 == "firefox-head":
            firefox_options.headless = False
            parameters += [webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)]
            ids += ["firefox-head"]
        if browser2 == "firefox":
            firefox_options.headless = True
            parameters += [webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)]
            ids += ["firefox"]
        ###################################
        # EDGE
        ###################################
        if browser2 == "edge":
            chrome_options.headless = True
            parameters += [webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)]
            ids += ["edge"]
        if browser2 == "edge-head":
            chrome_options.headless = True
            parameters += [webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))]
            ids += ["edge-head"]
        ###################################
        ###################################
        if browser2 not in browsers and browser2 is not None:
            pytest.fail("No such browser")
        ###################################
        # IF NOTHING IS SPECIFIED DEFAULT BROWSER -> CHROME
        ###################################
        if browser1 is None and browser2 is None:
            parameters += [webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)]
            ids += ["chrome"]

    metafunc.parametrize("browser", parameters, ids=ids)


def pytest_html_report_title(report):
    report.title = "Report"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if sys.platform == 'win32':
        if not os.path.exists(rf"{REPORT_PATH}\reports"):
            os.makedirs(rf"{REPORT_PATH}\reports")
    else:
        if not os.path.exists(f"{REPORT_PATH}/reports"):
            os.mkdir(f"{REPORT_PATH}/reports")
    if sys.platform == 'win32':
        if not os.path.exists(rf"{REPORT_PATH}\excel_reports"):
            os.makedirs(rf"{REPORT_PATH}\excel_reports")
    else:
        if not os.path.exists(f"{REPORT_PATH}/excel_reports"):
            os.mkdir(f"{REPORT_PATH}/excel_reports")
    config.option.htmlpath = f"{REPORT_PATH}/reports/" + \
                             datetime.now().strftime("%d-%m-%Y/%d-%m-%Y") + ".html"


def pytest_html_results_table_header(cells):
    ''' meta programming to modify header of the result'''

    from py.xml import html
    # removing old table headers
    del cells[1]
    # adding new headers
    cells.insert(0, html.th('Time', class_='sortable time', col='time'))
    cells.insert(1, html.th('Folder'))
    cells.insert(2, html.th('Testcase'))
    cells.insert(3, html.th('Method'))
    cells.insert(4, html.th('Browser'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    ''' orienting the data gotten from  pytest_runtest_makereport
    and sending it as row to the result '''
    del cells[1]
    cells.insert(0, html.td(datetime.today(), class_='col-time'))
    cells.insert(1, html.td(report.folder))
    cells.insert(2, html.td(report.testcase))
    cells.insert(3, html.td(report.method))
    cells.insert(4, html.td(report.browser))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''data from the output of pytest gets processed here
     and are passed to pytest_html_results_table_row'''
    outcome = yield
    # this is the output that is seen end of test case
    report = outcome.get_result()
    report.folder = re.split(r"/", report.nodeid)[0]
    report.testcase = re.split(r"/|::", report.nodeid)[1]
    report.method = re.split(r"/|::|\[|\]", report.nodeid)[2]

    # taking input args
    # example:
    #      report.nodeid = 'tests/test_case.py::test_min[input0-1]'
    #    data = re.split(r"\[|\]", 'tests/test_case.py::test_min[input0-1]')
    #    =>  ['tests/test_case.py::test_min', 'input0-1', '']
    report.browser = re.split(r"\[|\]", report.nodeid)[-2]

