# Python script to apply for jobs on Workday

The Python script to apply for the jobs that are on Workday using the Selenium library and Chrome web driver.

## Config
1. _config/profile.yaml_ - Has all the details related to your profile, you can clone it and change the creds(_email_, _password_, etc..) and other details as per your need
2. _config/Resume.pdf_ - That's the resume that you need to replace with yours and update _resume_path_ in _config/profile.yaml_ file

## Prerequisites
> $ python3 -m pip install --upgrade pip
> 
> $ python3 -m pip install --upgrade pip setuptools wheel
> 
> $ python3 -m pip install "ipdb"
> 
> $ python3 -m pip install "pyyaml"

## How to Run the script
> $ python3 workday.py
> 
> $ Please share the Workday URL:
>

#### Example Job URL 
[https://gapinc.wd1.myworkdayjobs.com/GAPINC/job/Spoke---Hyderabad/Software-Engineer_R164023/apply?source=JB-10340](https://gapinc.wd1.myworkdayjobs.com/GAPINC/job/Spoke---Hyderabad/Software-Engineer_R164023/apply?source=JB-10340)

## Notes
1. Some workday jobs have few additional mandatory fields in which case the submit may fail but the code rescues it and waits for 60 seconds for the user to manually **fix** the errors and **_Submit_** the form. Please note that if the errors are not fixed manually then the script will eventually fail.
2. If you run the script again for some reason then it clears all the fields and then adds the information from the _config/profile.yaml_ file. So, please don't assume that it would start from the step where it failed when you re-run the script.
3. If you want to skip the steps then go to the '_def run_' method in _workday.py_ and comment out the '_fillform_page_1_' or '_fillform_page_2_' or whichever step you want to skip.
4. For debugging insert this code '**_ipdb.set_trace()_**' at whichever needed.

## Background
There are too many companies that are using Workday as their job board. I have seen that the pattern for all these jobs is 90% similar, and applying on Workday is a real pain in the a**. 
It mandates you to log in which requires signup and it never segregates the candidate's profile, your profile is limited to a company and is not carried forward to any other company. Not sure why all MNCs are onboarding to Workday. 

I have thought to put my profile in a JSON file and apply to all the jobs through a Python script. So far, it worked for me like a charm. 

If you too think it benefits you then please feel free to use and suggest any modifications.
