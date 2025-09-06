def book_profile():
    print(f'\n===Add book information===')
    book_title = input('book title:')
    book_author = input('book author:')
    book_genre = input('book genre:')
    book_content = input('what is the content of the book?')
    thoughts_after_reading = input('what is your after-reading?')
    return f'Book title:{book_title},Book author:{book_author},Book genre:{book_genre},{book_content},{thoughts_after_reading}'

print('===book information system===')
count = int(input('How many books to app?'))

books = []
for i in range(count):
    profile = book_profile()
    books.append(profile)

print('\n===book list===')
for profile in books:
    print(profile)