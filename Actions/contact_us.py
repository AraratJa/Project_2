from typing import Text
from locators.locators_feedback import Locators,Er_locators
from Driver.driver import Base


class Contact_us:
    def __init__(self,driver):
        self.driver=driver
        self.input=Locators.input_fields
        self.message=Locators.message_field
        self.submit_button=Locators.submit_button
        self.clear_button=Locators.clear_button
        self.Er_message=Er_locators.name_err

    def input_field(self,text_name,text_email,text_telephone,text_country,text_company):
        input_name=self.driver.find_elements_by_xpath(Locators.input_fields)
        
        for Element in input_name:
            Element_name=Element.get_attribute('name')
            
            if Element_name=="name":
                Element.send_keys(text_name)
            elif Element_name=="email":
                Element.send_keys(text_email)
            elif Element_name=="telephone":
                Element.send_keys(text_telephone)
            elif Element_name=="country":
                Element.send_keys(text_country)
                text_country_value=Element.get_attribute("value")
                try:
                    text_country_value==text_country
                except:
                    print("values does not much")
            elif Element_name=="company":
                Element.send_keys(text_company)
                text_company_value=Element.get_attribute("value")
                return text_company_value
            
            
    def message_fild(self,text_message):
        input_mess=self.driver.find_element_by_xpath(Locators.message_field)
        input_mess.send_keys(text_message)

    def submit(self):
        submit_but_ton=self.driver.find_element_by_xpath(Locators.submit_button)
        submit_but_ton.click()

    def clear(self):
        clear_but_ton= self.driver.find_element_by_xpath(Locators.clear_button)
        clear_but_ton.click()
        input_name=self.driver.find_elements_by_xpath(Locators.input_fields)
        input_mess=self.driver.find_element_by_xpath(Locators.message_field)
        lst=[]
        cleared_mesega_value=input_mess.get_attribute("value")
        lst.append(cleared_mesega_value)
        for input_values in input_name:
            cleared_values=input_values.get_attribute("value")
            lst.append(cleared_values)
                
        return lst

    def find_err(self):
        err_messagge=self.driver.find_element_by_class_name(Er_locators.name_err).text
        return err_messagge