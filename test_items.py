import time

from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_exists(browser):
	browser.get(link)
	
	# Uncomment next line to pause test.
	#time.sleep(30)
	
	button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
	assert len(button) == 1, f'{len(button)} buttons was found. Should be exactly 1 button.'