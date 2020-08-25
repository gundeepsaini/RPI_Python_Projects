
# Config variables
import Secrets_RPi.py


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


# Open browser and attempt login
def open_browser_login():   
    print(datetime.datetime.now(), "Startup")

    if RPi = True:
	    from selenium import webdriver
		driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')  # Optional argument, if not specified will search path.
	else:    
    	driver = Firefox()
    driver.get(url_vfs_news)

    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'global-fade-in')))
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'regional-fade-in')))            
        print(datetime.datetime.now(),"Page loaded")
        #print(element)
        return driver
    except Exception as e:
        print(datetime.datetime.now(), "Timeout on loading page", e)
        return driver
    
# Locate the news elements and serach for New Delhi
def search_keywords(driver):
    element = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.ID, 'global-fade-in')))
    Global_news = element.get_attribute('innerHTML')
    element = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.ID, 'regional-fade-in'))) 
    Regional_news = element.get_attribute('innerHTML')
    
    import bs4
    import re

    searched_word = 'Delhi'

    soup1 = bs4.BeautifulSoup(Global_news, 'html.parser')
    results1 = soup1.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    soup2 = bs4.BeautifulSoup(Regional_news, 'html.parser')
    results2 = soup2.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    
    return results1, results2


# Write results to file
def write_results_to_file(results1, results2):
    try:
        Global_file = open("VFS_Globalnews_file.txt","w")
        Global_file.write( str(results1) )
        Global_file.close()

        Regional_file = open("VFS_Regionalnews_file.txt","w")
        Regional_file.write( str(results2) )
        Regional_file.close()
    
    except Exception as e:
        print(datetime.datetime.now(), "Error writing to file", e)
        

# Read results from file
def read_results_from_files():
    dictionary1 = {}
    dictionary2 = {}
    try:
        import ast
        file = open("VFS_Globalnews_file.txt", "r")
        contents = file.read()
        dictionary1 = ast.literal_eval(contents)
        file.close()

        file = open("VFS_Regionalnews_file.txt", "r")
        contents = file.read()
        dictionary2 = ast.literal_eval(contents)
        file.close()

        return dictionary1, dictionary2

    except Exception as e:
        print(datetime.datetime.now(), "Error reading file", e)
        return dictionary1, dictionary2 

if __name__ == "__main__":
	
	while True:	    
	    dev = setup_notification_pb()
	    driver = open_browser_login()
	    results1, results2 = search_keywords(driver)
	    old_results1, old_results2 = read_results_from_files()


	    if old_results1 == results1 and old_results2 == results2:
	        print(datetime.datetime.now(),"Nothing new")
	    else:
	        print(datetime.datetime.now(),"Something changed for New Delhi!")
	        write_results_to_file(results1, results2)
	        #send notification to phone!
	        msg = "Check it here:" + url_vfs_news
	        #push = dev.push_note("VFS News Change @ New Delhi!!", msg)

	    print("----------------------------")
	    driver.quit()	    
	    time.sleep(60 * 60) # re-run every 1 hour

