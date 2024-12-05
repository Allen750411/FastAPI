# http://127.0.0.1:8000/books/123
# 此時狀態碼為200 (F12->網路(Network)->Status:200),應該為出錯才對，因為沒有此id，資料應該抓不到，所以需做更改
# 先把  Response 呼叫進來
from fastapi import FastAPI, Response

app = FastAPI()
books = {"python": "Python book", "php": "PHP book", "js": "JavaScrpt book"}


@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/books/{id}")
# 多加一個參數 resp: Response
def books_detail(id, resp: Response):
    try:
        return {"title": books[id]}
    except KeyError:
        # 多加這串判別
        # 這串數字 404 (合規定的狀態碼)可以自訂，但是別惡搞 418 /10000/.....
        resp.status_code = 404
        return {"title": "no title"}
