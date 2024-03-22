from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Start browser')
def step_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.demo.guru99.com/test/newtours")

@when('Verify login by using below query')
def step_imp(context):
    for r in context.table:
        context.driver.find_element(By.NAME, "userName" ).send_keys(r["userName"])
        context.driver.find_element(By.NAME, "password").send_keys(r["password"])
        context.driver.find_element(By.NAME, "submit").click()
        