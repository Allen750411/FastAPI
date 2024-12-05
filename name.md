# JS 取出 name

# 下方是一個物件，會有屬性

const hero = {
name: 'kk',
age: 18
}

hero.name
hero['name']

# Py 取出 name

# 下方是一個字典

hero = {
"name": "kk",
"age": 18
}

hero["name"]
hero.get("name")

- 前後端分離
- 切版： 設計、切版、動畫
- 前端：串 API、呈現資料、SPA = Single Pag Application
- 渲染，沒有換頁
- 資料抓取後，透過 DOM 的變化 / 操作 Data
- 網址都沒有變，都在同一頁面
- 後端：給 API、資料庫、伺服器、資料處理

- SSR = Server Side Render
- 無前後端分離
- 畫面放在 template
- 資料放在.py 檔
- 從資料庫撈資料
- 透過神社樣板引擎把資料塞進 template

- Django 一站式 (前後端無分離)
- Flask 一站式 / 分離
- FastAPI 單純後端
- 微服務 Micro Service

# FastAPI url="https://fastapi.tiangolo.com/"

- 建立虛擬環境
- python -m venv .venv
-
- .\.venv\Scripts\activate
- 新增 main.py 檔案
- 安裝 pip install "fastapi[standard]"
- main.py 輸入程式碼
  -from fastapi import FastAPI

  app = FastAPI()

  app.get("/")
  def home():
  return {"hello": "world"}

- 執行 fastapi dev main.py

# swagger

# http://127.0.0.1:8000/docs 後端介面
