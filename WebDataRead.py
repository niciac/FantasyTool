
# Importing Required Libraries
import os
import csv
import time
from selenium.webdriver import Safari
from bs4 import BeautifulSoup

# Function that writes input to a text file
def stringToTxtFile(data,filename,directory):
    dir = directory
    if os.path.exists(dir):
        os.chdir(dir)
    else:
        os.mkdir(dir)
        os.chdir(dir)
    print("Now saving in: ", os.getcwd())
    datafile = open("{a}.txt".format(a=filename),'w')
    datafile.write(data)
    datafile.close()
    os.chdir('..')
    print(os.getcwd())

# Setting Safari as the webdriver
driver = Safari()
# Opening safari driver and loading website
driver.set_window_size(1000,600)
driver.get("http://fplstatistics.com/Home/Events",)
print(driver.current_url)

# Get the webpage source code
content = driver.page_source

# Wait 5 seconds and close webdriver session
# time.sleep(1)
driver.quit()

# Extracting specific data from website
soup = BeautifulSoup(content,'html.parser')
