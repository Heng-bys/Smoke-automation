from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from common.PIN_detection import check_and_handle_pin
from common.Click_AC_Tab_By_Name import click_ac_tab_by_name

# Set up Chrome options to handle SSL certificate errors
chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--incognito")

# Initialize Chrome driver with the updated approach
service = Service("C:\\Program Files (x86)\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
driver.get("http://10.44.15.120/index.html")

wait = WebDriverWait(driver, 10)



try:
    # Find and click on the Security tab
    security_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Security')]")
    ))
    print("Found Security tab, clicking...")
    security_tab.click()

    access_control_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Access Control')]")
    ))
    print("Found Access Control tab, clicking...")
    access_control_tab.click()

    check_and_handle_pin(driver, wait)

    click_ac_tab_by_name(driver, wait, "LDAP Setup")


except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
