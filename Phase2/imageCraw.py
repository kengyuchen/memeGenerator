import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
import numpy as np


def get_image_ndarray(name:str, keyword:list or str=None,negative_keyword:list or str=None)->"ndarray":

    img_name = name

    if type(keyword) == list and keyword is not None:
        for x in keyword:
            img_name += '+"{}"'.format(x)
    elif type(keyword)== str and keyword is not None:
        img_name += '+"{}"'.format(keyword)

    if type(negative_keyword) == list and negative_keyword is not None:
        for x in negative_keyword:
            img_name += '+-{}'.format(x)
    elif type(negative_keyword)== str and negative_keyword is not None:
        img_name += '+-{}'.format(negative_keyword)

    url = "https://www.google.com/search?q={}&tbm=isch".format(img_name)

    # 建立chromedriver並啟動
    chrome_driver = r"./chromedriver"
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_driver, options=option)
    driver.get(url)

    # 定位圖片位址並儲存
    img_src = driver.find_element(By.CSS_SELECTOR, ".isv-r .islib .islir img").click()
    time.sleep(4)
    img_real_src = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
    img = requests.get(img_real_src)
    with open("phase2.jpg", "wb") as file:
        file.write(img.content)

    # 用PIL中的Image將本地的檔案打開轉成ndarray
    pic = Image.open('phase2.jpg')
    arr = np.array(pic)

    return arr


if __name__ == "__main__":
    figure_arr = get_image_ndarray(input(), input().split(), input().split())
    print(figure_arr)