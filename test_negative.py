from selenium import webdriver
from Driver.driver import Base
import pytest
from Actions.contact_us import Contact_us
from time import sleep
import re

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    
    @pytest.mark.parametrize("text_name",[(""),("At789")])
    def test_name_field(self,text_name,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        el_item=element_list.input_field(text_name,"abs@mail.ru","789","Armenia","ABD")
        message_item=element_list.message_fild("Hello there")
        submit_action=element_list.submit()
        
        sleep(3)
        
        error_mesega=element_list.find_err()
        if len(text_name)==0:
            assert error_mesega==error_config[0],"No message displayed about empty field"
        else:
            assert error_mesega==error_config[1],"No message displayed about digits in name field"

    @pytest.mark.parametrize("text_email",[("fgfgf"),("")])   
    def test_email_valid(self,text_email,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("Garnik",text_email,"789","Armenia","ABS")
        message_item=element_list.message_fild("Hello there")
        submit_action=element_list.submit()
        sleep(3)
        error_mesega=element_list.find_err()
        
        if "@" not in text_email and len(text_email)>0:
            assert error_mesega==error_config[2],"No message displayed about invalid email"
        elif len(text_email)==0:
            assert error_config[0] in error_mesega,"No message displayed about empty field"

    @pytest.mark.parametrize("text_telephone",[("fgfgf"),("")])   
    def test_telephone_valid(self,text_telephone,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("ABC","xyz@mail.ru",text_telephone,"Armenia","ABS")
        message_item=element_list.message_fild("Hello there")
        submit_action=element_list.submit()
        sleep(3)
        error_mesega=element_list.find_err()
        if re.search('[a-zA-Z]', text_telephone) and len(text_telephone)>0:
            assert error_mesega==error_config[3],"No message displays about invalid phone number form"
        if len(text_telephone)==0:
            assert error_config[0] in error_mesega,"No message displayed about empty field"   

    @pytest.mark.parametrize("text_country",[("fgfgf667"),("567")])   
    def test_country_valid(self,text_country,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("ABS","xyz@mail.ru","789",text_country,"ABS")
        message_item=element_list.message_fild("Hello there")
        submit_action=element_list.submit()
        sleep(3)
        error_mesega=element_list.find_err()
        for char in text_country:
            if char.isdigit():
                assert error_mesega==error_config[5],"No message displayed about non aceptable digits in country field"

    @pytest.mark.parametrize("text_message",[("x"*181),("")])   
    def test_message_field(self,text_message,error_config):
        driver=self.driver
        element_list=Contact_us(driver)
        El_item=element_list.input_field("ABS","xyz@mail.ru","789","Armenia","ABS")
        message_item=element_list.message_fild(text_message)
        submit_action=element_list.submit()
        sleep(3)
        error_mesega=element_list.find_err()
        if len(text_message)>180:
            assert error_mesega==error_config[6],"more then 180 letters can be entered in message field"

     
    