from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('open browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.demo.guru99.com/test/newtours")
     
@when('providing valid username and password')
def validUserNameAndPassword(context):
    context.driver.find_element(By.NAME, "userName" ).send_keys("mercury")
    context.driver.find_element(By.NAME, "password").send_keys("mercury")
    context.driver.find_element(By.NAME, "submit").click()
    
@then('Verifying home')
def verify_home(context):
    assert context.driver.title == "Login: Mercury Tours"