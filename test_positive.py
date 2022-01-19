from selenium import webdriver
from Driver.driver import Base
import pytest
from Actions.contact_us import Contact_us
from time import sleep
import re

@pytest.mark.usefixtures('set_up')
class TestPozitive(Base):
    
    @pytest.mark.parametrize("cleared_value",[""])
    def test_clear_button(self,cleared_value):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("ABS","xyz@mail.ru","789","Armenia","ABS")
        message_item=element_list.message_fild("Hello There")
        clear_action=element_list.clear()
        sleep(3)
        for empty_value in clear_action:
            assert cleared_value==empty_value,"Not all fields are empty after clear action"

    @pytest.mark.parametrize("error_config",[("Feedback has been sent to the administrator")])   
    def test_submit_button(self,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("ABS","xyz@mail.ru","123","Armenia","ABS")
        message_item=element_list.message_fild("Hello there")
        submit_action=element_list.submit()
        sleep(3)
        error_mesega=element_list.find_err()
        if error_config==error_config[7]:
            assert error_config==error_mesega,"unsuccessful submit"