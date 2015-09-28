"""
This module defines all person related classes.

"""


class Person(object):
    """docstring for Person"""

    # class-level pseudo-constants:
    STAFF = 'STAFF'
    FELLOW = 'FELLOW'


    def __init__(self, name):

        # set name attribute:
        if(isinstance(name, str)):
            self.__name = name
        else:
            raise TypeError("'name' parameter must be a string!")


    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self.__name




class Staff(Person):
    """docstring for Staff"""

    def __init__(self, name):
        
        # call the super __init__:
        super(Staff, self).__init__(name)

        # set role:
        self.__role = Person.STAFF


    @property
    def role(self):
        return self.__role


    def __repr__(self):
        return "{} ({})".format(self.name, self.role)




class Fellow(Person):
    """docstring for Fellow"""

    # class-level pseudo-constants:
    MALE = 'M'
    FEMALE = 'F'
    YES = 'Y'
    NO = 'N'

    def __init__(self, name, wants_living, gender=None):

        # call the super __init__:
        super(Fellow, self).__init__(name)

        # set role:
        self.__role = Person.FELLOW

        # set the wants_living option:
        if (
            wants_living == Fellow.YES  or
            wants_living == Fellow.NO
        ):
            self.__wants_living = wants_living
        else:
            raise ValueError("Invalid value provided for attribute 'wants_living'!")

        # set the gender when required:
        if (
            gender == Fellow.MALE    or  
            gender == Fellow.FEMALE  or 
            gender == None
        ):
            self.__gender = gender
        else:
            raise ValueError("Invalid value provided for attribute 'gender'!")


    @property
    def role(self):
        return self.__role


    @property
    def gender(self):
        return self.__gender


    @property
    def wants_living(self):
        return self.__wants_living


    def __repr__(self):

        if self.gender == None:
            return "{} ({})".format(self.name, self.role)
        else:
            return "{} ({} {})".format(self.name, self.role, self.gender)