from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

url = "https://www.fnb.co.za/"

user = "SimoneStrydom5"
secureword = "Dan0115"
account = "FNB Gold Cheque Account" #,"FNB Premier Credit Card"]

driver.get(url)

time.sleep(2)   

# Entire site
username = driver.find_element_by_id("user")
username.clear()
username.send_keys(user)
password = driver.find_element_by_id("pass")
password.clear()
password.send_keys(secureword)
submit = driver.find_element_by_id("OBSubmit")
submit.click()
time.sleep(10)

# Go to accounts page
accounts_page = driver.find_element_by_css_selector(".shortCutLink:nth-child(1)")
accounts_page.click()
time.sleep(10)

# Go to accounts page
account_page = driver.find_element_by_xpath("// a[contains(text(),\'" + account + "')]")
account_page.click()
time.sleep(10)

# Go to transaction history page
transaction_history_button = driver.find_element_by_id("transactionHistory")
transaction_history_button.click()
time.sleep(10)

# Identify first and last element in transaction history table
# determine if they are at least a month seperated or always load all transaction
# from the 23 to 23.
