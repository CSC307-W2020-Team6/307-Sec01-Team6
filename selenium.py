from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Safari()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000/register/")
        assert 'register' in selenium.page_source

    def test_login(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000/login/")
        assert 'login' in selenium.page_source

    def test_about(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000/about/")
        assert 'about' in selenium.page_source

    def test_basic(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000/")
        assert '/' in selenium.page_source

    def test_login_credentials(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000/login/")
        login = selenium.find_element_by_link_text("Sign Up")
        login.click()
        assert 'register' in selenium.page_source
