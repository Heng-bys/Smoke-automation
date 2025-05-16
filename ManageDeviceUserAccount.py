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


def create_user(driver, wait, username, display_name, password, role):
    try:
        plus_icon = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//mat-icon[@aria-label='Add']"
        )))
        plus_icon.click()

        username_input = wait.until(EC.element_to_be_clickable((By.ID, "userId")))
        username_input.clear()
        username_input.send_keys(username)
        print(f"Entered Username: {username}")

        display_name_input = wait.until(EC.element_to_be_clickable((By.ID, "displayName")))
        display_name_input.clear()
        display_name_input.send_keys(display_name)
        print(f"Entered Display Name: {display_name}")

        dropdown = wait.until(EC.element_to_be_clickable((By.ID, "permissionSet")))
        dropdown.click()

        option = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//mat-option//span[normalize-space(text())='{role}']"
        )))
        option.click()
        print(f"Selected Role: {role}")

        new_password_input = wait.until(EC.element_to_be_clickable((By.ID, "newPassword")))
        new_password_input.clear()
        new_password_input.send_keys(password)

        confirm_password_input = wait.until(EC.element_to_be_clickable((By.ID, "confirmPassword")))
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)
        print("Entered Password fields.")

        add_button = wait.until(EC.element_to_be_clickable((
            By.ID, "footer-configure-device-user-add-button-apply"
        )))
        add_button.click()
        print("Clicked Add to submit user.")
        time.sleep(2)

    except Exception as e:
        print(f"Error creating user: {e}")
        driver.save_screenshot('error_screenshot.png')
        raise


try:
    # Navigate through the UI
    security_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Security')]")))
    print("Found Security tab, clicking...")
    security_tab.click()

    access_control_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Access Control')]")))
    print("Found Access Control tab, clicking...")
    access_control_tab.click()

    check_and_handle_pin(driver, wait)
    click_ac_tab_by_name(driver, wait, "Printer User Accounts")

    # Use the helper function
    create_user(driver, wait, "user", "user", "user@123", "Printer User")
    time.sleep(5)
    create_user(driver, wait, "admin", "admin", "admin@123", "Device Administrator")
    time.sleep(5)


    def edit_user(driver, wait, index, new_role, current_password):
        try:
            # Select the user checkbox by index
            checkbox_label = wait.until(EC.element_to_be_clickable((
                By.XPATH, f"//label[@for='device-user-checkbox-{index}-input']"
            )))
            checkbox_label.click()
            print(f"Checkbox for user at index {index} selected.")

            # Click the Edit button
            edit_button = wait.until(EC.element_to_be_clickable((
                By.ID, "edit-device-user"
            )))
            edit_button.click()
            print("Clicked Edit button.")

            # Change user permission
            dropdown = wait.until(EC.element_to_be_clickable((By.ID, "permissionSet")))
            dropdown.click()

            option = wait.until(EC.element_to_be_clickable((
                By.XPATH, f"//mat-option//span[normalize-space(text())='{new_role}']"
            )))
            option.click()
            print(f"Changed role to: {new_role}")

            # Enter current password
            current_password_input = wait.until(EC.element_to_be_clickable((By.ID, "currentPassword")))
            current_password_input.clear()
            current_password_input.send_keys(current_password)
            print("Entered current password.")

            # Click Apply
            apply_button = wait.until(EC.element_to_be_clickable((
                By.ID, "footer-configure-device-user-edit-button-apply"
            )))
            apply_button.click()
            print("Clicked Apply to submit changes.")

            time.sleep(2)

        except Exception as e:
            print(f"Failed to edit user at index {index}: {e}")
            driver.save_screenshot(f'edit_user_error_{index}.png')
            raise


    edit_user(driver, wait, 0, "Printer User", "admin@123")
    time.sleep(5)

    edit_user(driver, wait, 1, "Device Administrator", "user@123")
    time.sleep(5)

    def delete_all_user():
        try:
            #Select all user
            all_checkbox = wait.until(EC.element_to_be_clickable((
                By.ID, "device-user-select-all-checkbox"
            )))
            all_checkbox.click()
            print(f"All Checkbox has been clicked")

            #Click delete button
            delete_button = wait.until(EC.element_to_be_clickable((
                By.ID, "delete-device-user"
            )))
            delete_button.click()

            #Confirm delete
            confirm_delete_button = wait.until(EC.element_to_be_clickable((
                By.ID, "footer-delete-device-user-button-apply"
            )))
            confirm_delete_button.click()

            #OK
            ok_button = wait.until(EC.element_to_be_clickable((
                By.ID, "footer-delete-status-email-server-button-ok"
            )))
            ok_button.click()

        except Exception as e:
            print(f"Failed to delete user : {e}")
            raise

    delete_all_user()
    time.sleep(5)



except Exception as e:
    print(f"Error during operation: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    print("Closing the browser...")
    driver.quit()
