# allocator
Room allocation system for Andela's Amity.


This application runs as a command interpreter. See below for the list of commands and their usage.

Typically you will want to start by loading or inputing data for teams and rooms. (NOTE: There are defaults for this, you only need call the commands once).
Next you run the 'allocate' command to allocate person to rooms.
Finally you can query for room or team allocation data and print it to console or to a file.



COMMAND     OPTIONS:


load        Loads data from text files to populate either the 'team' or 'rooms'.

            Use the format: load  <target>(team|rooms)  ['<filepath>']   [<mode>(:o|:a)] 

            target:     Target data to populate. Either 'team' or 'rooms'.

            filepath:   Optional path to the input file wrapped in single-quotes ''.
                        Can be absolute or relative. 
                        Defaults to '/data/input_persons.txt' for team 
                        and '/data/input_rooms.txt' for rooms.

            mode:       Optionally specifies how the data is added to target. 
                        ':o' to overwrite previously loaded data.
                        ':a' to append to previously loaded data.
                        Defaults to ':o'.
            
            e.g.        load team '/data/input_persons.txt' :a
                        load rooms


input       Collects data from command line to populate either the 'team' or 'rooms'.

            Use the format: input  <target>(team|rooms)  '<cslist>'   [<mode>(:o|:a)] 
            
            target:     Target data to populate. Either 'team' or 'rooms'.

            cslist:     Comma seperated list of input lines for persons or rooms.
                        Wrapped in single-quotes ''.

            mode:       Optionally specifies how the data is added to target. 
                        ':o' to overwrite previously loaded data.
                        ':a' to append to previously loaded data.
                        Defaults to ':a'.
            
            e.g.        input team 'ANDREW PHILLIPS FELLOW Y M, MATTHEW O'CONNOR STAFF' :o
                        input room 'HAMMER  OFFICE  STAFF, SAPELE LIVING F'


allocate    Allocates persons to rooms using optional or default conditions.

            Use the format: allocate  [<sep_gender>(g+|g-)]  [<sep_roles>(r+|r-)]
            
            sep_gender: Optionally Specify whether genders should be separated when allocating 
                        fellows to living spaces.
                        'g+' to seperate genders.
                        'g-' to allow different genders to share living spaces. lol...in your dreams ;)
                        Defaults to 'g+'.

            sep_roles: Optionally Specify whether roles (staff and fellows) should be separated 
                        when allocating persons to office spaces.
                        'r+' to seperate roles.
                        'r-' to allow staff and fellows to share office spaces. Not bad huh?
                        Defaults to 'r+'.
            
            e.g.        allocate g+ r-
                        allocate


print       Outputs team or room data to the console. Filter options are available.

            Use the format: print  <target>(team|room)  [<filters>(any combination from the list below)] 
            
            target:     Target data to output. Either 'team' or 'rooms'.
            
            filters:    Optionally filters the output using combinations of these conditions:

                        os      office spaces
                        oss     office spaces for staff
                        osf     office spaces for fellows
                        ls      living spaces
                        lsm     living spaces for males
                        lsf     living spaces for females
                        c+      rooms with full capacity
                        c-      rooms below full capacity
                        s       staff
                        f       fellows
                        fm      fellows that are male
                        ff      fellows that are female
                        o+      persons with office space
                        o-      persons without office space
                        l+      persons with living space
                        l-      persons without living space
            
            e.g.        print rooms osf c-    # prints office-spaces for fellows that are not yet filled to capacity.
                        print team ff l-      # prints female fellows that have not been alloctaed living spaces.


save        Outputs team or room data to a file. Filter options are available.

            Use the format: save  <target>(team|room) [<filters>(any combination from the list below)] ['<filepath>'] [<mode>(:o|:a)]
            
            target:     same as in 'print' command.
            
            filters:    same as in 'print' command.

            filepath:   Optional path to the output file wrapped in single-quotes ''.
                        Can be absolute or relative. 
                        Defaults to '/data/output.txt'.

            mode:       Optionally specifies how the data is written to file. 
                        ':o' to overwrite previous saved content.
                        ':a' to append to previously saved content.
                        Defaults to ':o'.
            
            e.g.        save rooms osf c- '/data/input_persons.txt' :a
                        save team ff l-target:     same as in 'print' command.
            
            filter:     same as in 'print' command.

            filepath:   Optional path to the output file wrapped in single-quotes ''.
                        Can be absolute or relative. 
                        Defaults to '/data/output.txt'.

            mode:       Optionally specifies how the data is written to file. 
                        ':o' to overwrite previous saved content.
                        ':a' to append to previously saved content.
                        Defaults to ':o'.
            
            e.g.        save rooms osf c- '/data/input_persons.txt' :a
                        save team ff l-