from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.chrome.options import Options
# Replace below path with the absolute path 
# to chromedriver in your computer 
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options = chrome_options) 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = "'Jio836'"
input("All Loaded")
# Replace the below string with your own message 
string = f"Hi I'm Eliza. Rishabh's AI. He is on vacation. Please tell me about yourself."

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
group_title.click() 
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located(( 
#     By.XPATH, inp_xpath))) 
# for i in range(100): 
#     input_box.send_keys(string + Keys.ENTER) 
#     time.sleep(1) 
# msg_box = driver.find_element_by_class_name('selectablecopyable-text')
msg_box = driver.find_element_by_xpath("//div[@spellcheck='true']")

#for i in range(len(string)):
msg_box.send_keys(string)
    #driver.find_element_by_class_name('compose-btn-send').click()

sendButton = driver.find_element_by_xpath("//span[@data-icon='send']")
sendButton.click()


time.sleep(3)

driver.quit()

#alert_obj = driver.switch_to.alert
#alert_obj.accept() 