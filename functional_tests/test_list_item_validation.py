from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        
        # User goes to home page and accidentally tries to submit an empty list item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_new_item").send_keys('\n')
        
        # Home page refrehes and there is an error message saying it can't be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # User tries again with some text and it works
        self.browser.find_element_by_id("id_new_item").send_keys('Buy Milk\n')
        self.check_for_row_in_list_table('1: Buy Milk')

        # User tries to submit a second blank item
        self.browser.find_element_by_id("id_new_item").send_keys('\n')

        # User receives similar warning on their list
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # User corrects it by filling in text
        self.browser.find_element_by_id("id_new_item").send_keys('Make Tea\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        self.check_for_row_in_list_table('2: Make Tea')

if __name__ == '__main__':
    unittest.main(warnings='ignore')