import csv

with open('books.csv', 'r', encoding='cp1251') as f:
     reader = csv.reader(f, delimiter = ';')
     cnt_name = 0
     for line in reader:
          if len(line[1]) > 30:
            cnt_name += 1
print(f'Количество записей, у которых в поле "Название" строка длиннее 30 символов: {cnt_name}')
