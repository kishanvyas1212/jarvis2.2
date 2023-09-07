
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Put code inside a function
def automation():
    driver = uc.Chrome(executable_path='chromedriver.exe')

    # Navigate to the link
    driver.get("https://chat.openai.com/chat")
    driver.implicitly_wait(10)
    time.sleep(3)

    # Wait until the "click element" present on webpage
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div')))

    # Login to the page with the given username
    email_click_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div').click()
    username = driver.find_element(By.ID, "username").send_keys("kishanvyas12")
    continue_btn = driver.find_element(By.NAME, "action").click()

    # Login to the page with the given password
    password = driver.find_element(By.NAME, "password").send_keys("Your Password here")
    continue_btn = driver.find_element(By.NAME, "action").click()

    click_on_btn = driver.find_element(By.CLASS_NAME, "btn.flex.justify-center.gap-2.btn-neutral.ml-auto").click()
    continue_btn = driver.find_element(By.CLASS_NAME, "btn.flex.justify-center.gap-2.btn-neutral.ml-auto").click()
    time.sleep(8)

    # Skip the popup
    def skip_info():
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB * 3)
        actions.perform()

        actions.send_keys(Keys.ENTER)
        actions.perform()

    # Calling a function
    skip_info()
    time.sleep(3)

    # Search query
    input_field = driver.find_element(By.XPATH, '//form/div/div[2]/textarea').send_keys("Create a login page in HTML")
    time.sleep(2)
    driver.find_element(By.XPATH, "//main/div[2]/form/div/div[2]/button").click()
    time.sleep(10)


if __name__ == '__main__':
    automation()  # execute this only when run directly, not when imported!
