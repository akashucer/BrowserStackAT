# BrowserStackAT

Automated UI testing for Broswerstack Demo Website "StackDemo" using Selenium, Pytest, and Allure reporting.

## Features
- Login test
- Sort products by vendor
- Filter products by price
- Add items to cart and checkout
- Verify order placement
- Screenshots for each step
- Allure reporting integration

## Folder Structure
```
├── test_Script.py         # Main test file with pytest and allure
├── reports/               # Allure and test run artifacts
├── screenshots/           # Screenshots captured during tests
```

## Requirements
- Python 3.8+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium
- Pytest
- Allure-pytest

## Installation
```bash
pip install selenium pytest allure-pytest
```

## Usage
1. **Run tests:**
   ```bash
   pytest --alluredir=reports/
   ```
2. **View Allure report:**
   ```bash
   allure serve reports/
   ```

## Test Details
- Each test is decorated with Allure annotations for better reporting.
- Screenshots are attached to Allure reports for failed and successful steps.
- Tests are independent and use fixtures for browser setup/teardown.

## Contributing
1. Fork the repo
2. Clone your fork
3. Create a new branch
4. Make changes and commit
5. Push and create a pull request


## Author
Akashdeep Singh
