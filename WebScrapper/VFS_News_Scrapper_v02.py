# Config variables
from Secrets_RPi import *

# Import Libs
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
import time


# Setup android notification service - pushbullet
def setup_notification_pb():
    # Setup pushbullet notification
    from pushbullet import Pushbullet
    pb = Pushbullet(pushbullet_API)
    #print(pb.devices)
    dev = pb.get_device(pushbullet_Device)
    #push = dev.push_note("Alert!!", "My msg...")
    return dev


# Sends notification - single point to disable in case of testing / errors
def send_notification_pb(msg):
    comment_to_disable = 0
    push = dev.push_note("VFS News Change @ New Delhi!!", msg)


# Open browser and attempt login
def open_browser_load1(url, xpath):
    print(datetime.datetime.now(), "Startup")

    if RPi == True:
        from selenium import webdriver
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver') 
    else:    
        driver = Firefox()
    driver.get(url)
    
    if(xpath != ""):
        try:            
            element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print(datetime.datetime.now(),"Page loaded")
            
            element_data = element.get_attribute('innerHTML')
            import bs4
            import re
            soup1 = bs4.BeautifulSoup(element_data, 'html.parser')
            #print(soup1)
            return driver, soup1
        
        except Exception as e:
            print(datetime.datetime.now(), "Timeout on loading page", e)
            soup1 = ""
            return driver, soup1        


# Write results to file
def write_results_to_data_file(data, file_no):
    file_name = "data_file_" + str(file_no) + ".txt"
    try:
        file = open(file_name,"w")
        file.write(str(data))
        file.close()
    
    except Exception as e:
        print(datetime.datetime.now(), "Error writing to file", e)           
    
    
# Read results from file
def read_results_from_data_file_1(file_no):    
    file_name = "data_file_" + str(file_no) + ".txt"
    try:
        from bs4 import BeautifulSoup    
        file = open(file_name, "r")
        contents = file.read()
        file.close()
        soup = BeautifulSoup(contents, "html.parser")
        return soup

    except Exception as e:
        print(datetime.datetime.now(), "Error reading file", e)
        soup = ""
        return soup  



if __name__ == "__main__":

    RPi = True   

    url_vfs_news2_element_class = "search-results-latest-updates js-news-search-results col-xs-12"
    url_vfs_news2_X_PATH = '//*[@id="content"]/div/div/div/div[3]/div/div[2]'    

    while True:     
        dev = setup_notification_pb()
        driver1, data1 = open_browser_load1(url=url_vfs_news2, 
                                            xpath=url_vfs_news2_X_PATH)
        old_data1 = read_results_from_data_file_1("101")

        if old_data1 == data1:
                print(datetime.datetime.now(),"Nothing new")
        else:
                print(datetime.datetime.now(),"Something changed!")
                write_results_to_data_file(data1, "101")
                #send notification to phone!
                msg = "Check it here:" + url_vfs_news2
                send_notification_pb(msg)

        driver1.quit()

        # re-run every x mins
        recheck_time_mins = 2 
        
        counter = 0        
        while counter < recheck_time_mins:
                print('-', end = '')
                counter += 1
                time.sleep(1*60) # Sleep for 1 min
        print("")
        