# Allocator [![Build Status](https://travis-ci.org/andela-uawili/amity-room-allocation.svg?branch=master)](https://travis-ci.org/andela-uawili/amity-room-allocation)
Python program to allocate people to rooms in Andela's Amity.

## Installation
1. Clone the repo to any directory on your PC from which you can run python (preferrably with a virtual environment). 
2. Run `pip install -r requirements.txt` to install all dependencies.
3. Finally run `python allocator.py` and voila! Start allocating! 

The program is should guide you from there but if not, feel free to use the help command anytime. 

## Testing
1. Run the following command in the root program's root package: `nosetests`
2. To test with coverage reports: `nosetests --with-coverage --cover-package=allocator`

## Usage
This application runs as a command interpreter.

1. Typically you start by loading or inputing data for teams and rooms. (NOTE: There are defaults for this, you only need call the bare minimum commands without any arguments).   
2. Next you run the 'allocate' command to allocate person to rooms.   
3. Finally you can query for room or team allocation data and 'print' it to the console or 'save' to a file.   

## Commands:
See below for the list of commands and their usage:

#### LOAD        
Loads data from text files to populate either the 'team' or 'rooms'. Has the format:  
`load  [<target>(team|rooms)  ['<filepath>'] ]  [<mode>(:o|:a)]`   
* __target__:   
The target data to populate. Value can be either `team` or `rooms`. Note that although setting target is optional, the other options have no effect unless it is specified. Calling load without target loads both rooms and teams with the default filepath and mode settings.   
* __filepath__:   
Optional. Path to the input file wrapped in single-quotes `''`. Can be absolute or relative. Defaults to '/data/input_persons_ext.txt' for team and '/data/input_rooms_ext.txt' for rooms.   
* __mode:__   
Optional. Specifies how the data is added to target.   
 `:o` to overwrite previously loaded data.   
 `:a` to append to previously loaded data.    
Defaults to `:o`.    

  __Examples:__        
  `load team './data/input_persons_ext.txt' :a`   
  `load rooms`   



#### INPUT
Collects data from command line to populate either the 'team' or 'rooms'. Has the format:   
`input  <target>(team|rooms)  '<cslist>'   [<mode>(:o|:a)]`
* __target:__   
The target data to populate. Value can be either `team` or `rooms`. Note that although setting target is optional, the other options have no effect unless it is specified. Calling load without target loads both rooms and teams with the default filepath and mode settings.
* __cslist:__   
Comma seperated list of input lines for persons or rooms wrapped in single-quotes `''`.
* __mode:__   
Optional. Specifies how the data is added to target.   
 `:o` to overwrite previously loaded data.   
 `:a` to append to previously loaded data.    
Defaults to `:a`.

  __Examples:__          
  `input team 'ANDREW PHILLIPS FELLOW Y M, MATTHEW O'CONNOR STAFF' :o `   
  ` input room 'HAMMER  OFFICE  STAFF, SAPELE LIVING F' `    



#### ALLOCATE
Allocates persons to rooms using optional or default constraints. Has the format:   
`allocate  [<sep_gender>(g+|g-)]  [<sep_roles>(r+|r-)]`
* __sep_gender:__   
Optional. Specifies whether genders should be separated when allocating fellows to living spaces.   
`g+` to seperate genders.   
`g-` to allow different genders to share living spaces. _lol...in your dreams ;)_    
Defaults to `g+`.
* __sep_roles:__    
Optional. Specifies whether roles (staff and fellows) should be separated when allocating persons to office spaces.   
`r+` to seperate roles.   
`r-` to allow staff and fellows to share office spaces. Not bad huh?   
Defaults to `r+`.   

  __Examples:__       
  `allocate g+ r-`   
  `allocate`   



#### PRINT
Outputs team or room data to the console. Filter options are available. Has the format:   
`print  <target>(team|room)  [<filters>(see the filter tables below)]` 
            
* __target:__   
Target data to output. Value can be either `team` or `rooms`.
            
* __filters:__   
Optional. Filters the output using combinations of constraints:   
                        
  __Room filters__  |  __meaning__
  :-----------------|:-------------
  `os` or `ls`      |  _office spaces_ or _living spaces_ 
  `st` or `fw`      |  _for staffor_ _for _fellows_
  `ml` or `fm`      |  _for males_ or _for females_
  `oc+` or `oc-`    |  _has occupants_ or _no occupants_
  `cf+` or `cf-`    |  _is full capacity_ or _not full capacity_

  __Person filters__  |  __meaning__
  :-----------------|:-------------
  `st` or `fw`      |   _staff_ or _fellows_
  `ml` or `fm`      |   _male_ or _female_
  `o+` or `o-`      |   _have office space_ or _don't have office space_
  `l+` or `l-`      |   _have living space_ or _don't have living space_
  `w+` or `w-`      |   _want living space_ or _don't want living space_

  __NOTE:__ for rooms filters, any of the five pairs can be combined in the same command. The same hold true for person filteres.  
    
  __Examples:__     
  `print rooms os fw c+`      # prints office-spaces for fellows that are filled to capacity.   
  `print team fw fm w+ l-`    # prints female fellows that want but have not been allocated living spaces.    



#### SAVE
Outputs team or room data to a file. Filter options are available. Use the format:  
`save <target>(team|room) [<filters>(any combination from the list below)] ['<filepath>'] [<mode>(:o|:a)]`
* __target:__   
Same as in 'print' command.   
* __filters:__   
Same as in 'print' command.   
* __filepath:__   
Optional path to the output file wrapped in single-quotes `''`. Can be absolute or relative.    
Defaults to './data/output.txt'.   
* __mode:__   
Optional. Specifies how the data is written to file.     
 `:o` to overwrite previous saved content.   
 `:a` to append to previously saved content.    
Defaults to `:o`.

  __Examples:__     
  `save rooms os fw c- '/data/output.txt' :a`    
  `save team fw ml l-`         
