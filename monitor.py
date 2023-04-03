import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

options = Options()
options.add_experimental_option('detach', True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

url = 'https://fal-pure-x90-01.etisalat.corp.ae/dashboard'
username = *
psw = *
driver.get(url)

def main():
    login()
    find_values()
    write_to_notepad()
    

def login():
    # Clicking prereqs to login if any (advance, proceed, etc)
    try:
        driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
        driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
    except:
        pass

    # Logging in
    try:
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(psw)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.RETURN)     
    except:
        pass

def find_values():
    global system_value,  system_label, percent_value
    
    # Scraping relevant information 
    system_value = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'legend-value-container')))[0].text
    system_label = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'legend-unit')))[0].text
    percent_value = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'percent-used'))).text


def write_to_notepad():
    while(True):
        login() # To chk if it has to login due to page autologout, if true then logs in 
        find_values() # Refresh the values to stop from storing the same previous values
        now = datetime.now()
        min = now.strftime("%M")
        if 00 == int(min) or 30 == int(min) or 15 == int(min) or 45 == int(min):
            with open(r"D:\Temp\system_details.txt.txt", "a") as f:
                f.write(time.ctime() + " -> " + percent_value + '% @ ')
                f.write(system_value + system_label + "\n")
                
        time.sleep(60) # Repeating the process every 60 secs


if __name__ == "__main__":
    main()
