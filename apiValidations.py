import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'reyann'}, )
# print(response.text)
# print(type(response.text))
# dict_djson.loads(response.text)

json_response = response.json()
# print(type(json_response))
# print(json_response[0]['isbn'])
# print(response.status_code)
# assert response.status_code == 200
# print(response.headers)
# assert response.headers['Content-type'] == 'application/json;charset=UTF-8'
for actualBook in json_response:
    # print(type(actualBook))
    if actualBook['isbn'] == 'reyann':
        print(actualBook)
        break  # for looking the exact book
expectedBook = {
    "book_name": "Learn Appium Automation with Java",
    "isbn": "reyann",
    "aisle": "22733"
}

assert actualBook == expectedBook
