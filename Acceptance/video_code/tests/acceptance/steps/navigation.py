from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome('/Users/jeffreydavisson/chromedriver')
    browser.get('http://127.0.0.1:5000')