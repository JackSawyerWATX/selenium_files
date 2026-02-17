"""
Selenium Web Element Interaction Examples
Demonstrates common ways to interact with web elements
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Initialize the Chrome WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to a webpage
    driver.get("https://www.jonathanfausset.com")
    
    # ===== FINDING ELEMENTS =====
    # Multiple ways to locate elements:
    
    try:
        # By ID
        element = driver.find_element(By.ID, "username")
        print("✓ Found element by ID")
    except:
        print("✗ No element with ID 'username'")
    
    try:
        # By Name
        element = driver.find_element(By.NAME, "email")
        print("✓ Found element by Name")
    except:
        print("✗ No element with Name 'email'")
    
    try:
        # By Class Name
        element = driver.find_element(By.CLASS_NAME, "submit-button")
        print("✓ Found element by Class Name")
    except:
        print("✗ No element with Class 'submit-button'")
    
    try:
        # By CSS Selector
        element = driver.find_element(By.CSS_SELECTOR, "div.container > input[type='text']")
        print("✓ Found element by CSS Selector")
    except:
        print("✗ No element matching CSS selector")
    
    try:
        # By XPath
        element = driver.find_element(By.XPATH, "//button[@id='submit']")
        print("✓ Found element by XPath")
    except:
        print("✗ No element matching XPath")
    
    try:
        # By Link Text
        element = driver.find_element(By.LINK_TEXT, "Click Here")
        print("✓ Found element by Link Text")
    except:
        print("✗ No link with text 'Click Here'")
    
    try:
        # By Partial Link Text
        element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
        print("✓ Found element by Partial Link Text")
    except:
        print("✗ No link containing 'Click'")
    
    
    # ===== INTERACTING WITH ELEMENTS =====
    
    try:
        # 1. TYPING TEXT INTO INPUT FIELDS
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Selenium tutorial")  # Type text
        search_box.send_keys(Keys.RETURN)  # Press Enter key
        print("✓ Successfully typed in search box")
    except:
        print("✗ Could not interact with search box")
    
    try:
        # 2. CLICKING ELEMENTS
        button = driver.find_element(By.ID, "submit-btn")
        button.click()
        print("✓ Successfully clicked button")
    except:
        print("✗ Could not click button")
    
    try:
        # 3. DROPDOWN/SELECT ELEMENTS
        dropdown = Select(driver.find_element(By.ID, "country-select"))
        dropdown.select_by_visible_text("United States")
        print("✓ Successfully selected dropdown option")
    except:
        print("✗ Could not interact with dropdown")
    
    try:
        # 4. CHECKBOXES AND RADIO BUTTONS
        checkbox = driver.find_element(By.ID, "terms-checkbox")
        if not checkbox.is_selected():
            checkbox.click()
        print("✓ Successfully interacted with checkbox")
    except:
        print("✗ Could not interact with checkbox")
    
    try:
        # 5. EXTRACTING INFORMATION
        heading = driver.find_element(By.TAG_NAME, "h1")
        print(f"✓ Found heading: {heading.text}")
    except:
        print("✗ Could not find heading")
    
    try:
        # Get attribute value
        link = driver.find_element(By.ID, "home-link")
        href = link.get_attribute("href")
        print(f"✓ Found link URL: {href}")
    except:
        print("✗ Could not get link attribute")
    
    try:
        # 6. HANDLING MULTIPLE ELEMENTS
        all_links = driver.find_elements(By.TAG_NAME, "a")
        print(f"✓ Found {len(all_links)} links on the page")
        for i, link in enumerate(all_links[:3]):  # Show first 3
            print(f"  Link {i+1}: {link.text[:50]}")
    except:
        print("✗ Could not find links")
    
    try:
        # 7. SCROLLING
        driver.execute_script("window.scrollBy(0, 500);")
        print("✓ Successfully scrolled page")
    except:
        print("✗ Could not scroll page")
    
    try:
        # 8. TAKING SCREENSHOTS
        driver.save_screenshot("screenshot.png")
        print("✓ Screenshot saved as 'screenshot.png'")
    except:
        print("✗ Could not take screenshot")
    

finally:
    # Always close the browser
    time.sleep(2)  # Brief pause to see results
    driver.quit()


# ===== PRACTICAL EXAMPLE: LOGIN FORM =====
def login_example():
    """
    Complete example: Filling and submitting a login form
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Navigate to login page
        driver.get("https://example.com/login")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        
        # Find and fill username
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("myusername")
        
        # Find and fill password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("mypassword")
        
        # Find and click login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for login to complete and check for success
        wait.until(EC.url_contains("/dashboard"))
        
        print("Login successful!")
        
    finally:
        driver.quit()


# ===== PRACTICAL EXAMPLE: WEB SCRAPING =====
def scraping_example():
    """
    Example: Scraping product information from a page
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://example.com/products")
        
        # Wait for products to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product")))
        
        # Find all product elements
        products = driver.find_elements(By.CLASS_NAME, "product")
        
        for product in products:
            name = product.find_element(By.CLASS_NAME, "product-name").text
            price = product.find_element(By.CLASS_NAME, "product-price").text
            rating = product.find_element(By.CLASS_NAME, "rating").get_attribute("data-rating")
            
            print(f"Product: {name}, Price: {price}, Rating: {rating}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    print("This script demonstrates Selenium element interactions.")
    print("Uncomment the function calls below to run specific examples:")
    # login_example()
    # scraping_example()
