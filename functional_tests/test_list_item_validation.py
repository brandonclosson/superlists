from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally tries to submit an empty list item

        # Home page refrehes and there is an error message saying it can't be blank

        # User tries again with some text and it works

        # User tries to submit a second blank item

        # User receives similar warning on their list

        # User corrects it by filling in text

        self.fail("write me!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')