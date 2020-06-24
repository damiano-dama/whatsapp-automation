from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def whats_init(executable_path):
    # get chrome driver
    driver = webdriver.Chrome(executable_path)
    # open whatsapp
    driver.get('https://web.whatsapp.com')
    return driver

def whats_send(driver,cont_number,bar_lang='Search or start new chat'):
    # define wait timeout
    timeout_sec = 10
    wait = WebDriverWait(driver,timeout_sec)
    # search wanted contact
    searchBar = wait.until(EC.element_to_be_clickable\
                ((By.CSS_SELECTOR,'input[title="{}"]'.format(bar_lang))))
    time.sleep(0.5)
    searchBar.click()
    searchBar.send_keys(Keys.CONTROL,"a")
    searchBar.send_keys(Keys.DELETE)
    searchBar.send_keys(cont_number)
    # number may not have whatsapp, timeout exception if number not recognized
    time.sleep(0.5)
    timeout_sec = 2
    wait = WebDriverWait(driver,timeout_sec)
    contactBar = wait.until(EC.element_to_be_clickable\
                ((By.CSS_SELECTOR,'div[class="_3j7s9"]')))
    contactBar.click()
    
def write_msg_text(driver,msg):
    # define wait timeout
    timeout_sec = 10
    wait = WebDriverWait(driver,timeout_sec)
    # select editable textbox inside the chat
    editBox = wait.until(EC.element_to_be_clickable\
            ((By.XPATH,"//div[@contenteditable='true']")))
    # wtite message down
    editBox.send_keys(msg)
    # hit RETURN to send the message
    editBox.send_keys(Keys.RETURN)    

def close_whatsapp(driver):
    driver.quit()
