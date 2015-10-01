"""
This module defines all room/space related classes.

"""

import settings
from persons import Person, Fellow


class Room(object):
    """
    Base class for the spaces module classes. 
    Implements functionality shared by the other space/room classes
    but is never instantiated by itself in the program.

    """

    # class-level variables:
    max_occupants = None
    

    def __init__(self, name):

        # set attribute:
        if(isinstance(name, str)):
            self.name = name
        else:
            raise TypeError("'name' parameter must be a string!")

        self.occupants = None
        self.purpose = None
        self.occupant_role = None
        self.occupant_gender = None
        self.occupants = []
    
    def add_occupant(self, person):
        """ Adds a person to the room's occupants list.
        Returns true if successful, False if not. """
        
        # ensure the room isn't over-allocated:
        if self.max_occupants and (len(self.occupants) >= self.max_occupants): 
            return False
        
        # ensure to add only Persons:
        if not isinstance(person, Person):
            return False
       
        # add person to occupant list and return:
        self.occupants.append(person)

        return True

    def add_occupants(self, persons):
        """ Adds a list of persons to the room's occupants list.
        Sublasses overide this method """

        if not isinstance(persons, list):
            return False

        for person in persons:
            self.add_occupant(person)

        return True

    @property
    def is_full(self):
        if len(self.occupants) < self.max_occupants:
            return False
        else:
            return True

    def __repr__(self):
        return self.name



class OfficeSpace(Room):
    """
    Class representing rooms to be used as office spaces. 
    Can take a maximum of 6 occupants and may also restrict 
    them to a particular role (Staff or Fellow) depending on
    the format of the input data.

    """
    # class-level variables:
    max_occupants = 6

    def __init__(self, name, occupant_role=None):
        
        # call the super __init__ with args:
        super(OfficeSpace, self).__init__(name)

        # set purpose:
        self.purpose = settings.OFFICE

        # set the occupant_role:
        if (
            occupant_role == settings.STAFF   or  
            occupant_role == settings.FELLOW  or 
            occupant_role == None
        ):
            self.occupant_role = occupant_role
        else:
            raise ValueError("Invalid value provided for attribute 'occupant_role'!")

    def __repr__(self):
        if self.occupant_role == None:
            return "{} ({})".format(self.name, self.purpose)
        else:
            return "{} ({} {})".format(self.name, self.purpose, self.occupant_role[0:2])



class LivingSpace(Room):
    """
    Class representing rooms to be used as living spaces. 
    Can take a maximum of 4 occupants and may also restrict 
    them to a particular gender (Male or Female) depending on
    the format of the input data.

    """
    # class-level variables:
    max_occupants = 4


    def __init__(self, name, occupant_gender=None):
        
        # call the super __init__ with args:
        super(LivingSpace, self).__init__(name)

        # set purpose:
        self.purpose = settings.LIVING

        # set the occupant_gender:
        if (
            occupant_gender == settings.MALE    or  
            occupant_gender == settings.FEMALE  or 
            occupant_gender == None
        ):
            self.occupant_gender = occupant_gender
        else:
            raise ValueError("Invalid value provided for attribute 'occupant_gender'!")

    def __repr__(self):

        if self.occupant_gender == None:
            return "{} ({})".format(self.name, self.purpose)
        else:
            return "{} ({} {})".format(self.name, self.purpose, self.occupant_gender[0:2])
