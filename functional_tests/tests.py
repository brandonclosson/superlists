from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

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
        list_one_url = self.browser.current_url
        self.assertRegex(list_one_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # User sees another text box and is invited to add another item
        # User enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page lists both items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # A second user come to the site

        ## Use a new browser session to make sure no info is coming through from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # User 2 visits the home page, there is no sign of User 1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # User 2 creates new list by entering new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # User 2 gets their own URL
        list_two_url = self.browser.current_url
        self.assertRegex(list_two_url, '/lists/.+')
        self.assertNotEqual(list_one_url, list_two_url)

        # Stil no trace of User 1's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        # User sees that unique url was created for their lists

        # User visits that url and to-do list is still there

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # User starts a new list and the input box is still centered
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

if __name__ == '__main__':
    unittest.main(warnings='ignore')