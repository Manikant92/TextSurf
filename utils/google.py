import time
import random
from .web import scroll

def google(driver, search):
    driver.get("https://www.google.com/search?q=" + search)
    time.sleep(random.uniform(2, 5))  # Random delay
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(random.uniform(1, 3))
    for i in range(3):
        driver.save_screenshot("./temp/" + str(i) + ".png")
        scroll(driver, 350*(i+1))
    return "./temp/0.png"