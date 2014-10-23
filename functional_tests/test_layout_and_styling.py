from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
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