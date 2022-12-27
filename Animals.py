class Animals:
    '''A class of animals that are described by the following characteristics:
    Age, habitat, sounds
    '''
    def __init__(self, age, habitat, sound):
        self.age = age
        self.habitat = habitat
        self.sound = sound

class Mammals(Animals):
    '''The mammalian class inherits animal traits and is different:
    Gender and the presence or absence of wool
    '''
    def __init__(self, age, habitat, sound, gender, wool):
        super().__init__(age, habitat, sound)
        self.gender = gender
        self.wool = wool 
        
class Human(Mammals):
    '''The human class inherits the characteristics of mammals and is different:
    Name, height and weight
    '''
    def __init__(self, gender, age, sound, name, height, weight):
        super().__init__(gender, age, sound)
        self.name = name
        self.height = height
        self.weight = weight
    
    def say(self, text):
        print(text)

    def say_age(self):
        if self.gender == 'male':
            print(f'My age is {self.age}')
        else:
            print('No')

class Dog(Mammals):
    '''The dog class inherits the characteristics of mammals and is different:
    Name, breed and loyalty
    '''
    def __init__(self, gender, age, sound, wool, habitat, name, breed, loyality):
        super().__init__(age, habitat, sound, gender, wool)
        self.name = name
        self.breed = breed
        self.loyality = loyality

    def info(self):
        print(f"I'm dog. My breed is {self.breed}")

    def make_sound(self):
        print('gaf')

class Cat(Mammals):
    '''The cat class inherits the characteristics of mammals and is different:
    Name, breed and cunning
    '''
    def __init__(self, gender, age, sound, wool, habitat, name, breed, cunning):
        super().__init__(age, habitat, sound, gender, wool)
        self.name = name
        self.breed = breed
        self.cunning = cunning
            
    def info(self):
        print(f"I'm cat. My breed is {self.breed}")

    def make_sound(self):
        print('meow')