from selenium import webdriver
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
		self.fail('Finish the tests!')

		# User is invited to enter a to-do item

		# User type "Buy Peacock Feathers" into a text box

		# User hits enter, the page updates, and page lists
		# "1: Buy peacock feathers" into a text box

		# User sees another text box and is invited to add another item
		# User enters "Use peacock feathers to make a fly"

		# The page lists both items

		# User sees that unique url was created for their lists

		# User visits that url and to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')