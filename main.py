# from 模組名稱 import 方法
# 從 fastapi 模組中導入 FastAPI
from fastapi import FastAPI

app = FastAPI()

books = {"python": "Python book", "php": "PHP book", "js": "JavaScrpt book"}


# 建了一個 FastAPI 應用 app，並設置了一個簡單的路由，當訪問根路徑 / 時，返回一個包含 "Hello, World!" 的 JSON 響應。
@app.get("/")
def home():
    return {"hello": "world"}


# 建立books的網址
# 127.0.0.1:8000/books/python(php,js)
@app.get("/books/{id}")
def books_detail(id):
    # 下列文字說明會出現在http://127.0.0.1:8000/docs
    # \n 換行意思
    """
    請輸入id \n
    id格式等等....

    """
    # 有一個字典儲存書籍 ID 和書籍名稱的對應
    # 此id為 python /php /js
    books = {"python": "Python book", "php": "PHP book", "js": "JavaScrpt book"}
    # 根據傳入的 ID 查找對應的書籍名稱，若無則返回 "no title"
    return {"hi": "hey", "book": books.get(id, "no title")}


# http://127.0.0.1:8000/books/123
# 此時狀態碼為200 (F12->網路(Network)->Status:200),應該為出錯才對，因為沒有此id，資料應該抓不到，所以需做更改
# 檔案在檔案在 main2.py


@app.get("/books")
def book_list():
    # 字典變字串 : 串列推導式
    all_books = [{key: title} for key, title in books.items()]
    return all_books
