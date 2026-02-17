# Selenium Web Automation Demo

A collection of Python scripts demonstrating Selenium WebDriver interactions with web pages.

## Project Contents

- **selenium_interactions_demo.py** - Comprehensive examples of common Selenium operations including:
  - Finding elements (by ID, name, class, CSS selector, XPath, etc.)
  - Typing text into input fields
  - Clicking elements and links
  - Interacting with dropdowns/select elements
  - Working with checkboxes and radio buttons
  - Extracting text and information from elements
  - Waiting for elements (WebDriverWait)
  - Handling alerts
  - Managing cookies and sessions
  - Taking screenshots
  - Executing JavaScript
  - Advanced interactions (drag & drop, mouse hovering)

- **simple_selenium_demo.py** - A simpler introduction to basic Selenium operations

## Prerequisites

- Python 3.x
- Selenium library
- Chrome WebDriver (or appropriate driver for your browser)

## Installation

1. Install Selenium:
```bash
pip install selenium
```

2. Download ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/) matching your Chrome version, or let Selenium handle it automatically (Selenium 4.x+).

## Usage

Run either demo script:
```bash
python selenium_interactions_demo.py
python simple_selenium_demo.py
```

## Important Notes

The current demo scripts are set up to run against example websites. You'll need to:

1. **Verify element selectors** - The scripts use placeholder selectors like `id="username"`. Before running, inspect the actual webpage and update these selectors to match real elements on the target page.

2. **Update target URLs** - Change `driver.get("https://www.example.com")` to the actual URL you want to test.

3. **Handle timeouts** - If elements load dynamically, add `WebDriverWait` to wait for elements:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
```

## Common Selectors Reference

| Method | Example | Use Case |
|--------|---------|----------|
| ID | `By.ID, "username"` | Unique element identifier |
| Name | `By.NAME, "email"` | Form field names |
| Class | `By.CLASS_NAME, "button"` | Multiple elements with same class |
| CSS Selector | `By.CSS_SELECTOR, "div.container > input"` | Complex selectors |
| XPath | `By.XPATH, "//button[@id='submit']"` | Powerful, flexible selection |
| Link Text | `By.LINK_TEXT, "Click Here"` | Exact link text |
| Partial Link | `By.PARTIAL_LINK_TEXT, "Click"` | Partial link text |

## Troubleshooting

- **NoSuchElementException** - Element not found. Verify selector and check if element exists on the page.
- **TimeoutException** - Element didn't load in time. Increase wait time or verify the selector.
- **StaleElementReferenceException** - Element no longer in DOM. Re-find the element after page changes.

## Resources

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Selenium Official Docs](https://www.selenium.dev/documentation/)
