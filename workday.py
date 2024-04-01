from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    
    # fillform_page_1
    self.first_name = 'Raghu' # legalNameSection_firstName
    self.family_name = 'Boosetty' # legalNameSection_lastName
    self.first_name_local = self.first_name # legalNameSection_firstNameLocal
    self.address_line_1 = 'NCC Urban One' # addressSection_addressLine1
    self.address_line_2 = 'Narsingi' # addressSection_addressLine2
    self.address_line_3 = 'Kokapet' # addressSection_addressLine3
    self.address_city = 'Hyderabad' # addressSection_city
    self.address_postal_code = '500089' #addressSection_postalCode
    self.phone_number = '9177167375' # phone-number
    
    # fillform_page_2
    self.work_experiences = {
      'Amazon': {
        'company': 'Amazon',
        'start_year': '2022', 
        'start_month': 'Aug', 
        'end_year': '2023',  
        'end_month': 'Oct',
        'job_title': 'Software Development Manager', # jobTitle
        'location': 'Hyderabad',
        'role_description': "Completed the migration of one of the key projects in the data platform team to standardize the transport requests from 300+ clients. It involved the migration of the datastore from Sable to DynamoDB and orchestrating the application to 3 different microservices. Achieved this with a team of 12. Additionally, I’ve mentored 7 interns."
        },
      'Copart': {
        'company': 'Copart',
        'start_year': '2019', 
        'start_month': 'Feb', 
        'end_year': '2022',  
        'end_month': 'Aug',
        'job_title': 'Engineering Manager', # jobTitle
        'location': 'Hyderabad',
        'role_description': "Delivered five projects four of them from scratch. An insurance portal project for Germany was delivered in a record one month. Built Claims Hub Portal - a total loss claims system for the UK’s first in the market, with a team of 5. Recognized here. Created a portal Virtual Walkthrough - that helps streamline the process of going to auction for vehicles, with a team of 3. Now used by an in-house team of 300. As a lead, contributions to the company’s biggest projects for Title transfer in the US helped reduce the overall lot life cycle time by 50%."
        },
      'beckNF Technologies': {
        'company': 'beckNF Technologies',
        'start_year': '2018', 
        'start_month': 'May', 
        'end_year': '2019',  
        'end_month': 'Jan',
        'job_title': 'Co-Founder & CTO', # jobTitle
        'location': 'Hyderabad',
        'role_description': "I built an in-house product (LEAST), an online collaboration tool that helps organizations increase productivity. The end-to-end product was developed in less than 6 months, with a team of 8, mostly freshers."
        },
      'RubyEffect Software Solutions': {
        'company': 'RubyEffect Software Solutions',
        'start_year': '2010', 
        'start_month': 'Sep', 
        'end_year': '2018',  
        'end_month': 'Apr',
        'job_title': 'Principal Software Engineer & CTO', # jobTitle
        'location': 'Hyderabad',
        'role_description': "Advanced through several promotions over the years. Played a major role in the company’s growth and expansion. Successfully delivered about 30 projects in 8 years, by coding, managing a team, and meeting deadlines. Architected the back end and server configuration for most projects in the company. I fine-tuned the performance of microsites of a large-scale US-based parking application ParkMobile. Improved the microsite load times by 50-60%, by fixing the memory leaks. Single-handedly designed and upgraded the entire server infrastructure from Heroku to AWS for FindMeACard, using VPC, Auto-Scaling, ALB, CloudFront, S3, RDS, Route53, and CodeDeploy. Integrated payment gateway, built call sites, and the brand alerts feature for Brandrep Integrated full-text search into applications with gems like Elasticsearch, Searchify, and Searchkick in Rails."
        },
      'Teqnium Consultancy Services': {
        'company': 'Teqnium Consultancy Services',
        'start_year': '2009', 
        'start_month': 'Aug', 
        'end_year': '2010',  
        'end_month': 'Apr',
        'job_title': 'Software Engineer', # jobTitle
        'location': 'Hyderabad',
        'role_description': "Worked on e-learning content development. Integrating templates/mockups given in PSD to Flash with ActionScript 2 and 3. Converting executables with the SWFs."
        },
    }
    self.linkedin_question = 'https://www.linkedin.com/in/raghuboosetty/' # linkedinQuestion
    self.resume_path = '/Users/raghuboosetty/Documents/Workspace/python/workday/RaghuBoosetty.pdf'
    
    # Set up Selenium WebDriver
    self.driver = webdriver.Chrome()  # You need to have chromedriver installed
    self.wait = WebDriverWait(self.driver, 10)
    self.driver.maximize_window()

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

  def fillform_page_1(self):
    # put radio button at the beginning as it sometimes goes to unclickable state
    self.driver.switch_to.active_element
    self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][data-uxi-element-id='radio_2']").click()
    # radio = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][data-uxi-element-id='radio_2']")
    # radio.find_element(By.XPATH, 'parent::*').click()
    # self.driver.find_element(By.XPATH, "//div[data-automation-id='previousWorker']/div/label[text()='No']").click()
    # self.driver.find_element(By.XPATH, "//label[text()='No']").click()
    
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
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstName']").send_keys(self.first_name)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_lastName']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_lastName']").send_keys(self.family_name)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstNameLocal']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='legalNameSection_firstNameLocal']").send_keys(self.first_name_local)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine1']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine1']").send_keys(self.address_line_1)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine2']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine2']").send_keys(self.address_line_2)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine3']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_addressLine3']").send_keys(self.address_line_3)
  
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_city']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_city']").send_keys(self.address_city)

    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='addressSection_postalCode']").send_keys(self.address_postal_code)

    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='addressSection_countryRegion']").click()
    time.sleep(5)
    self.driver.find_element(By.XPATH, "//div[text()='Telangana']").click()
    time.sleep(2)
    
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='phone-device-type']").click()
    time.sleep(5)
    self.driver.find_element(By.XPATH, "//div[text()='Mobile']").click()
    time.sleep(2)
    
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='phone-number']").clear()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='phone-number']").send_keys(self.phone_number)
    time.sleep(2)
  
  def fillform_page_2(self):
    delete_work_experiences = self.driver.find_elements(By.CSS_SELECTOR, "button[data-automation-id='panel-set-delete-button']")
    i = 1
    while i <= len(delete_work_experiences):
      self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='panel-set-delete-button']").click()
      i = i+1
      time.sleep(1)
    
    for work_experience_index, work_experience in enumerate(self.work_experiences):
      if work_experience_index == 0:
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add Work Experience'][data-automation-id='Add']").click()
      else:
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add Another Work Experience'][data-automation-id='Add Another']").click()
        
      time.sleep(2)
      work_experience_div = self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='workExperience-"+str(work_experience_index+1)+"']")
      self.work_experiences[work_experience].update({'div': work_experience_div})
      self.fill_work_experience(self.work_experiences[work_experience])
      time.sleep(2)
    
    skill_prompt = self.driver.find_element(By.CSS_SELECTOR, "div[data-automation-id='formField-skillsPrompt']")
    skill_prompt.location_once_scrolled_into_view
    time.sleep(2)
      
    delete_resumes = self.driver.find_elements(By.CSS_SELECTOR, "button[data-automation-id='delete-file']")
    i = 1
    while i <= len(delete_resumes):
      self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='delete-file']").click()
      i = i+1
      time.sleep(1)
    
    file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(self.resume_path)
    time.sleep(10)
    
    linkedin_question = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='linkedinQuestion']")
    linkedin_question.clear()
    linkedin_question.send_keys(self.linkedin_question)
    
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
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='gender']").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//div[text()='Male']").click()
    time.sleep(2)
  
    self.driver.find_element(By.CSS_SELECTOR, "button[type='button'][data-automation-id='nationality']").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//div[text()='India']").click()
    time.sleep(2)
    
    agreement_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][data-automation-id='agreementCheckbox']")
    agreement_checkbox.location_once_scrolled_into_view
    agreement_checkbox.click() 

  def fill_work_experience(self, work_experience):
    work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='jobTitle']").send_keys(work_experience['job_title'])
    work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='company']").send_keys(work_experience['company'])
    location = work_experience['div'].find_element(By.CSS_SELECTOR, "input[type='text'][data-automation-id='location']")
    location.send_keys(work_experience['location'])
    work_experience['div'].find_element(By.CSS_SELECTOR, "textarea[data-automation-id='description']").send_keys(work_experience['role_description'])
    
    location.location_once_scrolled_into_view
    
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
    time.sleep(10)
    
  def run(self):
    parsed_url = urlparse(self.url)
    company = parsed_url.netloc.split('.')[0]
    existing_company = company in COMPANY_LIST_SIGNEDUP
        
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
    # button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[role='button'][data-automation-id='applyManually']")))
    try:
      button = self.driver.find_element(By.CSS_SELECTOR, "a[role='button'][data-automation-id='applyManually']")
      button.click()
    except:
      print("NoSuchElementException")

    time.sleep(10)
    self.fillform_page_1()
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
print("Please share Workday Email for login/signup:")
email = 'raghu.boos@gmail.com' #str(input())
print("Please share Workday Password:")
password = 'Workdaylab@144' #getpass()

workday = Workday(url, email, password)
workday.run()