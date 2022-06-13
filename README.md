# memeGenerator

諧音梗圖產生器。使用者輸入一句中文句子，程式輸出一張包含帶有諧音的句子的圖片。

## Usage

* 安裝套件：`Phase1/`、`Phase2`、 `Phase3/`三個資料夾的`README.md`。

* 請將下載好解壓縮後的chromedriver放到執行的資料夾，並命名為`chromedriver.exe`。(詳情請參照`Phase2/`)

* 執行

  ```bash
  python3 MemeTextGenerator.py
  ```

* python

  ```python
  from memeGenerator import memeGenerator
  chinese_str = u'有備而來'
  keyword = u'卡通'
  negative_keyword = u'背景'
  memeGenerator(chinese_str, keyword, negative_keyword)
  ```

  