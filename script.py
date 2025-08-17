from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime




driver = webdriver.Chrome()
driver.get("https://bstackdemo.com/")
driver.maximize_window()
print("Title of the Page: ", driver.title)
signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin"]')))
signin_button.click()
login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-btn']")))
driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/loginpage.png")


def login():
   username_dropdown = driver.find_element(By.XPATH,"//div[contains(text(),'Select Username')]")
   username_dropdown.click()
   fav_user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"fav_user")]')))
   fav_user.click()
   password_Dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Select Password')]")
   password_Dropdown.click()
   fav_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"testing")]')))
   fav_password.click()
   submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn")))
   submit_btn.click()
   logo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='Navbar_logo__image__3Blki']")))
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/afterlogin.png")


def quit():
   driver.quit()


#sort using vendor name
def sort_by_vendor():
   samsung_vendor = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Samsung')]")))
   samsung_vendor.click()
   first_value = driver.find_element(By.XPATH, "(//p[contains(text(),'Galaxy')])[1]")
   #print(first_value.text)
   assert first_value.text == "Galaxy S20"
   time.sleep(2)
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/sort_by_vendor_galaxy.png")
   samsung_vendor.click()


def check_filter():
   select_dropdown = driver.find_element(By.XPATH, "//select")
   select = Select(select_dropdown)
   select.select_by_value("lowestprice")
   first_row = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='val'])[1]")))
   first_row_price = driver.find_element(By.XPATH, "(//div[@class='val'])[1]")
   second_row_first_price = driver.find_element(By.XPATH, "(//div[@class='val'])[2]")


   first_price_num = float(first_row_price.text.replace("$", "").replace(",", ""))
   second_price_num = float(second_row_first_price.text.replace("$", "").replace(",", ""))


   assert first_price_num < second_price_num
   time.sleep(1)
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/sort_by_price.png")




def add_to_cart():
   add_to_cart_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//div[contains(text(),"Add to cart")])[1]')))
   add_to_cart_btn.click()
   Bag_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Bag")]')))
   checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Checkout")]')))
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots//add_to_cart.png")
   checkout_btn.click()
   stack_demo_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Stack")]')))
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/checkout.png")
   first_name = driver.find_element(By.ID, 'firstNameInput').send_keys("Akash")
   last_name = driver.find_element(By.ID, 'lastNameInput').send_keys("last_name")
   Address = driver.find_element(By.ID, 'addressLine1Input').send_keys("random address 1")
   State_province = driver.find_element(By.ID, 'provinceInput').send_keys("Maharastra")
   postal_code = driver.find_element(By.ID, 'postCodeInput').send_keys("400001")
   submit_btn = driver.find_element(By.ID, 'checkout-shipping-continue').click()
   confirmation_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'confirmation-message')))
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/orderconfirmed.png")
   continue_shop_btn = driver.find_element(By.XPATH, '//button[contains(text(),"Continue")]')
   continue_shop_btn.click()


def verify_order_placed():
   orders_Tab = driver.find_element(By.XPATH, '//strong[contains(text(),"Orders")]')
   orders_Tab.click()
   Order_Placed_date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="a-color-secondary value"])[1]')))
   driver.save_screenshot("/Users/akashdeepsingh/Desktop/Broswerstack/screenshots/ordersTab.png")
   todays_date = datetime.today().date()
   order_date = driver.find_element(By.XPATH, "(//span[@class='a-color-secondary value'])[1]")
   order_date_obj = datetime.strptime(order_date.text, "%B %d, %Y").date()
   assert todays_date == order_date_obj, f"Expected {todays_date} but got {order_date_obj}"


def print_result():
   results = []
   try:
       login()
       results.append("Login: ✅ Successful")
   except Exception as e:
       results.append(f"Login: ❌ Failed ({e})")
   try:
       sort_by_vendor()
       results.append("Sort by vendor: ✅ Successful")
   except Exception as e:
       results.append(f"Sort by vendor: ❌ Failed ({e})")
   try:
       check_filter()
       results.append("Filter check: ✅ Successful")
   except Exception as e:
       results.append(f"Filter check: ❌ Failed ({e})")
  
   try:
       add_to_cart()
       results.append("Add to cart: ✅ Successful")
   except Exception as e:
       results.append(f"Add to cart: ❌ Failed ({e})")
   try:
       verify_order_placed()
       results.append("Verify order placed: ✅ Successful")
   except Exception as e:
       results.append(f"Verify order placed: ❌ Failed ({e})")
   try:
       quit()
   except Exception as e:
       results.append(f"Quit: ❌ Failed ({e})")
   for result in results:
       print(result)


print_result()

