import unittest
from selenium import webdriver

base_url = "http://localhost:8000"

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(base_url+ '/login') 

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        username_input = self.driver.find_element_by_id("username")
        password_input = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_id("submit")

        username_input.send_keys("testuser")
        password_input.send_keys("password")
        submit_button.click()

        # Assert that the user is redirected to the home page
        self.assertEqual(self.driver.current_url, "http://localhost:8000/home")

    def test_failed_login(self):
        username_input = self.driver.find_element_by_id("username")
        password_input = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_id("submit")

        username_input.send_keys("testuser")
        password_input.send_keys("wrongpassword")
        submit_button.click()

        # Assert that the user stays on the login page and sees an error message
        error_message = self.driver.find_element_by_id("error-message")
        self.assertEqual(self.driver.current_url, "http://localhost:8000/login")
        self.assertTrue(error_message.is_displayed())

if __name__ == "__main__":
    unittest.main()