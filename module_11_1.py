import requests
import pandas as pd
import numpy as np


class Text_url_data:
    def get_post(self,*pl):
            return requests.post('https://httpbin.org/post', data=pl)
    def data_frame(self,**data):
        return pd.DataFrame(data)

n1=(np.arange(1,41)**2)
n2=(np.arange(42,82)-2)

# num = np.array(n1,n2)
print(n1)
print(n2)

tu=Text_url_data()
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1=tu.get_post(*payload_tuples)
print(r1.text)
print(r1.url)

data1 = {'Имя': ['Иван', 'Мария', 'Петр'],
        'Возраст': [25, 31, 42]}

r2=tu.data_frame(**data1)
print(r2)
df1 = pd.DataFrame({'Имя': ['Иван', 'Мария'],
                    'Возраст': [25, 31]})
df2 = pd.DataFrame({'Имя': ['Петр', 'Сергей'],
                    'Возраст': [42, 35]})

r3=tu.data_frame(**df1)
r4=tu.data_frame(**df2)
df_concat = pd.concat([df1, df2])
print(df_concat)
df_filtered = df_concat[df_concat['Возраст'] > 30]
print(df_filtered)
