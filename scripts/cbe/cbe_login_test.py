import ssl
from pydoc import html
from time import sleep

from pip._internal.commands import index
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .cbe_settings import driver

class CbeLoginTest:

    def __init__(self):
        self.driver = None

    def _get_selenium_driver(self) -> webdriver.Chrome:
        if not self.driver:
            options = webdriver.ChromeOptions()
            options.add_argument('javascript.enabled')
            options.add_argument('--no-sandbox')
            self.driver = webdriver.Chrome(options=options)
        return self.driver

    def _wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def _wait_for_alert(self, timeout=10):  # Increased the timeout to 20 seconds
        return WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )

    # Switch to the alert
    alert = driver.switch_to.alert

    # Get the text from the alert
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")

    # Perform actions on the alert if needed (accept, dismiss, etc.)
    alert.accept()  # This accepts the alert

    # If you need to find the XPath, you might need to use browser-specific tools
    # For example, in Chrome, you can right-click on the element and choose "Copy" > "Copy XPath"
    # This will give you the XPath of the element in the alert

    def enter_text_and_submit(self, xpath, text, keys=Keys.ENTER, wait=2):
        textarea = self._wait_for_element(By.XPATH, xpath.format(''))
        textarea.clear()
        sleep(wait)
        textarea.send_keys(text)
        sleep(wait)
        textarea.send_keys(keys)
        sleep(wait)
    def get_otp_from_alert(self, wait=20):  # Increased the timeout to 20 seconds
        alert = self._wait_for_alert(wait)
        otp = alert.text
        alert.accept()
        return otp

    def enter_otp_digit_by_digit(self, otp_xpath_template, otp, body=None):
        for index, digit in enumerate(otp):
            digit_xpath = '/html/body/div[1]/div/div[2]/div/div/form/div/div[1]/div/input[1]'.format(index + 1)
            self.enter_text_and_submit(digit_xpath, digit)

        # Assuming there is a submit button after entering all OTP digits
        submit_button_xpath = '/html/body/div[1]/div/div[2]/div/div/form/div/div[4]/button'
        self.enter_text_and_submit(submit_button_xpath)

# Create an instance of your class
cbeinstance = CbeLoginTest()

# Maximize the browser window
driver = cbeinstance._get_selenium_driver()
driver.maximize_window()

# Open the automation practice site
driver.get('https://ibapi.eaglelionsystems.com/')

# Enter IB username and phone number
cbeinstance.enter_text_and_submit('/html/body/div[1]/div/div[2]/div/form/div/div[1]/label/span[2]/input', 'ib5098864')
cbeinstance.enter_text_and_submit('/html/body/div[1]/div/div[2]/div/form/div/div[2]/label/span[2]/input', '977665544')


# Get OTP from alert
otp = cbeinstance.get_otp_from_alert()
print(f"OTP: {otp}")

# Enter OTP digit by digit
otp_xpath = '/html/body/div[1]/div/div[2]/div/div/form/div/div[1]/div/input[1]/div/input[{}]'
cbeinstance.enter_otp_digit_by_digit(otp_xpath, otp)