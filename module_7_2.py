import os
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def count_lines(filename):
    with open(filename, 'r',encoding="utf-8") as file:
        i = sum(1 for _ in file)
        # file.close()
    return i
def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w',encoding="utf-8")
    for string in strings:
        file.write(f"{str(string)}\n")
        # print(string)
    file.close()
    x = count_lines(file_name)
    with open(file_name, 'r',encoding="utf-8") as file:
        i=0
        j=1
        finish = 0
        list_poz=[]
        for line in file:
            k= j, finish
            str_poz=k,line.replace("\n",'')
            list_poz.append(str_poz)
            l=line
            file.seek(i)
            start = file.tell()
            file.readline()
            finish = file.tell()
            i =finish
            if file.tell() == os.path.getsize(file_name) - 1:
                break
            j += 1

    dict_data = {key: value for key, value in list_poz}
    return dict_data



result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)