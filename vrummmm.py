class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__years_of_use = self.__use()
    def __use(self):
        return 2024 - self.__year
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def __repr__(self):
        return f'{self.__brand} {self.__model}, {self.__years_of_use} anos de uso'

car = Car(input().strip(),input().strip(),int(input()))
print(car)
