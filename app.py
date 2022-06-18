from poplib import POP3
from cv2 import Param_UINT64
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install() )

WEBSITE_URL = r"https://www.amazon.eg/s?rh=n%3A21832883031&fs=true&language=en&ref=lp_21832883031_sar"
#DRIVER_PATH = r"~/Desktop/projects/scrapping/chromedriver_linux64"
CARDS_PATH = r"//div[@class = 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20']"
NEXT_BUTTON_PATH = "//span[@class = 's-pagination-strip']/a[@class = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"

# driver = webdriver.Chrome(DRIVER_PATH)
driver.get(WEBSITE_URL)


cards = driver.find_elements_by_xpath(CARDS_PATH)


print(f"num elementd = {len(cards)}")
rows = []
page = 1
num_elements = 0

rows = []
for card in cards:
    title  = card.find_element_by_xpath(".//span[@class = 'a-size-base-plus a-color-base a-text-normal']").text
    rate = card.find_element_by_xpath(".//span[@class = 'a-size-base s-underline-text']").text
  
    price = 0
    try:
        price  = card.find_element_by_xpath(".//span[@class = 'a-price-whole']").text
    except:
        print("Price ERROR!!")

    price_frac = 00
    try:
        price_frac  = card.find_element_by_xpath(".//span[@class = 'a-price-fraction']").text
    except:
        print("Price _frac ERROR!!")

    print(title)
    print(price)
    print(rate)
    print("*********************")

    row = [title, rate, price, price_frac]
    rows.append(row)
driver.quit()


df = pd.DataFrame(data= rows,columns=['product_name', 'rating', 'price', 'price_fraction'])
print(df.shape)
df.head()
df.to_csv("amazon_mobile.csv")