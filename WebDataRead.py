
# Importing Required Libraries
import csv
import time
from selenium.webdriver import Safari
from bs4 import BeautifulSoup

# Setting Safari as the webdriver
driver = Safari()

driver.set_window_size(1000,600)
driver.get("http://fplstatistics.com/Home/Events")
# print(driver.current_url)

# Get the webpage source code
content = driver.page_source
# print(content)

# # Write source code into text file
# datafile = open("data.txt",'w')
# datafile.write(content)
# datafile.close()

# Extracting specific data from website
soup = BeautifulSoup(content)
# print(soup.prettify())
# print(soup.get_text()) # returns just text but might make it more difficult to use the data
print(soup.find_all('role="row"'))

# Wait 5 seconds and close webdriver session
time.sleep(5)
driver.quit()

