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
driver.get("http://10.44.15.147/index.html")

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

    #Click Enable LDAP Sign-In button
    enable_button = wait.until(EC.element_to_be_clickable((
        By.ID, "enableLdap"
    )))
    enable_button.click()

    #Input LDAP server address
    address_field = wait.until(EC.element_to_be_clickable((
        By.ID, "serverAddress"
    )))
    address_field.clear()
    address_field.send_keys("10.44.13.138")

    #Input LDAP username
    ldap_username_input = wait.until(EC.element_to_be_clickable((
        By.ID, "userName"
    )))
    ldap_username_input.clear()
    ldap_username_input.send_keys("administrator@bys.uoa")

    #Input LDAP password
    ldap_password_input = wait.until(EC.element_to_be_clickable((
        By.ID, "userPassword"
    )))
    ldap_password_input.clear()
    ldap_password_input.send_keys("Tp123456")

    #Input LDAP root
    ldap_root_input = wait.until(EC.element_to_be_clickable((
        By.ID, "ldapBindRoots"
    )))
    ldap_root_input.clear()
    ldap_root_input.send_keys("dc=bys,dc=uoa")

    #Input LDAP match name
    ldap_match_name = wait.until(EC.element_to_be_clickable((
        By.ID, "matchLdapNameAttribute"
    )))
    ldap_match_name.clear()
    ldap_match_name.send_keys(("sAMAccountName"))

    #Input LDAP group attribute
    ldap_group_attribute = wait.until(EC.element_to_be_clickable((
        By.ID, "retrieveLdapGroupAttribute"
    )))

    #Click apply button
    ldap_apply_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-applyConfig-button-apply"
    )))
    ldap_apply_button.click()
    time.sleep(2)

    #Click test button
    ldap_test_button = wait.until(EC.element_to_be_clickable((
        By.ID, "ldap-test-button"
    )))
    ldap_test_button.click()
    time.sleep(2)
    #Input test username
    ldap_test_username = wait.until(EC.element_to_be_clickable((
        By.ID, "userId"
    )))
    ldap_test_username.clear()
    ldap_test_username.send_keys("winnie")

    #Input test password
    ldap_test_password = wait.until(EC.element_to_be_clickable((
        By.ID, "password"
    )))
    ldap_test_password.clear()
    ldap_test_password.send_keys("admin@123")

    #Click test button
    test_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-ldap-test-footer-button-apply"
    )))
    test_button.click()
    time.sleep(2)

    #Click done button
    done_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-test-ldap-user-button-ok"
    )))
    done_button.click()

    # Click Test button again for wrong credentials
    ldap_test_button.click()

    # Re-locate and input test username
    ldap_test_username = wait.until(EC.element_to_be_clickable((By.ID, "userId")))
    ldap_test_username.clear()
    ldap_test_username.send_keys("hehe")

    # Re-locate and input test password
    ldap_test_password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    ldap_test_password.clear()
    ldap_test_password.send_keys("hehe")

    # Click test
    test_button = wait.until(EC.element_to_be_clickable((By.ID, "footer-ldap-test-footer-button-apply")))
    test_button.click()
    time.sleep(2)

    #Click done button
    done_button = wait.until(EC.element_to_be_clickable((
        By.ID, "footer-test-ldap-user-button-ok"
    )))
    done_button.click()

    time.sleep(15)

except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
