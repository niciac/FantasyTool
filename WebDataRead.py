
#Simple assignment
from selenium.webdriver import Safari
import time

driver = Safari()

# driver = webdriver.Safari("/Applications/Safari.app")
# driver = webdriver.Firefox("/Applications/Firefox.app")

driver.set_window_size(1000,600)
driver.get("http://fplstatistics.com/Home/Events")
print(driver.current_url)
time.sleep(10)
driver.quit()