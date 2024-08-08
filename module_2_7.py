def print_params(a = 1, b = 'строка', c = True):
    if a is None:
        a = 'not none'

    print(a, b, c)

print('1) -----------')
print_params(b = 25)
print_params(a = None)
print_params(c = [1,2,3])

print('\n2) -----------')
values_list = ['12-25','строка',True]
values_dict = {'a': 3.14,'b': 'строка-2','c': [7,40]}
print_params(*values_list)
print_params(**values_dict)


print('\n3) -----------')
values_list_2 = [54.32, 'Строка-3']
print_params(*values_list_2,8)
