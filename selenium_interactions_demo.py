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
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to a webpage
    driver.get("https://www.jonathanfausset.com")
    
    # ===== FINDING ELEMENTS =====
    # Multiple ways to locate elements:
    
    # By ID
    element = driver.find_element(By.ID, "username")
    
    # By Name
    element = driver.find_element(By.NAME, "email")
    
    # By Class Name
    element = driver.find_element(By.CLASS_NAME, "submit-button")
    
    # By CSS Selector
    element = driver.find_element(By.CSS_SELECTOR, "div.container > input[type='text']")
    
    # By XPath
    element = driver.find_element(By.XPATH, "//button[@id='submit']")
    
    # By Link Text
    element = driver.find_element(By.LINK_TEXT, "Click Here")
    
    # By Partial Link Text
    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
    
    
    # ===== INTERACTING WITH ELEMENTS =====
    
    # 1. TYPING TEXT INTO INPUT FIELDS
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium tutorial")  # Type text
    search_box.send_keys(Keys.RETURN)  # Press Enter key
    
    # Clear existing text before typing
    search_box.clear()
    search_box.send_keys("New search query")
    
    
    # 2. CLICKING ELEMENTS
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    
    # Click a link
    link = driver.find_element(By.LINK_TEXT, "About Us")
    link.click()
    
    
    # 3. DROPDOWN/SELECT ELEMENTS
    dropdown = Select(driver.find_element(By.ID, "country-select"))
    
    # Select by visible text
    dropdown.select_by_visible_text("United States")
    
    # Select by value attribute
    dropdown.select_by_value("us")
    
    # Select by index (0-based)
    dropdown.select_by_index(2)
    
    # Get all options
    all_options = dropdown.options
    for option in all_options:
        print(option.text)
    
    
    # 4. CHECKBOXES AND RADIO BUTTONS
    checkbox = driver.find_element(By.ID, "terms-checkbox")
    
    # Check if already selected
    if not checkbox.is_selected():
        checkbox.click()  # Check the box
    
    # Radio button
    radio = driver.find_element(By.ID, "payment-method-credit")
    radio.click()
    
    
    # 5. EXTRACTING INFORMATION
    # Get text content
    heading = driver.find_element(By.TAG_NAME, "h1")
    print(f"Heading text: {heading.text}")
    
    # Get attribute value
    link = driver.find_element(By.ID, "home-link")
    href = link.get_attribute("href")
    print(f"Link URL: {href}")
    
    # Get CSS property
    color = heading.value_of_css_property("color")
    print(f"Heading color: {color}")
    
    # Check if element is displayed/enabled
    if button.is_displayed() and button.is_enabled():
        button.click()
    
    
    # 6. WAITING FOR ELEMENTS (Important for dynamic pages)
    # Explicit wait - wait up to 10 seconds for element to be clickable
    wait = WebDriverWait(driver, 10)
    clickable_button = wait.until(
        EC.element_to_be_clickable((By.ID, "dynamic-button"))
    )
    clickable_button.click()
    
    # Wait for element to be visible
    visible_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "popup"))
    )
    
    
    # 7. ADVANCED INTERACTIONS (ActionChains)
    actions = ActionChains(driver)
    
    # Hover over an element
    menu = driver.find_element(By.ID, "main-menu")
    actions.move_to_element(menu).perform()
    
    # Right-click (context click)
    element = driver.find_element(By.ID, "context-menu-target")
    actions.context_click(element).perform()
    
    # Double-click
    actions.double_click(element).perform()
    
    # Drag and drop
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source, target).perform()
    
    # Chain multiple actions
    actions.move_to_element(menu).click().send_keys("text").perform()
    
    
    # 8. HANDLING MULTIPLE ELEMENTS
    # Find all matching elements
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    for link in all_links:
        print(f"Link: {link.text} -> {link.get_attribute('href')}")
    
    
    # 9. SWITCHING BETWEEN FRAMES/IFRAMES
    # Switch to iframe by name or id
    driver.switch_to.frame("iframe-name")
    
    # Interact with elements inside iframe
    iframe_button = driver.find_element(By.ID, "iframe-button")
    iframe_button.click()
    
    # Switch back to main content
    driver.switch_to.default_content()
    
    
    # 10. HANDLING ALERTS/POPUPS
    # Click something that triggers an alert
    alert_button = driver.find_element(By.ID, "alert-button")
    alert_button.click()
    
    # Wait for alert and switch to it
    alert = wait.until(EC.alert_is_present())
    
    # Get alert text
    print(f"Alert text: {alert.text}")
    
    # Accept alert (click OK)
    alert.accept()
    
    # Or dismiss alert (click Cancel)
    # alert.dismiss()
    
    
    # 11. SCROLLING
    # Scroll to element
    element = driver.find_element(By.ID, "footer")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    
    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Scroll by specific amount
    driver.execute_script("window.scrollBy(0, 500);")
    
    
    # 12. TAKING SCREENSHOTS
    driver.save_screenshot("screenshot.png")
    
    # Screenshot of specific element
    element = driver.find_element(By.ID, "content")
    element.screenshot("element_screenshot.png")
    

finally:
    # Always close the browser
    time.sleep(2)  # Brief pause to see results
    driver.quit()


# ===== PRACTICAL EXAMPLE: LOGIN FORM =====
def login_example():
    """
    Complete example: Filling and submitting a login form
    """
    driver = webdriver.Chrome()
    
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
    driver = webdriver.Chrome()
    
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
