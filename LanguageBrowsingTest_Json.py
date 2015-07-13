'''
Created on Jul 2, 2015

@author: Tim
'''
import unittest
import json
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from _codecs import encode
from idlelib.IOBinding import encoding

class LanguageBrowsingTest_Json(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
           
    def test_agegate_languages(self):
        
        def wait_for_page_load(self, timeout=30):
            old_page = self.driver.find_element_by_tag_name("html")
            yield 
            WebDriverWait(self.browser, timeout).until(staleness_of(old_page))
        
        print("test_agegate_languages")
        
      
        lang = {'english': ['VERIFY YOUR AGE', ".//*[@id='language-menu']/li[1]/a"], 
                'spanish': ['VERIFICA TU EDAD', ".//*[@id='language-menu']/li[3]/a"], 
                'german': ['BESTÄTIGE DEIN ALTER', ".//*[@id='language-menu']/li[5]/a"],
                'italian': ['INSERISCI LA TUA DATA DI NASCITA', ".//*[@id='language-menu']/li[7]/a"],
                'korean': ['연령 확인', ".//*[@id='language-menu']/li[9]/a"],
                'japanese': ['年齢認証', ".//*[@id='language-menu']/li[11]/a"],
                'chinese': ['確認您的年齡', ".//*[@id='language-menu']/li[13]/a"],
                'french': ['VÉRIFIER VOTRE ÂGE', ".//*[@id='language-menu']/li[15]/a"],
                'portuguese': ['VERIFIQUE SUA IDADE', ".//*[@id='language-menu']/li[17]/a"],
                'russian': ['ПРОВЕРКА ВОЗРАСТА', ".//*[@id='language-menu']/li[19]/a"]
                }
        
        
        driver = self.driver
        driver.get("http://gamechanger.evolvegame.com")
        
        JsonData  = json.dumps(lang, ensure_ascii=False)        
        
        with open('jsondata.txt', 'w', encoding='utf8') as outfile:
            json.dump(JsonData, outfile, ensure_ascii=False)
                        
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
    
