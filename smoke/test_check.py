# imports
from FUNCTIONS.helper import Checker
import json
from logfile import Logclass


# test case
def test_checking(browser):
    logger = Logclass()
    log = logger.getLogs()
    log.info("This test is now running")
    #################
    with open("locators/demo.json", 'r') as f:
        data = json.loads(f.read())
    ##################
    #  PASSING URL AND WEBDRIVER
    ##################
    run = Checker("http://127.0.0.1:5500/sample.html", browser)

    ##################
    # METHODS TO DISPLAY URL
    ##################
    run.display_url()
    website_url = run.return_url()
    print(f"Website url is: {website_url}")

    ##################
    # CHECK ALL CHECKBOXES
    ##################
    run.check_all("xpath", data["common"]["locator1"])

    ##################
    # COUNT ALL CHECKBOXES
    ##################
    count_checkbox = run.count_all_checkboxes("xpath", data["common"]["locator2"])
    print(f"Total number of checkboxes: {count_checkbox}")

    ##################
    # INPUT IN FIELDS
    ##################
    run.input("input", "xpath", data["common"]["locator3"], "type", "Sample Value 1")
    run.input("input", "xpath", data["common"]["locator4"], "type", "Sample Value 2")

    ##################
    # UNCHECK A CHECKED BOX
    ##################
    run.button("checkbox", "xpath", data["common"]["locator5"], "click")

    ##################
    # STATIC DROPDOWN WITH DELAY
    ##################
    run.static_dropdown("xpath", "//select[@id='options']", "index", "3")
    run.slowmo(2)
    run.static_dropdown("xpath", "//select[@id='options']", "value", "1")
    run.slowmo(2)
    run.static_dropdown("xpath", "//select[@id='options']", "visible", "Option2")

    ##################
    # OPENING A NEW WEBPAGE AND PRINTING ITS URL
    ##################
    run.goto("https://example.com/")
    current_tab_url = run.current_tab_url()
    print(f"New URL is: {current_tab_url}")
    run.goto("http://127.0.0.1:5500/sample.html")

    ##################
    # SEARCHING AND SELECTING FROM DYNAMIC FIELDS
    ##################
    run.dynamic_dropdown("input", "xpath", "//input[@id='myInput']", "type", "i", "xpath", "//div[@id='names']",
                         "index", "4")

    ##################
    # CLICKING TO GET ALERT BOX, PRINTING THE ALERT TEXT AND ACCEPTING THE ALERT
    ##################
    run.button("button", "xpath", "//button[@onclick='myFunction()']", "click")
    popup_text = run.popup_text()
    print(f"This is the popup text: {popup_text}")
    run.popup_accept()

    ##################
    # UPLOADS A FILE FROM THE ABSOLUTE PATH GIVEN
    ##################
    # run.file_upload("xpath", "//input[@id='myFile']", "")

    ##################
    # WAITS TILL THE CHECKBOX APPEARS AND THEN CLICKS
    ##################
    run.implicit_wait(4.5)
    run.button("checkbox", "xpath", "//p[@id='demo']//input[@type='checkbox']", "click")
    run.button("checkbox", "xpath", "//p[@id='demo2']//input[@type='checkbox']", "click")
