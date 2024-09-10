import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guest_age = [20, 25, 36, 41, 17, 12, 71, 58, 45, 56, 25, 9]

class Text_url_data:
    def get_post(self, *pl, url_post):
            return requests.post(url_post, data=pl)
    def data_frame(self,**data):
        return pd.DataFrame(data)

    def get_arange(self,start,stop,work,num):
        match work:
            case "**":
                return (np.arange(start, stop) ** num)
            case "*":
                return (np.arange(start, stop) * num)
            case "+":
                return (np.arange(start, stop) + num)
            case "-":
                return (np.arange(start, stop) - num)
            case _:
                print('Не известное действие.')
    def mean_min_max(self,*data):
        arr = np.array(data)
        return np.mean(arr), np.min(arr), np.max(arr)


tu=Text_url_data()
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
url_p = 'https://httpbin.org/post'
r1=tu.get_post(*payload_tuples,url_post=url_p)
print(r1.text)
print(r1.headers)


data1={"Имя": guests_names, "Возраст":guest_age}

r2=tu.data_frame(**data1)
print(r2)
df1 = pd.DataFrame({'Имя': ['Иван', 'Мария'],'Возраст': [25, 31]})
df2 = pd.DataFrame({'Имя': ['Петр', 'Сергей'],'Возраст': [42, 35]})

r3 = tu.data_frame(**df1)
r4 = tu.data_frame(**df2)
r5 = tu.data_frame(**data1)
df_concat = pd.concat([r3, r4, r5])
print(df_concat)

df_filtered = df_concat[df_concat['Возраст'] > 30]
print(df_filtered)


r6 = tu.get_arange(12,55,"*",3)
print(r6)
r5 = tu.get_arange(12,55,"**",3)
print(r5)
r5 = tu.get_arange(19,49,"-",3)
print(r5)
r6 = tu.get_arange(19,49,"+",3)
print(r6)
print(tu.mean_min_max(guest_age))
print(np.linspace(1, 5, 5))

for i in range(2):
    fig, ax = plt.subplots()
    ax.plot([random.randint(1, 10), random.randint(1, 10), random.randint(-5, 10), random.randint(-5, 10)],
            [random.randint(5, 10), random.randint(5, 10), random.randint(5, 10), random.randint(5, 10)])
    plt.show(block=False)
    plt.pause(2)
    plt.close()
for i in range(2):
    r5 = [random.randint(1, 10) for j in range(100)]
    r6 = [random.randint(5, 20) for j in range(100)]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(r5, r6, s=70, facecolor='C0', edgecolor='k')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

# b = np.matrix([[1, 2], [3, 4]])
# b_asarray = np.asarray(b)
for i in range(2):
    np.random.seed(19680801)  # seed the random number generator.
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.scatter('a', 'b', c='c', s='d', data=data)
    ax.set_xlabel('entry a')
    ax.set_ylabel('entry b')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

    img = Image.open('bird.JPG')
    img.save('bird2.jpg')
    img = img.resize((800, 600))
    img.save('bird3.jpg')

    img = Image.open('bird.JPG')
    img = img.filter(ImageFilter.BLUR)

    img.save('bird_blur.jpg')

    print(img.size)
    print(img.mode)

    img = Image.open('bird.jpg')

    draw = ImageDraw.Draw(img)

    draw.rectangle((100, 100, 300,300), fill='red')
    img = Image.new('RGB', (400, 300), color=(73, 109, 137))

    d = ImageDraw.Draw(img)

    ellipse_x0 = 50
    ellipse_y0 = 50
    ellipse_x1 = 350
    ellipse_y1 = 250

    # Рисование эллипса
    d.ellipse([(ellipse_x0, ellipse_y0), (ellipse_x1, ellipse_y1)], fill=(255, 255, 0))

    # Сохранение картинки
    img.save('ellipse.png')
