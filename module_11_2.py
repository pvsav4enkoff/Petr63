from datetime import date
import inspect
import sys
class mainClass:

    def __init__(self,name,age,date_birthday):
        self.name = name
        self.age = age
        self.date_birthday = date_birthday


    def num_year(self):
        return f'{self.name} : {date.today().year-self.date_birthday.year}'


def introspection_info(obj):

    info = {}

    info['Тип'] = type(obj).__name__

    info['Атрибуты'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    info['Методы'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]

    if inspect.getmodule(obj):
        info['Модуль'] = inspect.getmodule(obj).__name__

    if inspect.isfunction(obj) or inspect.ismethod(obj):
        info['Сигнатура'] = str(inspect.signature(obj))

    if inspect.isclass(obj):
        info['Родители'] = [parent.__name__ for parent in obj.__bases__]

    return info

data_1=date(1963, 3, 15)
m= mainClass("Petr",61,data_1)
print(m.num_year())
print(introspection_info(42))
print(introspection_info('строка'))
print(introspection_info(data_1))
print(introspection_info(m))
print(introspection_info(introspection_info))
print(introspection_info.__code__.co_varnames)
print(introspection_info.__code__.co_varnames.__len__())
print(f'{introspection_info.__name__}  {introspection_info.__annotations__}')

