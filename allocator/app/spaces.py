"""
This module defines all room/space related classes.

"""

from persons import Person, Fellow


class Room(object):
    """docstring for Room"""

    # class-level pseudo-constants:
    LIVING = 'LIVING'
    OFFICE = 'OFFICE'


    def __init__(self, name):

        # set name attribute:
        if(isinstance(name, str)):
            self.__name = name
        else:
            raise TypeError("'name' parameter must be a string!")

        # init the occupants list
        self.__occupants = []


    def add_occupant(self, person):
        """ Adds a person to the room's occupants list.
        Sublasses overide this method """
        
        return None

    def add_occupants(self, persons):
        """ Adds a list of persons to the room's occupants list.
        Sublasses overide this method """

        if not isinstance(persons, list):
            return False

        for person in persons:
            self.add_occupant(person)

        return True


    def __repr__(self):
        return self.name


    @property
    def name(self):
        return self.__name

    @property
    def occupants(self):
        return self.__occupants

    @property
    def occupant_role(self):
        return None

    @property
    def occupant_gender(self):
        return None



class OfficeSpace(Room):
    """docstring for OfficeSpace"""

    # class-level variables:
    max_occupants = 6

    def __init__(self, name, occupant_role=None):
        
        # call the super __init__ with args:
        super(OfficeSpace, self).__init__(name)

        # set purpose:
        self.__purpose = Room.OFFICE

        # set the occupant_role when required:
        if (
            occupant_role == Person.STAFF   or  
            occupant_role == Person.FELLOW  or 
            occupant_role == None
        ):
            self.__occupant_role = occupant_role
        else:
            raise ValueError("Invalid value provided for attribute 'occupant_role'!")


    def add_occupant(self, person):
        """ Adds a person to the room's occupants list.
        Returns true if successful, False if not. """
        
        # ensure the room isn't over-allocated:
        if len(self.occupants) >= OfficeSpace.max_occupants: 
            return False
        
        # ensure to add only Persons:
        if not (isinstance(person, Person)):
            return False
        
        # ensure correct occupant_role if specified:
        if not (self.__occupant_role == None or person.role == self.__occupant_role):
            return False
        
        # add person to occupant list and return:
        self.occupants.append(person)
        return True


    @property
    def purpose(self):
        return self.__purpose


    @property
    def occupant_role(self):
        return self.__occupant_role


    def __repr__(self):
        if self.occupant_role == None:
            return "{} ({})".format(self.name, self.purpose)
        else:
            return "{} ({} {})".format(self.name, self.purpose, self.occupant_role)



class LivingSpace(Room):
    """docstring for LivingSpace"""

    # class-level variables:
    max_occupants = 4


    def __init__(self, name, occupant_gender=None):
        
        # call the super __init__ with args:
        super(LivingSpace, self).__init__(name)

        # set purpose:
        self.__purpose = Room.LIVING

        # set the occupant_gender when required:
        if (
            occupant_gender == Fellow.MALE    or  
            occupant_gender == Fellow.FEMALE  or 
            occupant_gender == None
        ):
            self.__occupant_gender = occupant_gender
        else:
            raise ValueError("Invalid value provided for attribute 'occupant_gender'!")


    def add_occupant(self, person):
        """ Adds a person to the room's occupants list.
        Returns true if successful, False if not. """
        
        # ensure the room isn't over-allocated:
        if len(self.occupants) >= LivingSpace.max_occupants: 
            return False
        
        # ensure to add only Fellows:
        if not isinstance(person, Fellow):
            return False

        # ensure to add only Fellows with wants_living as Yes:
        if not (person.wants_living == Fellow.YES):
            return False

        # ensure correct occupant_gender if specified:
        if not (self.__occupant_gender == None or person.gender == self.__occupant_gender):
            return False
       
        # add person to occupant list and return:
        self.occupants.append(person)
        return True


    @property
    def purpose(self):
        return self.__purpose


    @property
    def occupant_gender(self):
        return self.__occupant_gender


    def __repr__(self):

        if self.occupant_gender == None:
            return "{} ({})".format(self.name, self.purpose)
        else:
            return "{} ({} {})".format(self.name, self.purpose, self.occupant_gender)
