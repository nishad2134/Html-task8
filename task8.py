import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

book_data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][1]  # The rating is in the second class attribute

    book_data.append([title, price, rating])
df = pd.DataFrame(book_data, columns=['Title', 'Price', 'Rating'])
df.to_csv('books.csv', index=False)
