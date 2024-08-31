from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Use the appropriate driver for your browser

try:
    # Open the registration page
    driver.get(r"C:\Users\Admin\Documents\Visual Studio Python\Python Practice Fites\index.html")

    # Fill in the registration form
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePassword123")
    driver.find_element(By.ID, "confirmPassword").send_keys("SecurePassword123")
    driver.find_element(By.ID, "phone").send_keys("1234567890")

    # Submit the form
    driver.find_element(By.XPATH, "//button[text()='Register']").click()

    # Wait for a moment to see the result (if there's a confirmation page)
    time.sleep(5)

    # Optionally, you can verify if the registration was successful
    # This part depends on your application's behavior after submission
    # Example: Check for a success message
    # success_message = driver.find_element(By.ID, "successMessage").text
    # assert "Registration Successful" in success_message

finally:
    # Close the browser
    driver.quit()