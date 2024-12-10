from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import re
import time

def setup_driver(driver_path):
    """Set up and return the Chrome WebDriver with appropriate options."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(driver_path)
    return webdriver.Chrome(service=service, options=chrome_options)

def wait_and_get_element(driver, by, value, timeout=10):
    """Wait for and return an element, with retry logic for stale elements."""
    wait = WebDriverWait(driver, timeout)
    for _ in range(3):  # Retry up to 3 times
        try:
            return wait.until(EC.presence_of_element_located((by, value)))
        except StaleElementReferenceException:
            time.sleep(1)
    raise TimeoutException(f"Element {value} not found after retries")

def get_dropdown_options(driver, dropdown_id):
    """Get all options from a dropdown with retry logic."""
    dropdown = wait_and_get_element(driver, By.ID, dropdown_id)
    select = Select(dropdown)
    try:
        return [option.text for option in select.options]
    except StaleElementReferenceException:
        # Retry once if options are stale
        time.sleep(1)
        dropdown = wait_and_get_element(driver, By.ID, dropdown_id)
        select = Select(dropdown)
        return [option.text for option in select.options]

def scrape_dsv_competitions(url, driver_path):
    """Main function to scrape DSV competition data."""
    driver = setup_driver(driver_path)
    matching_links = []
    
    try:
        # Open the website
        driver.get(url)
        
        # Click on DSV ID tab
        wait = WebDriverWait(driver, 10)
        tab = wait.until(EC.element_to_be_clickable((By.ID, "ContentSection_tab_dsv_id")))
        tab.click()
        
        # Get all season options once
        dropdown_id = "ContentSection__dsv_seasonDropDownList"
        seasons = get_dropdown_options(driver, dropdown_id)
        
        for season in seasons:
            print(f"Processing season: {season}")
            try:
                # Re-locate dropdown and select season
                dropdown = wait_and_get_element(driver, By.ID, dropdown_id)
                select = Select(dropdown)
                select.select_by_visible_text(season)
                
                # Wait for page load
                time.sleep(2)
                
                # Find competition links
                links = driver.find_elements(By.TAG_NAME, "a")
                pattern = re.compile(r"^\d{3}\. Deutsche Meisterschaften")
                
                # Store matching links
                for link in links:
                    try:
                        text = link.text.strip()
                        if pattern.match(text):
                            href = link.get_attribute("href")
                            matching_links.append((text, href))
                            print(f"Found: {text}")
                    except StaleElementReferenceException:
                        continue
                
            except Exception as e:
                print(f"Error processing season {season}: {str(e)}")
                continue
            
    except Exception as e:
        print(f"Fatal error: {str(e)}")
    
    finally:
        driver.quit()
        
    return matching_links

if __name__ == "__main__":
    URL = "https://dsvdaten.dsv.de/Modules/Results/MeetYear.aspx?Weekend=true&Lang=de-DE"
    DRIVER_PATH = "/opt/homebrew/bin/chromedriver"
    
    results = scrape_dsv_competitions(URL, DRIVER_PATH)
    
    # Create DataFrame from results
    import pandas as pd
    
    # Create DataFrame with column names
    df = pd.DataFrame(results, columns=['Competition_Name', 'URL'])
    
    # Save to Excel file
    excel_filename = 'dsv_competitions.xlsx'
    df.to_excel(excel_filename, index=False)
    
    print(f"\nData has been saved to {excel_filename}")
    print(f"Total competitions found: {len(df)}")
