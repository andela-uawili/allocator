"""
This module defines all person related classes.

"""

import settings


class Person(object):
    """
    Base class for the persons module classes. 
    Implements functionality shared by the other person classes
    but is never instantiated by itself in the program.

    """

    def __init__(self, name):

        # set name attribute:
        if(isinstance(name, str)):
            self.name = name
        else:
            raise TypeError("'name' parameter must be a string!")

        self.role = None
        self.gender = None
        self.wants_living = None

        # initialize space allocations:
        self.office_space = None
        self.living_space = None

    def __repr__(self):
        return self.name



class Staff(Person):
    """
    Class representing persons that are staff. 
    Staff cannot be assigned to living spaces.

    """

    def __init__(self, name):
        
        super(Staff, self).__init__(name)
        self.role = settings.STAFF

    def __repr__(self):

        return "{} ({})".format(self.name, self.role)



class Fellow(Person):
    """
    Class representing person that are Fellows. 
    Fellows can be assigned living spaces if they 
    so choose. And may have their gender defined in the input data.

    """


    def __init__(self, name, wants_living, gender=None):

        super(Fellow, self).__init__(name)
        self.role = settings.FELLOW

        # set the wants_living option:
        if (
            wants_living == settings.YES  or
            wants_living == settings.NO
        ):
            self.wants_living = wants_living
        else:
            raise ValueError("Invalid value provided for attribute 'wants_living'!")

        # set the gender when required:
        if (
            gender == settings.MALE    or  
            gender == settings.FEMALE  or 
            gender == None
        ):
            self.gender = gender
        else:
            raise ValueError("Invalid value provided for attribute 'gender'!")

    def __repr__(self):

        if self.gender == None:
            return "{} ({})".format(self.name, self.role)
        else:
            return "{} ({} {})".format(self.name, self.role, self.gender)