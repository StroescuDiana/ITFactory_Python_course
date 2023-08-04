import requests
from api_requests.authentification_request import get_token


token = get_token()
print(token)

base_url = "https://simple-books-api.glitch.me"
def get_status():
    response = requests.get(f"{base_url}/status")
    return response.json()["status"]

status = get_status()
print(status)

def get_books():
    response = requests.get(f"{base_url}/books")
    return response.status_code

# status_books = get_books()
# print(status_books)

def get_single_book(bookid):
    response = requests.get(f"{base_url}/books/{bookid}")
    return response.json()["name"]

# book = get_single_book(2)
# print(book)

def submit_order():
    header = {"Authorization": token}
    body = {
        "bookId": 1,
        "customerName": "Cathya"
    }
    response = requests.post(f"{base_url}/orders", headers=header, json=body)
    return bool(response.json()["created"])

order = submit_order()
print(order)
