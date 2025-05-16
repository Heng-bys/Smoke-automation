from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_and_handle_pin(driver, wait, pin_code="49030355"):
    try:
        # Short wait to check if PIN input appears
        pin_input = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='pin']"))
        )
        print("PIN prompt detected, entering PIN...")

        pin_input.clear()
        pin_input.send_keys(pin_code)

        # Now locate and click the Sign In button
        sign_in_button = driver.find_element(By.XPATH, "//span[text()='Sign In']/ancestor::button")
        sign_in_button.click()
        print("Clicked Sign In button after entering PIN.")

        # Optional: Wait for page to process and load
        time.sleep(2)

    except Exception:
        # No PIN prompt appeared, safe to continue
        pass
