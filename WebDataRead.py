# Importing Required Libraries
import os
from datetime import date
from selenium.webdriver import Safari
from bs4 import BeautifulSoup

# Current date
today = date.today()
currentDate = today.strftime("%b_%d_%Y")

# Declaring array to save data in
dataArray = []
# Setting URL
url = "http://fplstatistics.com/Home/Events"

# Setting project directory as a global variable
projectDir = os.getcwd()

# Function that writes string input to a text file
def stringToTxtFile(data,filename,directory='textfiles'):
    global projectDir
    newDir = os.path.join(projectDir,directory)
    if os.path.exists(newDir):
        os.chdir(newDir)
    else:
        os.mkdir(newDir)
        os.chdir(newDir)
    print("Now saving in: ", os.getcwd())
    datafile = open(f"{filename}.txt",'w')
    datafile.write(data)
    datafile.close()
    os.chdir('..')
    print(os.getcwd())

# Setting Safari as the webdriver
driver = Safari()
# Opening safari driver and loading website
driver.set_window_size(1000,600)
driver.get(url)
print(driver.current_url)

# Get the webpage source code
content = driver.page_source

# print(time.gmtime)

# Wait 5 seconds and close webdriver session
# time.sleep(1)
driver.quit()

# Extracting specific data from website
soup = BeautifulSoup(content,'html.parser')

# for tr_tag in soup.find_all('tr'):
#     # print(type(tr_tag.text))
#     print(tr_tag.text)

# for td_tag in soup.find_all('td'):
    # print(type(td_tag.text))
    # print(td_tag.text)

print(len(soup.find_all('tr')))
for x in range(0,len(soup.find_all('tr'))):
    dataArray[x] = soup.find_all('tr')[x]

# for table_tag in soup.find_all('table'):
#     x = re.sub(r"([A-Z])", r" \1", table_tag.text).split()
#     # y = re.sub(r"\d", r" \1", x).split()
#     print('{}\n'.format(x))

stringToTxtFile(dataArray,currentDate)