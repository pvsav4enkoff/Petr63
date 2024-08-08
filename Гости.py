frend = ['Иван','Петр','Сергей','Владимир','Юрий']
print(frend)
print('Привет, '+frend[0]+ ' приходи на пиво.')
print('Привет, '+frend[1]+ ' приходи на пиво.')
print('Привет, '+frend[2]+ ' приходи на пиво.')
print('Привет, '+frend[3]+ ' приходи на пиво.')
print('Привет, '+frend[4]+ ' приходи на пиво.')

frend_lost=frend.pop(0)
print(frend)
frend.append('Инокентий')
print(frend)
print(frend_lost)
print(len(frend))
i = 0 # объявление переменной i для условия цикла
while i < len(frend): # ключевое слово 'while' и условие выполнение цикла
    # тело цикла
    print('Привет, '+frend[i]+ ' приходи на пиво.')
    i += 1
frend.insert(0, 'Ибрагим')
frend.insert(2, 'Хафиза')
frend.append('Фарида')
print(frend)
print(len(frend))

x=len(frend)

i = 0 # объявление переменной i для условия цикла
while i <= x-1: # ключевое слово 'while' и условие выполнение цикла
    # тело цикла
    print(i)
    #print('Извини, '+frend[i]+ ' пиво не завезли.')
    #del frend[i]
    i += 1
print(frend)
#i = 0 # объявление переменной i для условия цикла
print(len(frend))
#frend.pop(0)
#frend.pop(1)
#frend.pop(2)
#frend.pop(3)
#frend.pop(4)
#frend.pop(5)

for frn in frend:
    print('1',frn.upper())
    print('2',frn.upper())

print(len(frend))
#del frend[0]
#del frend[1]
#del frend[2]
#del frend[3]
#del frend[0]
#del frend[1]
#del frend[4]
#rint(len(frend))
#for frn in frend: print(frn)