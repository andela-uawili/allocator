"""
Application settings for Allocator. Includes default application behaviours, pseudo-constant definitions, etc.

"""


SPLASH = """
+-------------------------------------------------------------------------------------+
+                                                                                     +
+                           ALLOCATOR by Awili Uzochikwa                              +
+                                                                                     +
+-------------------------------------------------------------------------------------+
+                                                                                     +
+   Hello, welcome to Allocator, a command-based Room Allocation System               +
+   for Andela's Amity. Just type 'help' for a list of commands you can use.          +
+   Have fun!                                                                         +
+                                                                                     +
+-------------------------------------------------------------------------------------+
"""

OUTPUT_HEADER_DEMARC = "+------------------------------------------+"
DOCS_RULER = "-"


# prompts and formats

PROMPT = '\n:) '

INFO_FORMAT = ";) *** {} ***"
ERROR_FORMAT = ":( *** {} ***"


# messages

COMMMAND_ERROR_MSG = "Don't be naughty! That command doesn't exist. Type 'help' for the list of commands and their usage."
COMMMAND_ARGS_ERROR_MSG = "Oops! You used the command wrongly. You can try again tho."


# headers

DOC_HEADER = 'Allocator Help'
MISC_HEADER = 'Allocator:'
UNDOC_HEADER = 'Other:'


# pseudo-constant definitions:

OFFICE = 'OFFICE'
LIVING = 'LIVING'
STAFF = 'STAFF'
FELLOW = 'FELLOW'
MALE = 'M'
FEMALE = 'F'
YES = 'Y'
NO = 'N'

TEAM = 'team'
ROOMS = 'rooms'
OVERWRITE = 'o'
APPEND = 'a'
ROLE_SEP = 'r+'
NO_ROLE_SEP = 'r-'
GENDER_SEP = 'g+'
NO_GENDER_SEP = 'g-'

FILTER_OFFICE_SPACE = 'os'
FILTER_LIVING_SPACE = 'ls'
FILTER_STAFF = 'st'
FILTER_FELLOW = 'fw'
FILTER_MALE = 'ml'
FILTER_FEMALE  = 'fm'
FILTER_FULL_CAPACITY  = 'cf+'
FILTER_NOT_FULL_CAPACITY  = 'cf-'
FILTER_HAS_OCCUPANTS  = 'oc+'
FILTER_NO_OCCUPANTS  = 'oc-'
FILTER_HAS_OFFICE  = 'o+'
FILTER_HAS_NO_OFFICE  = 'o-'
FILTER_HAS_LIVING  = 'l+'
FILTER_HAS_NO_LIVING  = 'l-'
FILTER_WANTS_LIVING  = 'w+'
FILTER_WANTS_NO_LIVING  = 'w-'


# default settings:

DEFAULT_LOAD_TEAM_PATH = "./data/input_persons_ext.txt"
DEFAULT_LOAD_ROOMS_PATH = "./data/input_rooms_ext.txt"
DEFAULT_OUTPUT_PATH = "./data/output.txt"

DEFAULT_LOAD_MODE = OVERWRITE
DEFAULT_INPUT_MODE = OVERWRITE
DEFAULT_SAVE_MODE = OVERWRITE

DEFAULT_ROLE_CONSTRAINT = ROLE_SEP
DEFAULT_GENDER_CONSTRAINT = GENDER_SEP


