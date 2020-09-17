from getChromeDriver import getChromeDriver
driver = getChromeDriver()

def lambda_handler(event, context):

	main(driver)

def main(driver): 	#write your function here 

	#NOTE: be sure to pass in the driver argument into any functions you create that require chrome driver  

	driver.get("https://www.google.com")
	print("Page loaded successfully!")
	print(driver.current_url)