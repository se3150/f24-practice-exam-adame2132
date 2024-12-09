from behave import when, then, given
from selenium.webdriver.common.by import By
import time

@given('I open the url "{url}"')
def step_go_to_url(context, url):
    context.behave_driver.get(url)

@when('I enter "{value}" in the text feild "{id}"')
def step_entering_value_for_triangle(context, value, id):
    text_field = context.behave_driver.find_element(By.ID, id)
    text_field.send_keys(value)
@when('I click on the button "{btn}"')
def step_to_click_btn(context, btn):
    calBtn = context.behave_driver.find_element(By.CLASS_NAME, btn)
    calBtn.click()
    time.sleep(2)
@then('I should see "{area}" in "{id}"')
def step_testing_if_area_is_correct(context, area, id):
    answer = context.behave_driver.find_element(By.ID, id).get_attribute("value").strip()
    
    # Assert the displayed result matches the expected
    assert answer == area, f"Expected '{area}', but got '{answer}'"