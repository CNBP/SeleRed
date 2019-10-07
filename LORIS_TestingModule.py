from unittest import TestCase, main
from  collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from time import time
from datetime import date

# Create a Firefox Session
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.implicitly_wait(30)
driver.maximize_window()

# Instantiate a named tuple class to contain the information
Credential = namedtuple("Credential", "URL username password")

class TestLORIS_setup():

    def __init__(self, credential_loris: Credential):
        self.credential = credential_loris




class TestLORIS(TestLORIS_setup, TestCase):


    def test_login(self):
        driver.get(self.credential.URL)
        field_username = driver.find_element_by_xpath('//*[placeholder="Username"]')
        field_username.sendKeys(self.credential.username)

        field_password = driver.find_element_by_xpath('//*[placeholder="Password"]')
        field_password.sendKeys(self.credential.password)

        button_login = driver.find_element_by_xpath('//*[value = "Login"]')
        button_login.click()

        # Check to see if we are still on the same page:
        field_username = driver.find_element_by_xpath('//*[placeholder="Username"]')
        assert field_username is []

    def test_imaging_browser(self):
        pass

    def test_imaging_uploader(self):
        pass

    def test_logout(self):
        pass

    def test_candidate_list(self):
        pass
    def test_candidate_creation(self):
        pass
    def test_candidate_deletion(self):
        pass
    def test_visit_timeopint_creation(self):
        pass
    def test_imaging_browser(self):
        pass
    def test_imaging_browser(self):
        pass
    def test_imaging_browser(self):
        pass

driver.get("https://inscription.ymcaquebec.org/Facilities/FacilitiesSearchWizard.asp")

# Type in search date.

field_facility_booking = driver.find_element_by_id("search-facbook-radio")
field_facility_booking.click()

field_facility_function = Select(driver.find_element_by_id("FacilityFunctions"))
field_facility_function.select_by_visible_text('CV Badminton')


field_centre = driver.find_element_by_xpath('//*[@title="Centre-ville"]')
field_centre.click()

# Get the current date:
today = date.today()
print(f"{today.year}, {today.day}, {today.month}")

date_operations = [
    ("YearFrom", today.year),
    ("MonthFrom", today.strftime("%b")),
    ("DayFrom", today.day),
    ("YearTo", today.year),
    ("MonthTo", today.strftime("%b")),
    ("DayTo", today.day),
]

for operation in date_operations:
    field_year = Select(driver.find_element_by_id(operation[0]))
    field_year.select_by_visible_text(str(operation[1]))