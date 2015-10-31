# Allocator
Python program to allocate people to rooms in Andela's Amity.


## Installation:

1. Clone the repo to any directory on your PC from which you can run python (preferrably with a virtual environment). 
2. Run ```pip install -r requirements.txt``` to install all dependencies.
3. Finally run ```python allocator.py``` and voila! Start allocating! 

The program is should guide you from there but if not, feel free to use the help command anytime. 


## Testing

* Run the following command in the root program's root package.   
```nosetests```  
* To test with coverage reports.   
``` nosetests --with-coverage --cover-package=allocator ```   


## Usage:
This application runs as a command interpreter.

1. Typically you will want to start by loading or inputing data for teams and rooms. (NOTE: There are defaults for this, you only need call the bare minimum commands without any arguments).
2. Next you run the 'allocate' command to allocate person to rooms.
3. Finally you can query for room or team allocation data and 'print' it to the console or 'save' to a file.


## Commands:
See below for the list of commands and their usage:

#### load        
Loads data from text files to populate either the 'team' or 'rooms'.   
Use the format: ```load  [<target>(team|rooms)  ['<filepath>'] ]  [<mode>(:o|:a)]```   

target|     The target data to populate. Either 'team' or 'rooms'.   
            Note that although <target> is optional, the other options have no effect unless it is specified.   
            calling load without target loads both rooms and teams with the default filepath and mode settings.   

filepath|   Optional. Path to the input file wrapped in single-quotes ''.   
            Can be absolute or relative.    
            Defaults to '/data/input_persons_ext.txt' for team    
            and '/data/input_rooms_ext.txt' for rooms.   

mode|       Optional. Specifies how the data is added to target. 
            ':o' to overwrite previously loaded data.
            ':a' to append to previously loaded data.
            Defaults to ':o'.

__Examples:__        
```load team './data/input_persons_ext.txt' :a```   
```load rooms```  


input:      Collects data from command line to populate either the 'team' or 'rooms'.

            Use the format: input  <target>(team|rooms)  '<cslist>'   [<mode>(:o|:a)] 
            
            target:     Target data to populate. Either 'team' or 'rooms'.

            cslist:     Comma seperated list of input lines for persons or rooms.
                        Wrapped in single-quotes ''.

            mode:       Optional. Specifies how the data is added to target. 
                        ':o' to overwrite previously loaded data.
                        ':a' to append to previously loaded data.
                        Defaults to ':a'.
            
            e.g.        input team 'ANDREW PHILLIPS FELLOW Y M, MATTHEW O'CONNOR STAFF' :o
                        input room 'HAMMER  OFFICE  STAFF, SAPELE LIVING F'


allocate:   Allocates persons to rooms using optional or default constraints.

            Use the format: allocate  [<sep_gender>(g+|g-)]  [<sep_roles>(r+|r-)]
            
            sep_gender: Optional. Specifies whether genders should be separated when allocating 
                        fellows to living spaces.
                        'g+' to seperate genders.
                        'g-' to allow different genders to share living spaces. lol...in your dreams ;)
                        Defaults to 'g+'.

            sep_roles: Optional. Specifies whether roles (staff and fellows) should be separated 
                        when allocating persons to office spaces.
                        'r+' to seperate roles.
                        'r-' to allow staff and fellows to share office spaces. Not bad huh?
                        Defaults to 'r+'.
            
            e.g.        allocate g+ r-
                        allocate


print:      Outputs team or room data to the console. Filter options are available.

            Use the format: print  <target>(team|room)  [<filters>(see the list below)] 
            
            target:     Target data to output. Either 'team' or 'rooms'.
            
            filters:    Optional. Filters the output using combinations of constraints:
                        
                        ROOM FILTERS (combine any of these. option seperated by '|' should not be combined ):

                        os|ls             office spaces | living spaces 
                        st|fw             for staff| for fellows
                        ml|fm             for males | for females
                        oc+|oc-           has occupants | no occupants
                        cf+|cf-           is full capacity | not full capacity

                        TEAM FILTERS (combine any of these):

                        st|fw             staff|fellows
                        ml|fm             male | female    
                        o+|o-             have office space | don't have space
                        l+|l-             have living space | don't have living space
                        w+|w-             want living space | don't want living space
                                        
            e.g.        print rooms os fw c+      # print office-spaces for fellows that are filled to capacity.
                        print team fw fm w+ l-    # print female fellows that want but have not been allocated living spaces.


save:       Outputs team or room data to a file. Filter options are available.

            Use the format: save  <target>(team|room) [<filters>(any combination from the list below)] ['<filepath>'] [<mode>(:o|:a)]
            
            target:     same as in 'print' command.
            
            filters:    same as in 'print' command.

            filepath:   Optional path to the output file wrapped in single-quotes ''.
                        Can be absolute or relative. 
                        Defaults to './data/output.txt'.

            mode:       Optionally specifies how the data is written to file. 
                        ':o' to overwrite previous saved content.
                        ':a' to append to previously saved content.
                        Defaults to ':o'.
            
            e.g.        save rooms os fw c- '/data/output.txt' :a
                        save team fw ml l-