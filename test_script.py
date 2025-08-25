from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
import pytest
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bstackdemo.com/")
    yield driver
    driver.quit()

def login(driver):
    driver.get("https://bstackdemo.com/signin")
    username_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Select Username')]")))
    username_dropdown.click()
    fav_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"fav_user")]')))
    fav_user.click()
    password_dropdown = password_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Select Password')]")
    password_dropdown.click()
    fav_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"testing")]')))
    fav_password.click()
    submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn")))
    submit_btn.click()
    logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='Navbar_logo__image__3Blki']")))
    assert logo.is_displayed()
    driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/afterlogin.png")
    logo.click()


#Tests
@allure.title("Login Test")
@allure.description("Verify that user can log in with valid credentials and see the logo on the homepage.")
@allure.severity(allure.severity_level.BLOCKER)
def test_login(driver):
    with allure.step("Click on Signin Button"):
        signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin"]')))
        signin_button.click()
    with allure.step("Select Username from Dropdown"):
        username_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Select Username')]")))
        username_dropdown.click()
        fav_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"fav_user")]')))
        fav_user.click()
    with allure.step("Select Password from Dropdown"):
        password_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Select Password')]")
        password_dropdown.click()
        fav_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"testing")]')))
        fav_password.click()
    with allure.step("Click on Login Button"):
        submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn")))
        submit_btn.click()
    with allure.step("Verify Logo is visible after login"):
        logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='Navbar_logo__image__3Blki']")))
        assert logo.is_displayed()
        allure.attach(driver.get_screenshot_as_png(), name="afterlogin", attachment_type=allure.attachment_type.PNG)
        logo.click()

@allure.title("Sort by Vendor Test")
@allure.description("Verify that user can sort products by vendor.")
@allure.severity(allure.severity_level.CRITICAL)
def test_sort_by_vendor(driver):
    with allure.step('Select Samsung Vendor'):
        samsung_vendor = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Samsung')]")))
        samsung_vendor.click()
    with allure.step('Verify First Value'):
        first_value = driver.find_element(By.XPATH, "(//p[contains(text(),'Galaxy')])[1]")
        assert first_value.text == "Galaxy S20"
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="sort_by_vendor_galaxy", attachment_type=allure.attachment_type.PNG)
        samsung_vendor.click()

@allure.title("Sort By Filter Test")
@allure.description("Verify that user can filter products by price.")
@allure.severity(allure.severity_level.TRIVIAL)
def test_check_filter(driver):
    with allure.step("Sort by Lowest Price"):
        select_dropdown = driver.find_element(By.XPATH, "//select")
        select = Select(select_dropdown)
        select.select_by_value("lowestprice")
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="sort_by_price", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Assert the price between first row and second row"):
        first_row = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='val'])[1]")))
        first_row_price = driver.find_element(By.XPATH, "(//div[@class='val'])[1]")
        second_row_first_price = driver.find_element(By.XPATH, "(//div[@class='val'])[2]")
        first_price_num = float(first_row_price.text.replace("$", "").replace(",", ""))
        second_price_num = float(second_row_first_price.text.replace("$", "").replace(",", ""))
        assert first_price_num < second_price_num
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name="price_assertion", attachment_type=allure.attachment_type.PNG)


@allure.title("Verify if user is able to add items in the cart")
@allure.description("Verify that user can add items to the cart and complete the checkout process.")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_to_cart(driver):

    with allure.step("Click on 'Add to cart' button for the first item"):
        add_to_cart_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[contains(text(),"Add to cart")])[1]'))
        )
        add_to_cart_btn.click()
    time.sleep(1)
    with allure.step("Verify Bag text and click Checkout"):
        Bag_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Bag")]'))
        )
        assert Bag_text.is_displayed()
        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Checkout")]'))
        )
        driver.save_screenshot("screenshots/add_to_cart.png")
        allure.attach.file("screenshots/add_to_cart.png", name="Cart Screenshot", attachment_type=allure.attachment_type.PNG)
        checkout_btn.click()

    with allure.step("Login with favourite user"):
        username_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Select Username')]"))
        )
        username_dropdown.click()

        fav_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"fav_user")]'))
        )
        fav_user.click()

        password_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Select Password')]")
        password_dropdown.click()

        fav_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"testing")]'))
        )
        fav_password.click()

        submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn")))
        submit_btn.click()

    with allure.step("Verify user navigated to Stack Demo checkout page"):
        stack_demo_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Stack")]'))
        )
        assert stack_demo_text.is_displayed()
        driver.save_screenshot("screenshots/checkout.png")
        allure.attach.file("screenshots/checkout.png", name="Checkout Screenshot", attachment_type=allure.attachment_type.PNG)

    with allure.step("Fill shipping details"):
        driver.find_element(By.ID, 'firstNameInput').send_keys("Akash")
        driver.find_element(By.ID, 'lastNameInput').send_keys("last_name")
        driver.find_element(By.ID, 'addressLine1Input').send_keys("random address 1")
        driver.find_element(By.ID, 'provinceInput').send_keys("Maharashtra")
        driver.find_element(By.ID, 'postCodeInput').send_keys("400001")

        submit_btn = driver.find_element(By.ID, 'checkout-shipping-continue')
        submit_btn.click()

    with allure.step("Verify order confirmation"):
        confirmation_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'confirmation-message'))
        )
        assert confirmation_msg.is_displayed()
        driver.save_screenshot("screenshots/orderconfirmed.png")
        allure.attach.file("screenshots/orderconfirmed.png", name="Order Confirmation", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click on 'Continue Shopping' button"):
        continue_shop_btn = driver.find_element(By.XPATH, '//button[contains(text(),"Continue")]')
        continue_shop_btn.click()

@allure.title("Verify Order Placed Test")
@allure.description("Verify that the order placed date matches today's date.")
@allure.severity(allure.severity_level.NORMAL)
def test_verify_order_placed(driver):
    test_add_to_cart(driver)
    with allure.step("Navigate to Orders Tab"):
        orders_Tab = driver.find_element(By.XPATH, '//strong[contains(text(),"Orders")]')
        orders_Tab.click()
    with allure.step("Verify Order Placed Date"):
        Order_Placed_date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="a-color-secondary value"])[1]')))
        allure.attach(driver.get_screenshot_as_png(), name="orders_tab", attachment_type=allure.attachment_type.PNG)
        todays_date = datetime.today().date()
        order_date = driver.find_element(By.XPATH, "(//span[@class='a-color-secondary value'])[1]")
        order_date_obj = datetime.strptime(order_date.text, "%B %d, %Y").date()
        assert todays_date == order_date_obj, f"Expected {todays_date} but got {order_date_obj}"
