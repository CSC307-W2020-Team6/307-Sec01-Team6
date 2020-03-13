# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# 
# 
# class AccountTestCase(LiveServerTestCase):
# 
#     def setUp(self):
#         self.selenium = webdriver.Safari()
#         super(AccountTestCase, self).setUp()
# 
#     def tearDown(self):
#         self.selenium.quit()
#         super(AccountTestCase, self).tearDown()
# 
#     def test_register(self):
#         selenium = self.selenium
#         # Opening the link we want to test
#         selenium.get('http://127.0.0.1:8000/register/')
#         # find the form element
#         username = selenium.find_element_by_id('id_username')
#         email = selenium.find_element_by_id('email')
#         password1 = selenium.find_element_by_id('password1')
#         password2 = selenium.find_element_by_id('password2')
#         submit = selenium.find_element_by_name('register')
# 
#         username.send_keys('rmete')
#         email.send_keys('riley@mete.com')
#         password1.send_keys('password321')
#         password2.send_keys('password321')
# 
#         submit.send_keys(Keys.RETURN)
# 
#         assert 'Check your email' in selenium.page_source
