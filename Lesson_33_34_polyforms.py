class Worker:
    qualification = 'worker'
    worker_level = 1
    def work(self):
        if self.qualification == 'worker':
            print('Do work!')
        elif self.qualification == 'builder':
            print('Do something!')
        elif self.qualification == 'sailor':
                print('Do sailing!')

class Builder(Worker):
    qualification = 'builder'
    builder_level = 1
    def build(self):
        print('Do something!')

class Sailor(Worker):
    qualification = 'sailor'
    sail_level = 1
    def sail(self):
        print('Do sailing!')

class SeaBuilder(Sailor, Builder):
    pass

bender = Builder()
papai = Sailor()
bender.work()
bender.build()
print(bender.qualification)
papai.sail()
print(papai.qualification)

seal = SeaBuilder()
print(seal.qualification)
seal.sail()
seal.work()
bender.work()
papai.work()



class Passport:
    name = 'Agatha'
    second_name = 'Christie'
    fathers_name = 'Johnovna'
    birth_date = '1890_09_15'
    def nation(self):
        print('English Passport')

class ForeignPassport(Passport):
    passport_number = '11111'
    visas = 'Canada, Hungary'
    def foreign(self):
        print('Foreign Passport')


writer = ForeignPassport()
print(writer.fathers_name)


class Borsch:
    meat = 'beef'
    volume = 2
    ingredients = ['beet', 'potato', 'cabbage', 'carrot']
    main_ingredient = 'beet'
    color = ['red', 'green']
    type = ['with meet', 'without meet']
    @staticmethod
    def add_ingredients(new_ingredient):
        Borsch.ingredients.append(new_ingredient)
    @staticmethod
    def remove_ingredients(del_ingredients):
        Borsch.ingredients.remove(del_ingredients)

    def colored(self, main_ingredient):
        if main_ingredient == 'beet':
            self.color = 'red'
        elif main_ingredient == 'dock':
            self.color = 'green'
        elif main_ingredient == 'yellow tomato':
            self.color = 'yellow'

    def boiled(self):
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

