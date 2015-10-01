"""
This module defines all allocation/manager related classes.

"""

import settings
import io
from persons import Person, Fellow
from spaces import OfficeSpace, LivingSpace
from math import floor 
from random import uniform 


class FacilityManager(object):
    """
    Handles all facility level tasks like managing the 
    team and room directories, allocation, etc

    """

    def __init__(self):

        # initialize data dirs to empty lists:
        self.teamdir = []
        self.roomsdir = []



    def load(self, target=None, filepath=None, mode=None):
        """ 
        Loads 'team' or 'rooms' data from text files for processing.

        """
        # set mode default:
        mode = mode if mode else settings.DEFAULT_LOAD_MODE
        
        # load data based on target:
        if target == settings.TEAM or target == None:

            # set filepath default:
            persons_filepath = filepath if filepath else settings.DEFAULT_LOAD_TEAM_PATH
            # load the data as a batch:
            input_batch = io.read_input_lines_from_file(persons_filepath)
            # process team data:
            success = self.process_input_to_target(settings.TEAM, input_batch, mode)

        if target == settings.ROOMS or target == None:

            # set filepath default:
            rooms_filepath = filepath if filepath else settings.DEFAULT_LOAD_ROOMS_PATH
            # load the data as a batch:
            input_batch = io.read_input_lines_from_file(rooms_filepath)
            # process room data
            success = self.process_input_to_target(settings.ROOMS, input_batch, mode)

        return success



    def input(self, target, cslist, mode=None):
        """ 
        collects 'team' or 'rooms' data from commandline for processing.

        """
        # set mode default:
        mode = mode if mode else settings.DEFAULT_INPUT_MODE

        # pre-process the data into a batch:
        input_batch = cslist.split(",")
        
        # load data based on target:
        if target == settings.TEAM:
            # process team data
            success = self.process_input_to_target(settings.TEAM, input_batch, mode)

        elif target == settings.ROOMS:
            # process room data
            success = self.process_input_to_target(settings.ROOMS, input_batch, mode)

        return success



    def process_input_to_target(self, target, input_batch, mode):
        """  
        Processes loaded/inputed data to populate either the 'team' and/or 'rooms' lists.

        """
        if isinstance(input_batch, list):

            if target == settings.TEAM:
                loaded_list = io.process_person_input_batch(input_batch)

                if mode == settings.OVERWRITE:
                    self.teamdir = loaded_list

                elif mode == settings.APPEND:
                    self.teamdir.extend(loaded_list)

            elif target == settings.ROOMS:
                loaded_list = io.process_room_input_batch(input_batch)

                if mode == settings.OVERWRITE:
                    self.roomsdir = loaded_list

                elif mode == settings.APPEND:
                    self.roomsdir.extend(loaded_list)

            return True
        else: 
            return False



    def allocate(self, gender_constraint=None, role_constraint=None):
        """ 
        Allocates persons to rooms using optional or default constraints.

        """
        for person in self.teamdir:
            if not person.office_space:
                self.assign_person_to_office_space(person, role_constraint)
            if not person.living_space:
                self.assign_person_to_living_space(person, gender_constraint)

        return True



    def assign_person_to_office_space(self, person, role_constraint=None):
        """ 
        assigns persons randomly to suitable office spaces

        """

        #  validate person type before proceeding:
        if not isinstance(person, Person):
            return False

        # set role_constraint default:
        role_constraint = role_constraint if role_constraint else settings.DEFAULT_ROLE_CONSTRAINT
        
        # get the list of office spaces suitable for this person based on constraints:

        def is_suitable_office(room):
            if room.purpose != settings.OFFICE:
                return False
            if room.is_full:
                return False
            if role_constraint == settings.ROLE_SEP:

                if room.occupant_role != person.role and room.occupant_role != None:
                    return False
            # otherwise:
            return True

        suitable_offices = filter(is_suitable_office, self.roomsdir)

        # confirm there are suitable-offices before proceeding:
        if not len(suitable_offices):
            return False

        # randomly select one from suitable_offices:
        random_index = int(floor(uniform(0, len(suitable_offices))))
        random_suitable_office = suitable_offices[random_index]
        
        # add person to the chosen office:
        random_suitable_office.add_occupant(person)
        person.office_space = random_suitable_office

        return True



    def assign_person_to_living_space(self, person, gender_constraint=None):
        """ 
        assigns persons randomly to suitable living spaces

        """
        #  validate person type before proceeding:
        if not isinstance(person, Fellow):
            return False
        if person.wants_living != settings.YES:
            return False
            
        # set gender_constraint default:
        gender_constraint = gender_constraint if gender_constraint else settings.DEFAULT_GENDER_CONSTRAINT
        
        # get the list of living spaces suitable for this person based on constraints:
        
        def is_suitable_living(room):
            if room.purpose != settings.LIVING:
                return False
            if room.is_full:
                return False
            if gender_constraint == settings.GENDER_SEP:
                if room.occupant_gender != person.gender and room.occupant_gender != None:
                    return False
            # otherwise:
            return True

        suitable_livings = filter(is_suitable_living, self.roomsdir)

        # confirm there are suitable_livings before proceeding:
        if not len(suitable_livings):
            return False

        # randomly select one from suitable_livings:
        random_index = int(floor(uniform(0, len(suitable_livings))))
        random_suitable_living = suitable_livings[random_index]
        
        # add person to the chosen living space:
        random_suitable_living.add_occupant(person)
        person.living_space = random_suitable_living

        return True



    def print_to_console(self, target, filters=None):
        """ 
        handles output of team or room data to standard output

        """
        if target == settings.TEAM:
            print self.output_persons(filters)

        elif target == settings.ROOMS:
            print self.output_rooms(filters)

        return True



    def save_to_file(self, target, filters=None, filepath=None, mode=None):
        """ 
        handles saving of team or room data to file system

        """
        # set mode default:
        mode = mode if mode else settings.DEFAULT_SAVE_MODE
        append = True if mode == settings.APPEND else False

        # set filepath default:
        filepath = filepath if filepath else settings.DEFAULT_OUTPUT_PATH

        if target == settings.TEAM:
            success = io.write_output_to_file(self.output_persons(filters), filepath, append)

        elif target == settings.ROOMS:
            success = io.write_output_to_file(self.output_rooms(filters), filepath, append)

        return success



    def output_persons(self, filters=None):
        """ 
        handles filtering and formatting of team data queries

        """
        if filters:
            def is_team_filter_match(person):

                if (
                    filters.find(settings.FILTER_STAFF) > -1                and
                    person.role != settings.STAFF
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_FELLOW) > -1               and
                    person.role != settings.FELLOW
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_MALE) > -1                 and
                    person.gender != settings.MALE                   and               
                    person.gender != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_FEMALE) > -1               and
                    person.gender != settings.FEMALE                        and
                    person.gender != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_HAS_OFFICE) > -1           and
                    not isinstance(person.office_space, OfficeSpace)
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_HAS_NO_OFFICE) > -1        and
                    isinstance(person.office_space, OfficeSpace)
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_HAS_LIVING) > -1           and
                    not isinstance(person.living_space, LivingSpace)
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_HAS_NO_LIVING) > -1        and
                    isinstance(person.living_space, LivingSpace)
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_WANTS_LIVING) > -1         and
                    person.wants_living != settings.YES
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_WANTS_NO_LIVING) > -1      and
                    person.wants_living != settings.NO
                    ):
                    return False

                # otherwise:
                return True

            output_batch = filter(is_team_filter_match, self.teamdir)

        else:
            output_batch = self.teamdir

        header = "Allocator Print: Team (Filters: {})".format(filters)
        output_str = io.format_person_output_batch(output_batch, header)
        
        return output_str



    def output_rooms(self, filters=None):
        """ 
        handles filtering and formatting of room data queries

        """
        if filters:
            def is_room_filter_match(room):

                if (
                    filters.find(settings.FILTER_OFFICE_SPACE) > -1  and
                    room.purpose != settings.OFFICE
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_LIVING_SPACE) > -1  and
                    room.purpose != settings.LIVING
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_STAFF) > -1         and
                    room.occupant_role != settings.STAFF            and
                    room.occupant_role != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_FELLOW) > -1        and
                    room.occupant_role != settings.FELLOW            and
                    room.occupant_role != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_MALE) > -1          and
                    room.occupant_gender != settings.MALE            and
                    room.occupant_gender != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_FEMALE) > -1        and
                    room.occupant_gender != settings.FEMALE          and
                    room.occupant_gender != None
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_FULL_CAPACITY) > -1       and
                    not (room.is_full)
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_NOT_FULL_CAPACITY) > -1   and
                    room.is_full
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_HAS_OCCUPANTS) > -1       and
                    not (len(room.occupants))
                    ):
                    return False
                if (
                    filters.find(settings.FILTER_NO_OCCUPANTS) > -1   and
                    (len(room.occupants))
                    ):
                    return False

                # otherwise:
                return True

            output_batch = filter(is_room_filter_match, self.roomsdir)

        else:
            output_batch = self.roomsdir

        header = "Allocator Print: Rooms (Filters: {})".format(filters)
        output_str = io.format_room_output_batch(output_batch, header)
        
        return output_str
            
