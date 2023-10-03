import random
import csv

with open('books.csv','r', encoding='cp1251') as f:
    books = []
    for line in f:
      books.append(line.split(';'))
      
with open('text_file.txt', 'w') as fmy:
    for i in range(20):
        num = random.randint(1, 9409)
        l = books[num]
        author = l[3]
        name = l[1]
        date = l[6]
        fmy.write(f'{num}. {author}. {name} - {date[6:10]} \n')
