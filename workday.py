import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from getpass import getpass
import time

class Workday:
  def __init__(self, url):
    self.url = url
    self.profile = json.load(open('profile.json'))

    # Set up Selenium WebDriver
    self.driver = webdriver.Chrome()  # You need to have chromedriver installed
    self.wait = WebDriverWait(self.driver, 10)
    self.driver.maximize_window()

  def signup(self):
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='createAccountLink']")))
    button.click()
    time.sleep(10)

    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='email']").send_keys(self.profile['email'])
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='password']").send_keys(self.profile['password'])
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='verifyPassword']").send_keys(self.profile['password'])
    try:
      self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][data-automation-id='createAccountCheckbox']").click()
    except:
      print("Exception: 'There is no checkbox for signup'")
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-label='Create Account'][data-automation-id='click_filter']")))
    time.sleep(1)
    button.click()
    time.sleep(2)
    
  def signin(self):
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='email']").send_keys(self.profile['email'])
    self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][data-automation-id='password']").send_keys(self.profile['password'])
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-label='Sign In'][data-automation-id='click_filter']")))
    time.sleep(1)
    button.click()

  def fillform_page_1(self):
    # put radio button at the beginning as it sometimes goes to unclickable state
    self.driver.switch_to.active_element
    self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][data-uxi-element-id='radio_2']").click()

    try:
      self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='multiSelectContainer']").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='promptOption'][data-automation-label='Job Board']").click()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='promptOption'][data-automation-label='LinkedIn']").click()
      time.sleep(5)
    except:
      print("Exception: 'No Source selector'")
        
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstName']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstName']").send_keys(self.profile['first_name'])
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_lastName']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_lastName']").send_keys(self.profile['family_name'])
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstNameLocal']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstNameLocal']").send_keys(self.profile['first_name_local'])
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine1']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine1']").send_keys(self.profile['address_line_1'])
    
    try:
      self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine2']").clear()
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine2']").send_keys(self.profile['address_line_2'])
    except:
      print("Exception: 'No addressSection_addressLine2'")
    
    try:
      self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine3']").clear()
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine3']").send_keys(self.profile['address_line_3'])
    except:
      print("Exception: 'No addressSection_addressLine3'")
  
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_city']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_city']").send_keys(self.profile['address_city'])

    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").send_keys(self.profile['address_postal_code'])

    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").location_once_scrolled_into_view
    
    try:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='addressSection_countryRegion']").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, "//div[text()='Telangana']").click()
      time.sleep(2)
    except:
      print("Exception: 'No addressSection_countryRegion'")
    
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='phone-device-type']").click()
    time.sleep(5)
    self.driver.find_element(By.XPATH, "//div[text()='Mobile']").click()
    time.sleep(2)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='phone-number']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='phone-number']").send_keys(self.profile['phone_number'])
    time.sleep(2)
  
  def fillform_page_2(self):
    delete_work_experiences = self.driver.find_elements(By.CSS_SELECTOR, "button[data-automation-id='panel-set-delete-button']")
    i = 1
    while i <= len(delete_work_experiences):
      self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='panel-set-delete-button']").click()
      i = i+1
      time.sleep(1)
    
    for work_experience_index, work_experience in enumerate(self.profile['work_experiences']):
      if work_experience_index == 0:
        try:
          self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add Work Experience'][data-automation-id='Add']").click()
        except:
          print("Exception: 'Add button not found'")
      else:
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add Another Work Experience'][data-automation-id='Add Another']").click()
        
      time.sleep(2)
      work_experience_div = self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='workExperience-"+str(work_experience_index+1)+"']")
      work_experience.update({'div': work_experience_div})
      self.fill_work_experience(work_experience)
      time.sleep(2)
    
    resume_section = self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='resumeSection']")
    resume_section.location_once_scrolled_into_view
    time.sleep(2)
      
    delete_resumes = self.driver.find_elements(By.CSS_SELECTOR, "button[data-automation-id='delete-file']")
    i = 1
    while i <= len(delete_resumes):
      self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='delete-file']").click()
      i = i+1
      time.sleep(1)
    
    file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(self.profile['resume_path'])
    time.sleep(10)
    
    try:
      linkedin_question = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='linkedinQuestion']")
      linkedin_question.clear()
      linkedin_question.send_keys(self.profile['linkedin_question'])
    except:
      print("Exception: 'No Linkedin input'")
    
  def fillform_page_3(self):
    try:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][aria-label='Are you legally authorized to work in the country to which you are applying? select one required']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//div[text()='Yes']").click()
      time.sleep(2)
    except:
      print("Exception: 'Work Authorization already selected'")
    
    try:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][aria-label='Will you require sponsorship to continue and/or extend your current work authorization status? select one required']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//div[text()='No']").click()
      time.sleep(2)
    except:
      print("Exception: 'Visa Sponsorship already selected'")
    
  def fillform_page_4(self):
    try:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='gender']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//div[text()='Male']").click()
      time.sleep(2)
    except:
      print("Exception: 'Gender not present'")

    try:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='nationality']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//div[text()='India']").click()
      time.sleep(2)
    except:
      print("Exception: 'Nationality not present")

    agreement_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][data-automation-id='agreementCheckbox']")
    agreement_checkbox.location_once_scrolled_into_view
    agreement_checkbox.click()

  def fill_work_experience(self, work_experience):
    work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='jobTitle']").send_keys(work_experience['job_title'])
    work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='company']").send_keys(work_experience['company'])
    try:
      location = work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='location']")
      location.send_keys(work_experience['location'])
    except:
      print("Exception: 'no location field in experience'")
    work_experience['div'].find_element(By.CSS_SELECTOR, "textarea[data-automation-id='description']").send_keys(work_experience['role_description'])
    
    # location.location_once_scrolled_into_view
    
    start_date_div = work_experience['div'].find_element(By.CSS_SELECTOR, "div[data-automation-id='formField-startDate']")
    start_date_div.find_element(By.CSS_SELECTOR, "div[role='button'][data-automation-id='dateIcon']").click()
    time.sleep(2)
    month_picker = self.driver.find_element(By.CSS_SELECTOR, "span[data-automation-id='monthPickerSpinnerLabel']")
    while month_picker.text != work_experience['start_year']:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='monthPickerLeftSpinner']").click()
    self.driver.find_element(By.XPATH, "//label[text()='"+work_experience['start_month']+"']").click()
    
    end_date_div = work_experience['div'].find_element(By.CSS_SELECTOR, "div[data-automation-id='formField-endDate']")
    end_date_div.find_element(By.CSS_SELECTOR, "div[role='button'][data-automation-id='dateIcon']").click()
    time.sleep(2)
    month_picker = self.driver.find_element(By.CSS_SELECTOR, "span[data-automation-id='monthPickerSpinnerLabel']")
    while month_picker.text != work_experience['end_year']:
      self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='monthPickerLeftSpinner']").click()
    self.driver.find_element(By.XPATH, "//label[text()='"+work_experience['end_month']+"']").click()

  def click_next(self):
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='bottom-navigation-next-button']")))
    button.click()
    try:
      error_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='errorBanner']")
      print("Exception: 'Errors on page. Please resolve and submit manually. You have 60 seconds to do so!'")
      time.sleep(60)
    except:
      print("No Errors")
    time.sleep(10)
    
  def run(self):
    parsed_url = urlparse(self.url)
    company = parsed_url.netloc.split('.')[0]
    existing_company = company in self.profile['signedup_companies_list']
        
    self.driver.get(self.url) # Open a webpage
    time.sleep(5)
    
    # accept cookies
    try:
      button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='legalNoticeAcceptButton']")))
      button.click()
    except:
      print("Exception: 'No button for Cookies!")
    
    if existing_company:
      self.signin()
    else:
      self.signup()

    time.sleep(5)
    try:
      button = self.driver.find_element(By.CSS_SELECTOR, "a[role='button'][data-automation-id='applyManually']")
      button.click()
    except:
      print("NoSuchElementException")

    time.sleep(10)
    # self.fillform_page_1()
    self.click_next()
    
    self.fillform_page_2()
    self.click_next()
    
    self.fillform_page_3()
    self.click_next()
    
    self.fillform_page_4()
    self.click_next()
    
    # review and submit
    self.click_next()
    
    # Wait for 10 seconds
    time.sleep(60)

    # Close the browser
    self.driver.quit()

print("Please share Workday URL:")
url = str(input())

workday = Workday(url)
workday.run()