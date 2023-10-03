import csv

with open('books.csv', 'r', encoding='cp1251') as f:
     reader = csv.DictReader(f)
     cnt = 0
     for line in reader:
          cnt += 1
print(f'Кол-во записей в файле: {cnt}')
