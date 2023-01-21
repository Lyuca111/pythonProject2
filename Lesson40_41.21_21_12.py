class Bottle:
    color = 'black'
    material = 'PET'
    volume = 1
    count_of_bottles = 0
    id = 1

    def open(self):
        print('Open bottle')
    def close(self):
        print('Close bottle')

    def __str__(self):
        return f'Volume : {self.volume} Material : {self.material} Color : {self.color.title()}'
    def __init__(self, name):
        self.name = name
        self.open()
        Bottle.count_of_bottles = Bottle.count_of_bottles + 1
        self.id = Bottle.id
        Bottle.id = Bottle.id +1

sause_bottle = Bottle('soja')
water_bottle = Bottle('mineral')
print(sause_bottle.id)
print(water_bottle.id)
print(Bottle.id)
print(Bottle.count_of_bottles)

print(sause_bottle.__class__.id)

#инкапсуляция
# public
# _protected
# __private


class Meetcut:
    color = 'grey'
    _produce_by = 'Germany'
    __series = 123456

    def __init__(self, color, produce_by):
        self.color = color
        self._produce_by = produce_by
        self.__series = Meetcut.__series
        Meetcut.__series = Meetcut.__series + 1
    def __str__(self):
        return f'Color : {self.color} Produce_by : {self._produce_by} Series : {self.__series}'

    def change_color(self, new_color):
        self.color = new_color
    def _change_produce_by(self, new_produce_by):
        self._produce_by = new_produce_by
    def __change_series(self, new_series):
        self.__series = new_series
Phillips = Meetcut('grey', 'Germany')
print(Phillips.color)
print(Phillips._produce_by)
print(Phillips._Meetcut__series)
print(Phillips)



