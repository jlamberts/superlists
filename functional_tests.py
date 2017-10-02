from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		#I go to my todo list to add a new item
		self.browser.get('http://localhost:8000')

		# Glancing at the top of the screen, I notice that the title and header of the webpage mentions "To-Do"
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# I'm immediately asked to enter an item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item')

		# I type "Work on homework" into the text box
		inputbox.send_keys('Work on homework')

		# I hit enter, and the page updates.  The list now contains "Work on homework" as its first item
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Work on homework' for row in rows),
			"New todo item did not appear in table"
			)

		
		# There's still a text box, and I enter "Clean Room"
		self.fail('Finish the test!')

		# The page updates and shows both items

		# I wonder whether this will store my list.  I then notice some text explaining that the page 
		# has generated a unique URL to store my list

		# I visit that URL and see my list

		# I go do other stuff

if __name__ == '__main__':
	unittest.main(warnings='ignore')