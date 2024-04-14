import yaml
import ipdb

class Config:
  def __init__(self, file):
    self.file = file

  def read_companies(self):
    companies_file = open(self.file, 'r')
    company_subdomains = []
    for company_subdomain in companies_file:
      company_subdomains.append(company_subdomain.strip())
    companies_file.close()
    return company_subdomains

  def write_company(self, company_subdomain):
    company_subdomains = self.read_companies()
    if company_subdomain in company_subdomains:
      return
    companies_file = open(self.file, 'a+')
    companies_file.writelines("\n"+company_subdomain)
    companies_file.close()

  def load_profile(self):
    with open(self.file) as profile_file:
      profile = yaml.safe_load(profile_file)
    return profile