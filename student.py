from Animals import Human


class Student(Human):
    '''The students class has all the signs of people, but is different:
    The number of dz handed over
    '''

    def __init__(self, gender, age, sound, name, height, weight, dz):
        super().__init__(gender, age, height, weight, name, sound)
        self.dz = dz
    '''We overload the comparison operators
    for the students class to compare the number of dz passed
    '''

    def __lt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz < other_dz

    def __le__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz <= other_dz

    def __eq__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz == other_dz

    def __ne__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz != other_dz

    def __gt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz > other_dz

    def __ge__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz >= other_dz
