from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click_ac_tab_by_name(driver, wait, tab_name):
    """
    Clicks on a tab in the EWS page based on the displayed name.

    :param driver: Selenium WebDriver instance
    :param wait: WebDriverWait instance
    :param tab_name: Exact visible text of the tab you want to click
    """
    try:
        tab_xpath = f"//div[@class='mat-tab-label-content' and normalize-space(text())='{tab_name}']"
        tab_element = wait.until(EC.element_to_be_clickable((By.XPATH, tab_xpath)))
        print(f"Clicking on tab: {tab_name}")
        tab_element.click()
    except Exception as e:
        print(f"Could not find or click the tab '{tab_name}'. Error: {e}")
        raise e
