# Phase II - 爬取網路圖片

## Function Interface

Input parameter: 英文拼字部分(list of str)、關鍵字(list of str)、排除字(list of str)
Output Return: 圖片的numpy array(ndarray)
(抓到的原始圖片也會儲存下來)

## Usage

* 需要額外[下載](https://chromedriver.chromium.org/downloads)chromedriver，根據使用者的Google Chrome版本下載對應的檔案，並將下載好的chromedriver和`imageCraw.py`放置在相同路徑下。
* 安裝套件
    ```
    pip install -r requirements2.txt
    ```

* 執行
    ```
    python imageCraw.py
    ```
* 輸入主要查詢單字
    ```
    cat
    ```
* 輸入多個關鍵字(以空格隔開)，若不需要則輸入一個空格
    ```
    cartoon white
    ```
* 輸入多個排除字(以空格隔開)，若不需要則輸入一個空格
    ```
    baby
    ```
![](https://i.imgur.com/QXGzmAJ.jpg)   
(搜尋到的圖片)

* 輸出結果
    ```
    [[[255 255 255]
    [255 255 255]
    [255 255 255]
    ...
    [255 255 255]
    [255 255 255]
    [255 255 255]]]
    ```
   
