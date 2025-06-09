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
    contacts_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Contacts')]")
    ))
    print("Found Contacts tab, clicking...")
    contacts_tab.click()

    check_and_handle_pin(driver, wait)

    click_ac_tab_by_name(driver, wait, "Contacts")
    add_contact = wait.until(EC.element_to_be_clickable((
        By.ID, "addContact-contacts"
    )))
    add_contact.click()
    time.sleep(3)
    display_name_input = wait.until(EC.element_to_be_clickable((
        By.ID, "displayName"
    )))
    display_name_input.clear()
    display_name_input.send_keys("heng")

    enable_nf = wait.until(EC.element_to_be_clickable((
        By.ID, "useNetworkFolder"
    )))
    enable_nf.click()

    nf_path = wait.until(EC.element_to_be_clickable((
        By.ID,"networkFolderPath"
    )))
    nf_path.clear()
    nf_path.send_keys(r"\\DESKTOP-Q4L1NOG\smoke_test")

    username_input = wait.until(EC.element_to_be_clickable((
        By.ID, "userName"
    )))
    username_input.clear()
    username_input.send_keys("network_test")

    password_input = wait.until(EC.element_to_be_clickable((
        By.ID, "password"
    )))
    password_input.clear()
    password_input.send_keys("1234")

    add_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-configure-contact-add-button-apply"
    )))
    add_button.click()
    time.sleep(2)
    address_book_tab = wait.until(EC.element_to_be_clickable((
        By.ID, "mat-tab-label-0-1"
    )))
    address_book_tab.click()

    enable_network_contact = wait.until(EC.element_to_be_clickable((
        By.ID, "enableNetworkContacts"
    )))
    enable_network_contact.click()
    ad_checkbox = wait.until(EC.element_to_be_clickable((
        By.ID, "address-books-checkbox-1"
    )))
    ad_checkbox.click()

    edit_button = wait.until(EC.element_to_be_clickable((
        By.ID, "edit-address-books"
    )))
    edit_button.click()

    LDAP_input = wait.until(EC.element_to_be_clickable((
        By.ID, "serverAddress"
    )))
    LDAP_input.clear()
    LDAP_input.send_keys("10.44.13.138")

    LDAP_authentication = wait.until(EC.element_to_be_clickable((
        By.ID, "serverRequiresAuthentication"
    )))
    LDAP_authentication.click()

    credentials = wait.until(EC.element_to_be_clickable((
        By.ID, "credentialType"
    )))
    credentials.click()
    ldap_credential_option = wait.until(EC.element_to_be_clickable((
        By.ID, "nvOption-simpleCredential"
    )))
    ldap_credential_option.click()

    ldap_username = wait.until(EC.element_to_be_clickable((
        By.ID, "userName"
    )))
    ldap_username.clear()
    ldap_username.send_keys(r"administrator@bys.uoa")

    ldap_pass = wait.until(EC.element_to_be_clickable((
        By.ID, "password"
    )))
    ldap_pass.clear()
    ldap_pass.send_keys("Tp123456")

    ldap_path = wait.until(EC.element_to_be_clickable((
        By.ID, "ldapPath"
    )))
    ldap_path.click()
    ldap_path.send_keys(Keys.CONTROL, 'a')  # Select all text
    ldap_path.send_keys(Keys.BACKSPACE)  # Delete selected text
    ldap_path.send_keys("dc=bys,dc=uoa")  # Send new value

    apply_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-address-book-edit-button-apply"
    )))
    apply_button.click()
    time.sleep(1)
    test_button = wait.until(EC.element_to_be_clickable((
        By.ID, "e110131b-be72-42e4-b3e6-cd4d18005314"
    )))
    test_button.click()
    criteria = wait.until(EC.element_to_be_clickable((
        By.ID, "criteria"
    )))
    criteria.clear()
    criteria.send_keys("winnie")

    click_test = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-test-address-book-button-apply"
    )))
    click_test.click()

    time.sleep(60)



except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
