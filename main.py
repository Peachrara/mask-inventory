import json
import os
from datetime import datetime

from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crawlHKTV():
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    options = Options()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument("--headless")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-dev-shm-usage")
    start = datetime.now()
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
        print("run")
    except:
        options.binary_location = ""
        driver = webdriver.Chrome(chrome_options=options)
        print("Exception")

    driver.get("https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000")

    terminate = False
    # Crawling HKTVMall
    while not terminate:
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "brand-product-name"))
            )
        except:
            continue
        products = driver.find_elements_by_class_name("brand-product-name")
        prices = driver.find_elements_by_class_name("sepaButton.add-to-cart-button")
        print(len(products))
        print(len(prices))
        productList = []
        priceList = []
        for p in range(len(products)):
            productList.append(products[p].text)
            priceList.append(prices[p].get_attribute("data-price"))
        btn = driver.find_element_by_id("paginationMenu_nextBtn")
        if not btn.get_attribute("class") == "disabled":

            action = ActionChains(driver)
            action.move_to_element(btn).perform()
            driver.execute_script("window.scrollBy(0,100)")
            action.click().perform()
        else:
            terminate = True

    print(datetime.now() - start)
    # Creating JSON file
    with open(os.getcwd() + '/crawl/hktv.json', 'w', encoding="utf-8") as outfile:
        hktvDict = {"Title": productList, "Price": priceList}
        json.dump(hktvDict, outfile, ensure_ascii=False)

    return 0

crawlHKTV()