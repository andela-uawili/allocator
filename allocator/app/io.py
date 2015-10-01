""" 
This module defines functions and utilities for command and input parsing, output formatting and filesystem operations.

"""

import re
import os

import settings
from persons import Person, Staff, Fellow
from spaces import Room, OfficeSpace, LivingSpace


# regex matching patterns for inputs and commands:

person_input_line_pattern = re.compile(
    r"^(?P<name>[a-zA-Z\'-]+ [a-zA-Z\'-]+)\s+(?P<role>STAFF|FELLOW)(\s+(?P<wants_living>Y|N)?(\s+(?P<gender>M|F)?)?)?$"
)

room_input_line_pattern = re.compile(
    r"^(?P<name>[a-zA-Z\'-]+)\s+(?P<purpose>OFFICE|LIVING)(\s+(?P<occupant_role>STAFF|FELLOW))?(\s+(?P<occupant_gender>M|F))?$"
)

load_cmd_pattern = re.compile(
    r"^((?P<target>(rooms)|(team))(\s+'(?P<filepath>[\w .:/\-\\]+)')?(\s+:(?P<mode>o|a))?)?$"
)

input_cmd_pattern = re.compile(
    r"^(?P<target>(rooms)|(team))(\s+\'(?P<cslist>[a-zA-Z,'\s-]+)\')(\s+:(?P<mode>o|a))?$"
)

allocate_cmd_pattern = re.compile(
    r"^(\s+|(?P<gender_constraint>g\+|g-)|(?P<role_constraint>r\+|r-))*$"
)

output_cmd_pattern = re.compile(
    r"^(?P<target>(rooms)|(team))(\s+(?P<filters>(\s+|os|ls|st|fw|ml|fm|cf\+|cf-|oc\+|oc-|o\+|o-|l\+|l-|w\+|w-)+?))?(\s+'(?P<filepath>[\w .:/\-\\]+)')?(\s+:(?P<mode>o|a))?$"
)



# input parsing functions:


def parse_cmd_args(cmd_string, cmd_pattern):
    """ 
    handles parsing of the users' commands by re matching
    to extract the argumnets.

    """
    cmd_string.strip().lower()
    match = cmd_pattern.match(cmd_string)

    if match:
        cmd_args = match.groupdict()
        return cmd_args
    else:
        return None


def parse_person_input_line(input_line):
    """ 
    parses a single line of peron input data.

    """

    input_line = input_line.strip().upper()
    match = person_input_line_pattern.match(input_line)

    if match:
        line_data = match.groupdict()

        if line_data.get('role') == settings.STAFF:
            person = Staff(
                line_data.get('name')
            )
            return person

        elif line_data.get('role') == settings.FELLOW:
            person = Fellow(
                line_data.get('name'), 
                line_data.get('wants_living'), 
                gender = line_data.get('gender')
            )
            return person

    else:
        return None


def process_person_input_batch(input_batch):
    """ 
    processes a batch/list of peron input line data.

    """
    persons_list = [parse_person_input_line(input_line) for input_line in input_batch]
    return persons_list


def parse_room_input_line(input_line):
    """ 
    parses a single line of room input data.

    """
    input_line = input_line.strip().upper()
    match = room_input_line_pattern.match(input_line)

    if match:
        line_data = match.groupdict()

        if line_data.get('purpose') == settings.OFFICE:
            room = OfficeSpace(
                line_data.get('name'),
                occupant_role = line_data.get('occupant_role')
            )
            return room

        elif line_data.get('purpose') == settings.LIVING:
            room = LivingSpace(
                line_data.get('name'),
                occupant_gender = line_data.get('occupant_gender')
            )
            return room

    else:
        return None


def process_room_input_batch(input_batch):
    """ 
    parses a batch/list of room input lines

    """
    rooms_list = [parse_room_input_line(input_line) for input_line in input_batch]
    return rooms_list




# output formatting functions:


def format_room_output(room):
    """ 
    formats a room object into the intended string line output

    """
    room_str = str(room)
    occupants_str = ", ".join([str(occupant) for occupant in room.occupants])
    output_str = "{}\n{}".format(room_str, occupants_str)
    
    return output_str


def format_room_output_batch(output_batch, header=None):
    """ 
    formats a batch of room objects into the intended output

    """
    output_str = "\n"
    
    if header:
        output_str += "{}\n   {}\n{}\n\n".format(settings.OUTPUT_HEADER_DEMARC, header, settings.OUTPUT_HEADER_DEMARC)
        
    room_output_strs = [format_room_output(room) for room in output_batch]
    output_str += "\n\n".join(room_output_strs)
    output_str += "\n\n{} result(s)\n".format(len(output_batch))

    return output_str


def format_person_output_batch(output_batch, header=None):
    """ 
    formats a batch of person objects into the intended output

    """
    output_str = "\n"

    if header:
        output_str += "{}\n   {}\n{}\n\n".format(settings.OUTPUT_HEADER_DEMARC, header, settings.OUTPUT_HEADER_DEMARC)
        
    person_output_strs = [str(person) for person in output_batch]
    output_str += "\n\n".join(person_output_strs)
    output_str += "\n\n{} result(s)\n".format(len(output_batch))
    return output_str




# file-sytstem functions:


def read_input_lines_from_file(filepath):
    """ 
    reads input data as a list of lines from file

    """
    # if filepath is relative (to currently running script):
    if not os.path.isabs(filepath):
        filepath = os.path.abspath(filepath)

    try:
        file_obj = open(filepath, "r")
        lines = file_obj.readlines();
        lines = [line for line in lines if not re.match(r"^\s*$", line)]      # removes whitespace lines
        file_obj.close()
        return lines
    except:
        return None
    

def write_output_to_file(output_str, filepath, append=False):
    """ 
    writes output data to file

    """
    # if filepath is relative (to currently running script):
    if not os.path.isabs(filepath):
        filepath = os.path.abspath(filepath)

    try:
        write_mode =  'a' if append else 'w'
        file_obj = open(filepath, write_mode)
        file_obj.write(output_str);
        file_obj.close()
        return True
    except:
        return None

    