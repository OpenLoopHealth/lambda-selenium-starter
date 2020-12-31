from getChromeDriver import getChromeDriver
driver = getChromeDriver()

def lambda_handler(event, context):

	main(driver)

def main(driver):  

	driver.get("https://www.google.com")
	print("Page loaded successfully!")
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys('aquaponics')
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").click()
	print("Searching Google for all things aquaponics..")
    links = driver.find_elements_by_xpath("//a[@href]")
    print("I've found all the links for aquaponics on the first page of Google!")
