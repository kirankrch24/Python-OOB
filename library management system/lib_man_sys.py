import requests
import csv

API_KEY = 'AIzaSyDH3yvAt7f3oj21wC_jm97mjB3U3I-fyNk'
QUERY = 'inauthor:"author_name"'

url = f'https://www.googleapis.com/books/v1/volumes?q={QUERY}&key={API_KEY}&maxResults=40'

response = requests.get(url)
data = response.json()

books = []

if 'items' in data:
    for item in data['items']:
        try:
            author = ', '.join(item['volumeInfo']['authors'])
            title = item['volumeInfo']['title']
            published_date = item['volumeInfo']['publishedDate']
            books.append([author, title, published_date])
        except KeyError:
            pass

with open('books.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['author_name', 'book_title', 'publication_year'])
    writer.writerows(books)

print('Books saved to books.csv')
