from pprint import pprint
class Product:
    def __init__(self,name,weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return self.name+", "+str(self.weight)+", "+self.category
        pass

    pass
class Shop(Product):
    __file_name = 'products.txt'
    def __init__(self):
        self.listprod = []
    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products
    def count_lines(self,filename):
        with open(filename, 'r') as file:
            i = sum(1 for _ in file)
            file.close()
        return i

    def add(self, *products):
        add_prod = []
        if self.count_lines(self.__file_name) == 0:
            file = open(self.__file_name, 'a')
            for product in products:
                file.write(f"{str(product)}\n")
                add_prod.append(product.name)
                break
            file.close()

        existing_products = set(product.name for product in self.get_products_2())
        i=0

        for product in products:
            if product.name not in existing_products:
                with open(self.__file_name, 'a') as file:
                        file.write(f"{str(product)}\n")
                        break
            else:
                print(f"Продукт {product.name} уже есть в магазине")
            i=i+1
    def get_products_2(self):
        with open(self.__file_name, 'r') as file:
            lines = file.readlines()
        products = []
        for line in lines:
            name, weight, category = line.strip().split(', ')
            products.append(Product(name, float(weight), category))
        file.close()
        return products


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())