from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		#I go to my todo list to add a new item
		self.browser.get('http://localhost:8000')

		# Glancing at the top of the screen, I notice that the title of the webpage mentions "To-Do"
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish this test')

		# I'm immediately asked to enter an iterm

		# I type "Work on homework" into the text box

		# I hit enter, and the page updates.  The list now contains "Work on homework" as its first item

		# There's still a text box, and I enter "Clean Room"

		# The page updates and shows both items

		# I wonder whether this will store my list.  I then notice some text explaining that the page 
		# has generated a unique URL to store my list

		# I visit that URL and see my list

		# I go do other stuff

if __name__ == '__main__':
	unittest.main(warnings='ignore')