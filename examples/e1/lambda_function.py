import time
import os
from dotenv import load_dotenv
from getChromeDriver import getChromeDriver

driver = getChromeDriver()
load_dotenv()
USERNAME = os.getenv("SITE_USERNAME")
PASSWORD = os.getenv("SITE_PASSWORD")

urls = {
    'login': 'https://www.examplesite.com/login',
    'jobs': 'https://www.examplesite.com/jobs'
}

def lambda_handler(event, context):

    main(driver)

def main(driver):

    print("Logging in..")
    driver.get(urls.get('login'))
    time.sleep(0.5)
    driver.find_element_by_id('email').send_keys(USERNAME)
    driver.find_element_by_id('passwd').send_keys(PASSWORD)
    driver.find_element_by_xpath("//input[@name='btn_login']").click()
    time.sleep(0.5)
    print("Logged in!")
    print("Refreshing jobs..")
    driver.get(urls.get('jobs'))
    time.sleep(0.5)
    driver.find_element_by_xpath("//a[@href='#']").click()
    print("All jobs refreshed successfully! Nicely done!")
    driver.quit()