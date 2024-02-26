import csv

def writeCsvFile(fname, data):
    ''' Описание функции writeCsvFile.
    Описание аргументов:

    fname - string, name of file to write
    data - list of list of items

    '''
    csvfile = open(fname,'w',newline='')

    csvwriter = csv.writer(csvfile)
    for item in data:
        mydata=[item]
        csvwriter.writerow(mydata)
    csvfile.close()




f=open('game.txt','r',encoding='utf-8')
f=f.readlines()
lst=[str(i)[:-1] for i in f]
mydata=[]
for i in lst:
    GameName,characters,nameError,date=i.split("$")
    if '55' in nameError:
        i=f"У персонажа;{characters};в игре;{GameName};нашлась ошибка с кодом:; {nameError}.;Дата фиксации:; {date}"
        mydata.append(i)
writeCsvFile(r'game_new.csv',mydata)

'Отчет создан'
mydata=[]
"Переход к его выполнению"
for i in lst:
    GameName,characters,nameError,date=i.split("$")
    if '55' in nameError:
        i=f"У персонажа;{characters};в игре;{GameName};нашлась ошибка с кодом:; {'Done'}.;Дата фиксации:; {'0000-00-00'}"
        mydata.append(i)
writeCsvFile(r'game_new.csv',mydata)