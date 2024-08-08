cars={"BMW":520000,"Audi":560000,"Honda": 450000,"Mazda": 501000,"Ford": 490231,"Audi Q9":1570000}
cars_1={}

priceList={}
for key in sorted(cars, key=cars.get, reverse=True):
    priceList[key] = cars[key]


print(priceList)

print(cars)
sorted_list = sorted(cars.items())
priceList={}
for key, value in sorted_list:
    priceList[key] = value
# for key in sorted(cars, key=cars.keys, reverse=True):
#     priceList[key] = cars[key]
#
#
print(priceList)

my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(my_dict.items())
sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value
print(sorted_dict)

# cars_1=sorted(cars_1, reverse=True)
# print(cars_1)
#cars_1.append(cars["BMW"])
#list_cars = sorted(cars_1)
#list_prices = sorted(priceList, reverse = True)

#print(list_cars)
#print(list_prices)

# my_str = 'bobbyhadz.com'
# result = my_str[:5]
# print(result)