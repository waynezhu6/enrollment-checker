from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client


def authenticate(driver):
    user_name = "zhuwayn1"
    password = "RPtGzVr5z4AsPui"
    driver.get("https://acorn.utoronto.ca/")
    element = driver.find_element_by_id("username")
    element.send_keys(user_name)
    element = driver.find_element_by_id("password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    course_url = "https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/courses/0"
    driver.get(course_url)


def test148(driver):
    time.sleep(1)
    element = driver.find_element_by_id("typeaheadInput")
    element.send_keys("csc148")
    time.sleep(2)
    element.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
    time.sleep(2)

    try:
        enrol_button = driver.find_element_by_id("enrol")
        notify("148")
        return True
    except:
        element.send_keys(Keys.ESCAPE)
        element.clear()
        return False


def test165(driver):
    time.sleep(1)
    element = driver.find_element_by_id("typeaheadInput")
    element.send_keys("csc165")
    time.sleep(2)
    element.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
    time.sleep(2)

    try:
        enrol_button = driver.find_element_by_id("enrol")
        notify("165")
        return True
    except:
        element.send_keys(Keys.ESCAPE)
        element.clear()
        return False


def notify(course_code):
    account_sid = 'ACce0b398cea1e393a8f70dc040d50c535'
    auth_token = 'f61e37faa5e37fe7467c90864136fb47'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body=course_code + " has an open spot",
                from_='+12054309462',
                to='+14373455581')


d = webdriver.Chrome()
authenticate(d)
while True:
    if test165(d):
        time.sleep(300)
    else:
        time.sleep(120)
        d.refresh()
    print('tested')
