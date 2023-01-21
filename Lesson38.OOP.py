# Класс - это инструкция, чертеж, набор правил для создания объекта
class Borsch:
    meat = 'beef' #поле класса, атрибут класса, аргумент, параметр, переменнач класса
    volume = 2 # поле класса отвечает на вопрос что? кто?
    ingredients = ['beet', 'potato', 'cabbage', 'carrot']
    color = ['red', 'green']
    type = ['with meet', 'without meet']
    @staticmethod
    def add_ingredients(new_ingredient):
        Borsch.ingredients.append(new_ingredient)
    @staticmethod
    def remove_ingredients(del_ingredients):
        Borsch.ingredients.remove(del_ingredients)

    def boiled(self): #метод класса, функция класса что делать? что сделать?
        print('We boiled borsch')

    def salted(self):
        print('we salted borsch')

    def stew(self):
        print('we stew borsch')

    def nalivay(self):
        print('we nalivay borsch')

    def show_meat(self):
        print(self.meat)
    def change_meat(self,new_meat):
        self.meat = new_meat

Borsch.add_ingredients('tomato')
Borsch.remove_ingredients('carrot')
odessa_borsch = Borsch() #объект класса
print(odessa_borsch.ingredients)
#
# poltava_borsch = Borsch()
# dnepr_borsch = Borsch()

# print(odessa_borsch.meat)
# print(poltava_borsch.meat)
# odessa_borsch.meat = 'chicken'
# poltava_borsch.meat = 'turkey'
# print(odessa_borsch.meat)
# print(poltava_borsch.meat)
# print(dnepr_borsch.meat)

# odessa_borsch.show_meat()
# poltava_borsch.show_meat()
# odessa_borsch.change_meat = 'chicken'
# poltava_borsch.change_meat = 'turkey'
# odessa_borsch.show_meat()
# poltava_borsch.show_meat()
# dnepr_borsch.show_meat()
#
# class Person:
#     name = 'Jonn Wyk'
#     birth = ['1980.03.14']
#     phone  = '55555'
#     country = 'USA'
#     city = 'New York'
#
#     def work(self):
#         print('person is working')
#     def walk(self):
#         print('person is walking')
#     def sleep(self):
#         print('person is sleeping')
#
#     def show_name(self):
#         print(self.name)
#
#     def change_name(self,new_name):
#         self.name = new_name
#
# Adam_person = Person
# Eva_person = Person
# print(Adam_person.name)
# print(Eva_person.name)
#
# Adam_person.show_name()
# Eva_person.show_name()
# Adam_person.change_name = 'Ron Yizli'
# Adam_person.show_name()

class Bottle:
    color = 'black'
    material = 'PET'
    volume = 1

    def open(self):
        print('Open bottle')
    def close(self):
        print('Close bottle')

    def __str__(self):
        return f'Volume : {self.volume} Material : {self.material} Color : {self.color.title()}'

sause_bottle = Bottle()
water_bottle = Bottle()
print(sause_bottle)