from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from getpass import getpass
import time

COMPANY_LIST_SIGNEDUP = set(['verizon', 'gapinc', 'crowdstrike'])

class Workday:
  def __init__(self, url, email, password):
    self.url = url
    self.email = email
    self.password = password
    self.first_name = 'Raghu' # legalNameSection_firstName
    self.family_name = 'Boosetty' # legalNameSection_lastName
    self.first_name_local = self.first_name # legalNameSection_firstNameLocal
    self.address_line_1 = 'Narsingi' # addressSection_addressLine1
    self.address_city = 'Hyderabad' # addressSection_city
    self.address_postal_code = '500089' #addressSection_postalCode
    self.phone_number = '9177167375' # phone-number
    
    
    # Set up Selenium WebDriver
    self.driver = webdriver.Chrome()  # You need to have chromedriver installed
    self.wait = WebDriverWait(self.driver, 10)
  
  def signup(self):
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='createAccountLink']")))
    button.click()
    time.sleep(10)

    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='email']").send_keys(self.email)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='password']").send_keys(self.password)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='verifyPassword']").send_keys(self.password)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][data-automation-id='createAccountCheckbox']").click()
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-label='Create Account'][data-automation-id='click_filter']")))
    time.sleep(1)
    button.click()
    time.sleep(2)
    
  def signin(self):
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='email']").send_keys(self.email)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='password']").send_keys(self.password)
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-label='Sign In'][data-automation-id='click_filter']")))
    time.sleep(1)
    button.click()

  def fillform(self):
    self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][data-uxi-element-id='radio_2']").click()
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstName']").send_keys(self.first_name)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_lastName']").send_keys(self.family_name)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstNameLocal']").send_keys(self.first_name_local)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine1']").send_keys(self.address_line_1)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_city']").send_keys(self.address_city)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").send_keys(self.address_postal_code)
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='addressSection_countryRegion']").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "li[data-value='3cfc61cd0cf4100004b86c8483b80007'][role='option']").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='phone-device-type']").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "li[data-value='1d175767e01d1000aed4bd0115d70000'][role='option']").click()
    time.sleep(2)
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='bottom-navigation-next-button']")))
    button.click()
    
    time.sleep(10)
    
  def run(self):
    parsed_url = urlparse(self.url)
    company = parsed_url.netloc.split('.')[0]
    existing_company = company in COMPANY_LIST_SIGNEDUP
        
    self.driver.get(self.url) # Open a webpage
    time.sleep(5)
    
    if existing_company:
      self.signin()
    else:
      self.signup()

    time.sleep(5)
    button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[role='button'][data-automation-id='applyManually']")))
    button.click()
    
    time.sleep(10)
    self.fillform()
    
    # Wait for 10 seconds
    time.sleep(6)

    # Close the browser
    self.driver.quit()
    

print("Please share Workday URL:")
url = str(input())
print("Please share Workday Email for login/signup:")
email = 'raghu.boos@gmail.com' #str(input())
print("Please share Workday Password:")
password = 'Workdaylab@144' #getpass()

workday = Workday(url, email, password)
workday.run()