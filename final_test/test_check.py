# imports
from FUNCTIONS.helper import Checker
import json
from logfile import Logclass


# test case
def test_demo(browser):
    logger = Logclass()
    log = logger.getLogs()
    log.error("This test is now running")
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
    count_checkbox = run.count_all("xpath", data["common"]["locator2"])
    print(f"Total number of checkboxes: {count_checkbox}")
    #
    # ##################
    # # INPUT IN FIELDS
    # ##################
    run.input("xpath", data["common"]["locator3"], "Sample Value 1")
    run.input("xpath", data["common"]["locator4"], "Sample Value 2")
    #
    # ##################
    # # UNCHECK A CHECKED BOX
    # ##################
    run.button("xpath", data["common"]["locator5"])
    #
    # ##################
    # # STATIC DROPDOWN WITH DELAY
    # ##################
    # run.static_dropdown("xpath", "//select[@id='options']", "index", "3")
    # run.slowmo(2)
    # run.static_dropdown("xpath", "//select[@id='options']", "value", "1")
    # run.slowmo(2)
    # run.static_dropdown("xpath", "//select[@id='options']", "visible", "Option2")
    #
    # ##################
    # # OPENING A NEW WEBPAGE AND PRINTING ITS URL
    # ##################
    # run.goto("https://example.com/")
    # current_tab_url = run.current_tab_url()
    # print(f"New URL is: {current_tab_url}")
    # run.goto("http://127.0.0.1:5500/sample.html")
    #
    # ##################
    # # SEARCHING AND SELECTING FROM DYNAMIC FIELDS
    # ##################
    # run.dynamic_dropdown("input", "xpath", "//input[@id='myInput']", "i", "xpath", "//div[@id='names']",
    #                      "index", "4")
    # run.dynamic_dropdown("input", "xpath", "//input[@id='myInput']", "i", "xpath", "//div[@id='names']",
    #                      "value", "India")
    #
    # ##################
    # # CLICKING TO GET ALERT BOX, PRINTING THE ALERT TEXT AND ACCEPTING THE ALERT
    # ##################
    # run.button("xpath", "//button[normalize-space()='Try it']", "click")
    # popup_text = run.popup_text()
    # print(f"This is the popup text: {popup_text}")
    # run.popup_accept()
    #
    # ##################
    # # UPLOADS A FILE FROM THE ABSOLUTE PATH GIVEN
    # ##################
    # # run.file_upload("xpath", "//input[@id='myFile']", "")
    #
    # ##################
    # # WAITS IMPLICITLY TILL THE CHECKBOX APPEARS AND THEN CLICKS
    # ##################
    # run.implicit_wait(4.5)
    # run.button("xpath", "//p[@id='demo']//input[@type='checkbox']", "click")
    # run.button("xpath", "//p[@id='demo2']//input[@type='checkbox']", "click")
    #
    # ##################
    # # WAITS EXPLICITLY TILL THE CHECKBOX APPEARS AND THEN CLICKS
    # ##################
    # run.explicit_wait(5, "element_to_be_clickable", "xpath", "//p[@id='demo']//input[@type='checkbox']")
    # run.button("xpath", "//p[@id='demo']//input[@type='checkbox']", "click")
    #
    # ##################
    # # WAITS EXPLICITLY TILL THE CHECKBOX APPEARS AND THEN CLICKS
    # ##################
    # run.mouse_hover("xpath", "//button[normalize-space()='Dropdown']")
    # run.button("xpath", "//a[normalize-space()='Link 1']", "click")
    # run.goto("http://127.0.0.1:5500/sample.html")
    #
    # ##################
    # # GO TO FRAME AND CHECK ALL CHECKBOXES
    # ##################
    # run.shift_to_frame("xpath", "//iframe[@title='Deja vu']")
    # run.check_all("xpath", data["common"]["locator1"])
    # run.leave_frame()
    #
    # ##################
    # # DOUBLE CLICK BUTTON
    # ##################
    # run.double_click("xpath", "//button[normalize-space()='double click me!']")
    #
    # ##################
    # # DISPLAY TEXT OF ELEMENT(CHECKBOX)
    # ##################
    # text = run.return_text("xpath", "//label[@for='clicked1']")
    # print(text)
    # run.display_text("xpath", "//label[@for='clicked1']")
    #
    # #################
    # # DISPLAY TEXT OF ELEMENT(CHECKBOX)
    # #################
    # text = run.return_attribute("xpath", "//input[@id='myInput']", "placeholder")
    # print(text)
    # run.display_attribute("xpath", "//input[@id='myInput']", "placeholder")
    #
    # run.display_all_inner_text("xpath", "//*[contains(@*, 'clicked')]")
    # a = run.return_all_inner_text("xpath", "//*[contains(@*, 'clicked')]")
    # print(a)
    #
    # ##################
    # # CHECKS IF CHECKBOX IS CLICKED OR NOT
    # ##################
    # a = run.is_checked_return("xpath", "//input[@id='clicked1']")
    # if a:
    #     print("yes")  # checkbox is checked
    # else:
    #     print("no")  # checkbox is not checked
    # run.is_checked_display("xpath", "//input[@id='clicked1']")
    #
    # ##################
    # # CHECKS IF ELEMENT IS VISIBLE
    # ##################
    # a = run.is_visible_return("xpath", "//label[@for='clicked19']")
    # if a:
    #     print("yes")  # is visible
    # else:
    #     print("no")  # not visible
    # run.is_visible_display("xpath", "//label[@for='clicked19']")

    a = run.return_is_clickable("xpath", "//button[@id='nonclick']")
    if a:
        print("yes")  # is clickable
    else:
        print("no")  # not clickable
    run.display_is_clickable("xpath", "//button[@id='nonclick']")

    a = run.return_is_clickable("xpath", "//button[@id='nonclick2']")
    if a:
        print("yes")  # is clickable
    else:
        print("no")  # not clickable
    run.display_is_clickable("xpath", "//button[@id='nonclick2']")



