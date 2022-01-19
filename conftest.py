import pytest
import allure

@pytest.fixture
def error_config():
    name_empty="* This field is required"
    name_digit="No digit can be entered"
    email_invalid="* Invalid email address"
    phone_invalid="* Invalid phone number"
    phone_empty="* This field is required"
    country_numbers="No digits can be entered"
    message_more_180="Not more then 180 letters can be entered"
    succes_submit_message="Feedback has been sent to the administrator"
    return name_empty,name_digit,email_invalid,phone_invalid,phone_empty,country_numbers,message_more_180,succes_submit_message

