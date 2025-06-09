from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options to handle SSL certificate errors
chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize Chrome driver with the updated approach
service = Service("C:\\Program Files (x86)\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to printer EWS
driver.get("http://10.44.15.202/index.html")

try:
    # Wait for the page to load and the search button to be clickable
    wait = WebDriverWait(driver, 10)

    # Click the search button to open the search field
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "app-search-panel-button")))
    search_button.click()
    print("Clicked on search button")

    # Wait for the search input field to appear (you may need to adjust the selector)
    search_input = wait.until(EC.element_to_be_clickable((By.ID, "application-search")))

    # Type in the search field
    search_input.send_keys("contact")
    print("Entered search text")

    # Press Enter/Return to submit the search
    search_input.send_keys(Keys.RETURN)
    print("Submitted search")

except Exception as e:
    print(f"Error during search operation: {e}")

# Keep the browser open for a while
time.sleep(30)