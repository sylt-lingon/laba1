with open('books.csv','r', encoding='cp1251') as f:

    authors = dict()
    title = f.readline().split(';')

    for line in f:
        l = line.split(';')
        cur_name = l[3]
        if cur_name in authors:
            authors[cur_name].append(l)
        else:
            authors[cur_name] = []
            authors[cur_name].append(l)

name = input('Введите автора: ')
print('Книги:')

if name in authors:
        inf = authors[name]
        print(title,':')
        for i in range(len(inf)):
            print(inf[i])
else:
    print('Книг этого автора нет в базе :(')
