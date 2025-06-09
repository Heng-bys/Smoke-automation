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
    # Find and click on Scan tab
    scan_tab = wait.until(EC.element_to_be_clickable(
        (By.ID, "menu-scan")
    ))
    print("Found Scan tab, clicking...")
    scan_tab.click()

    scan_to_network_folder_tab = wait.until(EC.element_to_be_clickable((
        By.ID, "menu-scan-networkFolder"
    )))
    scan_to_network_folder_tab.click()

    check_and_handle_pin(driver, wait)

    time.sleep(1)

    #Click Default Folder tab
    default_folder_tab = wait.until(EC.element_to_be_clickable((
        By.ID, "mat-tab-label-0-1"
    )))
    default_folder_tab.click()

    #Click Default Network Folder Configuration
    default_nf_field = wait.until(EC.element_to_be_clickable((
        By.ID, "mat-select-value-15"
    )))
    default_nf_field.click()

    #Select option specify network folder
    network_folder_option = wait.until(EC.element_to_be_clickable((
        By.ID, "nvOption-specifyNetworkFolder"
    )))
    network_folder_option.click()

    #Input Display Name
    display_name = wait.until(EC.element_to_be_clickable((
        By.ID, "displayName"
    )))
    display_name.clear()
    display_name.send_keys("Heng")

    #Input UNC Folder path
    unc_path = wait.until(EC.element_to_be_clickable((
        By.ID, "folderPath"
    )))
    unc_path.clear()
    unc_path.send_keys(r"\\DESKTOP-Q4L1NOG\smoke_test")

    #Select Sign-In Method
    sign_in_method = wait.until(EC.element_to_be_clickable((
        By.ID, "mat-select-value-19"
    )))
    sign_in_method.click()

    #Select use the following credentials
    option_following_credentials = wait.until(EC.element_to_be_clickable((
        By.ID, "nvOption-alwaysUseCredential"
    )))
    option_following_credentials.click()

    #Input username
    nf_username = wait.until(EC.element_to_be_clickable((
        By.ID, "userName"
    )))
    nf_username.clear()
    nf_username.send_keys("network_tes")

    #Input password
    nf_password = wait.until(EC.element_to_be_clickable((
        By.ID, "password"
    )))
    nf_password.clear()
    nf_password.send_keys("1234")

    #Click apply button
    nf_apply = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-default-folder-options-button-apply"
    )))
    nf_apply.click()
    time.sleep(3)
    driver.refresh()
    # Edit username
    nf_username = wait.until(EC.element_to_be_clickable((
        By.ID, "userName"
    )))
    nf_username.clear()
    nf_username.send_keys("network_test")

    # Resubmit
    nf_apply = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-default-folder-options-button-apply"
    )))
    nf_apply.click()

    time.sleep(15)

except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
