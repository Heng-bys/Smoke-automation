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
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to handle SSL certificate errors
chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--incognito")

# Initialize Chrome driver with the updated approach
service = Service("C:\\Program Files (x86)\\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
driver.get("http://10.44.15.202/index.html")

wait = WebDriverWait(driver, 10)



try:
    # Find and click on the Security tab
    security_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Security')]")
    ))
    print("Found Security tab, clicking...")
    security_tab.click()

    certificate_management_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Certificate Management')]")
    ))
    print("Found Certificate Management tab, clicking...")
    certificate_management_tab.click()

    check_and_handle_pin(driver, wait)

    #Select self-signed certificate checkbox
    self_signed_certificate = wait.until(EC.element_to_be_clickable((
        By.ID, "certificate-management-checkbox-1"
    )))
    self_signed_certificate.click()

    #Click view button
    view_button = wait.until(EC.element_to_be_clickable(
        (By.ID, "view-certificate-management")
    ))
    view_button.click()
    time.sleep(15)

    #Click ok button
    ok_button = wait.until(EC.element_to_be_clickable((
        (By.ID, "status-dialog-ok-button")
    )))
    ok_button.click()

    #Select self-signed certificate checkbox
    self_signed_certificate = wait.until(EC.element_to_be_clickable((
        By.ID, "certificate-management-checkbox-1"
    )))
    self_signed_certificate.click()

    #Delete self-signed certificate
    delete_button = wait.until(EC.element_to_be_clickable((
        By.ID, "delete-certificate-management"
    )))
    delete_button.click()

    #Confirm delete
    confirm_delete_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-confirm-delete-certificates-button-apply"
    )))
    confirm_delete_button.click()

    #Delete ok
    finish_delete = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-confirm-delete-certificates-button-apply"
    )))

    finish_delete.click()

    #Click create tab
    create_tab = wait.until(EC.element_to_be_clickable((
        By.ID, "mat-tab-label-0-1"
    )))
    create_tab.click()

    time.sleep(5)

    #Click next button
    next_button = wait.until(EC.element_to_be_clickable((
        By.ID, "cert-next"
    )))
    next_button.click()

    time.sleep(3)

    #Click create button
    create_button = wait.until(EC.element_to_be_clickable((
        By.ID, "cert-next"
    )))
    create_button.click()

    time.sleep(5)

    #Click ok
    create_ok_button = wait.until(EC.element_to_be_clickable((
        By.ID, "cert-next"
    )))
    create_ok_button.click()

    time.sleep(60)

except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
