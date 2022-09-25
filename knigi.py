import csv, random
flag = 0
with open('books.csv', 'r') as csvfile:
    count = 0                               #счетчик строк
    count30 = 0                             #счетчик строк, название книги в которой длиннее 30 символов
    table = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for row in table:                       #перебор строк из таблицы
        count += 1
        if len(row[1]) > 30:
            count30 += 1
print('Количество строк =', count)
print('Количество записей, где название > 30 =', count30)
print()

f = open('result.txt', 'w')                 #создание txt файла для записи
with open('books.csv', 'r') as csvfile:
    books = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for count in range(1,21):
        numb = random.randrange(1,len(books))
        ran = books[numb]                   #перебор рандомных строк
        f.write(f'{count} {ran[4]}. {ran[1]} - {ran[6][0:4]} \n') #запись их в файл
f.close()

with open('books.csv', 'r') as csvfile:
    search = input('Search for: ').lower()                        #задал поиск в нижнем регистре
    book = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for row in book:                                              #перебор строк
        low = row[4].lower()                                      #автор в нижнем регистре присваивается low
        if search in low:                                         #проверка наличия того, что ввели при поиске в low
            if ('2016' in row[6]) or ('2017' in row[6]) or ('2018' in row[6]):  #проверка доп условия №7
                flag = 1
                print(row[4]+'.', row[1], '-', row[6][0:4])       #вывод результатов поиска
    if flag == 0:
        print('Nothing found')                                    #если поиск не дал результата