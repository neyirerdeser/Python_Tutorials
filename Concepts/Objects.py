import random
import sys
import os


# __ makes attributes private
# _  makes them protected, so the child classes can access
class Animal:
    _name = None  # or use "", same thing
    _height = 0
    _weight = 0
    _sound = 0

    # constructor
    def __init__(self, name, height, weight, sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_sound(self, sound):
        self._sound = sound

    def get_sound(self):
        return self._sound

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} kg and says {}".format(self._name,
                                                               self._height,
                                                               self._weight,
                                                               self._sound)


cat = Animal('pamuk', 33, 10, 'miyav')

print(cat.toString())


# inheritance

class Dog(Animal):
    _owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self._owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self._owner = owner

    def toString(self):
        return "{} is {} cm tall and {} kg and says {}. Owner is {}".format(self._name,
                                                                            self._height,
                                                                            self._weight,
                                                                            self._sound,
                                                                            self._owner)

    def get_type(self):
        print('Dog')

    def multiple_sounds(self, how_many=None):  # its okay not to pass the how_many argument
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


puppy = Dog("potat", 10, 1, "mlem", "daddo")
print(puppy.toString())


# polymorphism
class AnimalTest:
    def get_type(self, animal):
        animal.get_type()


test_animal = AnimalTest()
test_animal.get_type(cat)
test_animal.get_type(puppy)

puppy.multiple_sounds(4)
puppy.multiple_sounds()
