# Phase 3 圖片加上文字

## Reference
GitHub [samgermain/python-meme](https://github.com/samgermain/python-meme.git)
## Function Interface
- Input parameter: 
    - caption: 欲印出文字（str）
    - array: 圖片的numpy array(ndarray)
    - imgID: 圖片的ID，str或int皆可，預設為"0"
- Output parameter: 無
- generate: 生成圖片，名稱為 "./phase3_id"
- function
```
putcaptions(caption, array, imgID = '0')
```

## Usage
安裝套件Pillow (ie. PIL)
```
$ pip install Pillow
# OR
$ pip3 install Pillow
```

## 直接使用
需已有一張圖片儲存於檔案夾中
會生成一張帶有文字的圖片，檔名為 phase3_id
```
$ python3 main.py
Insert pic source with file extension 輸入檔案path
my_image.jpg    
Input caption 輸入標題
這是一張meme
```


