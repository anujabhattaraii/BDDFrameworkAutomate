from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Opening browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.demo.guru99.com/test/newtours")
     
@when('Provide valid "{username}" and "{password}"')
def login(context, username, password):
    context.driver.find_element(By.NAME, "userName" ).send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()
    
@then('Verify title of the page')
def verify_title(context):
    assert context.driver.title == "Login: Mercury Tours"

@then('Verify success message')
def verify_success(context):
   try :
       text = context.driver.find_element(By.XPATH, "//h3[text()='Login Successfully']").text
   except:
       context.driver.close()
       assert False, "Test case failed"
       
   if text == "Login Sucessfully":
       context.driver.close()
       assert True , "Test case passed" 
