'''
Created on Jul 2, 2015

@author: Tim
'''
import unittest
import json
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of

class LanguageBrowsingTest_Json(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
           
    def test_agegate_languages(self):
        
        def wait_for_page_load(self, timeout=30):
            old_page = self.driver.find_element_by_tag_name("html")
            yield 
            WebDriverWait(self.browser, timeout).until(staleness_of(old_page))
        
        print("test_agegate_languages")
        print('loading data from jsondata.txt')
        
        jsonlang = json.load(codecs.open('jsondata.txt', 'r', 'utf-8-sig'))
        lang = json.loads(jsonlang)
        print(lang)
        
        for language in lang:
            print(language)
    
                
        driver = self.driver
        driver.get("http://gamechanger.evolvegame.com")
        
                        
        try:
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "ageheader")))
        finally:
            print("Wait timeout")
        
        for language in lang:
                    
            driver.find_element_by_xpath(lang[language][1]).click()
       
            driver.refresh()
            driver.implicitly_wait(15)             
               
            wait_for_page_load(self)
            
            print('Language: ' + language)
            print('Expected line: ' + lang[language][0])
            print('Actual line: ' + driver.find_element_by_class_name("ageheader").text)
            assert driver.find_element_by_class_name("ageheader").text == lang[language][0]
        
        
            
        
        
                
                
                
                
                
                
                
                
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
    
