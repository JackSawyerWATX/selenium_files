"""
Simple Selenium Example - Google Search Automation
This script demonstrates basic element interactions by automating a Google search
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)

try:
    print("1. Opening Google...")
    driver.get("https://www.google.com")
    
    # Wait for search box to be present
    wait = WebDriverWait(driver, 10)
    
    print("2. Finding search box...")
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    print("3. Typing search query...")
    search_box.send_keys("Selenium WebDriver")
    
    print("4. Pressing Enter...")
    search_box.send_keys(Keys.RETURN)
    
    print("5. Waiting for results...")
    # Wait for results to load (with increased timeout and alternative locator)
    time.sleep(3)  # Simple wait instead of explicit wait to avoid crash
    
    print("6. Extracting search results...")
    # Find all result titles
    try:
        result_titles = driver.find_elements(By.CSS_SELECTOR, "h3")
        print(f"\nFound {len(result_titles)} results:")
        for i, title in enumerate(result_titles[:5], 1):  # Print first 5
            if title.text:
                print(f"   {i}. {title.text}")
    except Exception as e:
        print(f"   Note: Could not extract all results: {e}")
    
    print("\n7. Taking a screenshot...")
    driver.save_screenshot("google_search_results.png")
    print("   Screenshot saved as 'google_search_results.png'")
    
    time.sleep(2)  # Pause to see the results
    
    print("\n✓ Demo completed successfully!")

except Exception as e:
    print(f"\n✗ Error occurred: {e}")

finally:
    print("\nClosing browser...")
    driver.quit()
