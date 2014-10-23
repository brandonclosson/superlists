from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        
        # User goes to home page and accidentally tries to submit an empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        # Home page refrehes and there is an error message saying it can't be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # User tries again with some text and it works
        self.get_item_input_box().send_keys('Buy Milk\n')
        self.check_for_row_in_list_table('1: Buy Milk')

        # User tries to submit a second blank item
        self.get_item_input_box().send_keys('\n')

        # User receives similar warning on their list
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # User corrects it by filling in text
        self.get_item_input_box().send_keys('Make Tea\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        self.check_for_row_in_list_table('2: Make Tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        self.get_item_input_box().send_keys('Buy wellies\n')

        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # User starts a new list that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # User starts typing to clear error message
        self.get_item_input_box().send_keys('a')

        # Error message is gone
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())

if __name__ == '__main__':
    unittest.main(warnings='ignore')