import ssl
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YourClassName:

    def __init__(self):
        self.driver = None

    def _get_selenium_driver(self) -> webdriver.Chrome:
        if not self.driver:
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument('javascript.enabled')
            options.add_argument('--no-sandbox')
            self.driver = webdriver.Chrome(options=options)
        return self.driver

    def _wait_for_element(self, by, value, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def enter_text_and_submit(self, xpath, text, keys=Keys.ENTER, wait=2):
        textarea = self._wait_for_element(By.XPATH, xpath)
        textarea.clear()
        sleep(wait)
        textarea.send_keys(text)
        sleep(wait)
        textarea.send_keys(keys)
        sleep(wait)

# Create an instance of your class
your_instance = YourClassName()

# Maximize the browser window
driver = your_instance._get_selenium_driver()
driver.maximize_window()

# Open the automation practice site
driver.get('https://ibapi.eaglelionsystems.com/')
# Enter IB username and phone number
your_instance.enter_text_and_submit('/html/body/div[1]/div/div[2]/div/form/div/div[1]/label/span[2]/input', 'ib5098864')
your_instance.enter_text_and_submit('/html/body/div[1]/div/div[2]/div/form/div/div[2]/label/span[2]/input', '977665544')