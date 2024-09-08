import requests
import pandas as pd
import numpy as np


class Text_url:
    def __init__(self,*n10):
        self.n10=n10
    def get_post(self,*n_2):
            return requests.post('https://httpbin.org/post', data=n_2)
            # print(rs.text)


# Создание DataFrame из словаря
data = {'Имя': ['Иван', 'Мария', 'Петр'],
        'Возраст': [25, 31, 42]}
df = pd.DataFrame(data)
print(df)
# Объединение двух DataFrame
df1 = pd.DataFrame({'Имя': ['Иван', 'Мария'],
                    'Возраст': [25, 31]})
df2 = pd.DataFrame({'Имя': ['Петр', 'Сергей'],
                    'Возраст': [42, 35]})
df_concat = pd.concat([df1, df2])
print(df_concat)
# Загрузка данных из CSV-файла
# Фильтрация данных по условию
df_filtered = df[df['Возраст'] > 30]
print(df_filtered)
n1=(np.arange(1,41)**2)
n2=(np.arange(42,82)-2)

# num = np.array(n1,n2)
print(n1)
print(n2)
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1=Text_url.get_post(*payload_tuples)
print(r1.text)
print(r1.url)
