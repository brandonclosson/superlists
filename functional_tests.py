from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		# User notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name("h1").text
		self.assertIn('To-Do', header_text)

		# User is invited to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# User type "Buy Peacock Feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		# User hits enter, the page updates, and page lists
		# "1: Buy peacock feathers" into a text box
		inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.test == '1: Buy peacock feathers' for row in rows)
		)

		# User sees another text box and is invited to add another item
		# User enters "Use peacock feathers to make a fly"
		self.fail('Finish the tests!')

		# The page lists both items

		# User sees that unique url was created for their lists

		# User visits that url and to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')