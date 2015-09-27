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
        Person.__init__(self, name)

        # set role:
        self.__role = Person.STAFF


    @property
    def role(self):
        return self.__role


    def __repr__(self):
        return "{} [{}]".format(self.name, self.role)




class Fellow(Person):
    """docstring for Fellow"""

    # class-level pseudo-constants:
    MALE = 'M'
    FEMALE = 'F'
    YES = 'Y'
    NO = 'N'

    # class-level variables:
    gender_aware = False


    def __init__(self, name, **kwargs):

         # call the super __init__:
        Person.__init__(self, name)

        # set role:
        self.__role = Person.FELLOW

        # set the gender when required:
        if Fellow.gender_aware:
            gender = kwargs.get('gender')
            if (gender == Fellow.MALE  or  gender == Fellow.FEMALE) :
                self.__gender = gender
            else:
                raise ValueError("Invalid value provided for attribute 'gender'!")

        # set the wants_living_space option:
        wants_living_space = kwargs.get('wants_living_space')
        if (wants_living_space == Fellow.YES  or wants_living_space == Fellow.NO) :
            self.__wants_living_space = wants_living_space
        else:
            raise ValueError("Invalid value provided for attribute 'wants_living_space'!")


    @property
    def role(self):
        return self.__role


    @property
    def gender(self):
        return self.__gender


    @property
    def wants_living_space(self):
        return self.__wants_living_space


    def __repr__(self):
        if Fellow.gender_aware:
            return "{} [{} {}]".format(self.name, self.role, self.gender)
        else:
            return "{} [{}]".format(self.name, self.role)