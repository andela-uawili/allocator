""" 
This module defines functions and utilities for command and input parsing, output formatting and filesystem operations.

"""

import re

from persons import Person, Staff, Fellow
from spaces import Room, OfficeSpace, LivingSpace
from settings import OUTPUT_HEADER_DEMARC




# regex matching patterns for inputs and commands:


person_input_line_pattern = re.compile(
    r"^(?P<name>[a-zA-Z\'-]+ [a-zA-Z\'-]+)\s+(?P<role>STAFF|FELLOW)(\s+(?P<wants_living>Y|N)?(\s+(?P<gender>M|F)?)?)?$"
)

room_input_line_pattern = re.compile(
    r"^(?P<name>[a-zA-Z\'-]+)\s+(?P<purpose>OFFICE|LIVING)(\s+(?P<occupant_role>STAFF|FELLOW))?(\s+(?P<occupant_gender>M|F))?$"
)

load_cmd_pattern = re.compile(
    r"^(('(?P<filepath>[\w .:/\-\\]+)')?(\s+)?(\s+:(?P<mode>o|a))?)?$"
)

input_cmd_pattern = re.compile(
    r"^\'(?P<cslist>[a-zA-Z,'\s-]+)\'(\s+:(?P<mode>o|a))?$"
)

allocate_cmd_pattern = re.compile(
    r"^(\s+|(?P<sep_gender>g\+|g-)|(?P<sep_roles>r\+|r-))*$"
)

output_cmd_pattern = re.compile(
    r"^(?P<query>(roomdir)|(teamdir))(\s+(?P<filters>(\s+|(os)|ls|(oss)|(osf)|lsm|lsf|c\+|c-|s|f|fm|ff|(o\+)|(o-)|l\+|l-)+))?(\s+:(?P<mode>o|a))?$"
)



# input parsing functions:


def parse_cmd_args(cmd_string, cmd_pattern):

    cmd_string.strip()
    match = cmd_pattern.match(cmd_string)

    if match:
        cmd_args = match.groupdict()
        return cmd_args
    else:
        return None


def parse_person_input_line(input_line):

    input_line = input_line.strip()
    match = person_input_line_pattern.match(input_line)

    if match:
        line_data = match.groupdict()

        if line_data.get('role') == Person.STAFF:
            person = Staff(
                line_data.get('name')
            )
            return person

        elif line_data.get('role') == Person.FELLOW:
            person = Fellow(
                line_data.get('name'), 
                line_data.get('wants_living'), 
                gender = line_data.get('gender')
            )
            return person

    else:
        return None


def process_person_input_batch(input_batch):

    persons_list = [parse_person_input_line(input_line) for input_line in input_batch]
    return persons_list


def parse_room_input_line(input_line):

    input_line = input_line.strip()
    match = room_input_line_pattern.match(input_line)

    if match:
        line_data = match.groupdict()

        if line_data.get('purpose') == Room.OFFICE:
            room = OfficeSpace(
                line_data.get('name'),
                occupant_role = line_data.get('occupant_role')
            )
            return room

        elif line_data.get('purpose') == Room.LIVING:
            room = LivingSpace(
                line_data.get('name'),
                occupant_gender = line_data.get('occupant_gender')
            )
            return room

    else:
        return None


def process_room_input_batch(input_batch):

    rooms_list = [parse_room_input_line(input_line) for input_line in input_batch]
    return rooms_list



# output formatting functions:


def format_room_output(room):

    room_str = str(room)
    occupants_str = ", ".join([str(occupant) for occupant in room.occupants])
    output_str = "{}\n{}".format(room_str, occupants_str)
    
    return output_str


def format_room_output_batch(output_batch, header=None):
    
    output_str = "\n"
    
    if header:
        output_str += "{}\n   {}\n{}\n\n".format(OUTPUT_HEADER_DEMARC, header, OUTPUT_HEADER_DEMARC)
        
    room_output_strs = [format_room_output(room) for room in output_batch]
    output_str += "\n\n".join(room_output_strs)
    
    return output_str


def format_person_output_batch(output_batch, header=None):
    
    output_str = "\n"

    if header:
        output_str += "{}\n   {}\n{}\n\n".format(OUTPUT_HEADER_DEMARC, header, OUTPUT_HEADER_DEMARC)
        
    person_output_strs = [str(person) for person in output_batch]
    output_str += "\n\n".join(person_output_strs)

    return output_str




# file-sytstem functions:


def read_input_lines_from_file(filepath):
    
    file_obj = open(filepath, "r")
    lines = file_obj.readlines();
    file_obj.close()
    
    return lines


def write_output_to_file(output_str, filepath, append=False):
    
    write_mode =  'a' if append else 'w'
    file_obj = open(filepath, write_mode)
    file_obj.write(output_str);
    file_obj.close()