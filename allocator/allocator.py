# =============================================================================
#   OFFICE SPACE ALLOCATION SYSTEM (for Andela's Amity)
# =============================================================================
#   Description:    Python program to allocate people to rooms in Amity.
#   Author:         Awili Uzochikwa Young (uzo.awili@andela.com).
#   Python Verson:  2.7.10
# ==============================================================================


from cmd import Cmd
from app import settings
from app import io
from app.managers import FacilityManager


class Allocator(Cmd):
    """ 
    Serves as the 'main' or entry point for the program. 
    It inherits from the Cmd class which  imlements functionality 
    that enables the program to run as an interactive command-line 
    interpreter. 

    """

    intro = settings.SPLASH
    prompt = settings.PROMPT
    doc_header = settings.DOC_HEADER
    misc_header = settings.MISC_HEADER
    undoc_header = settings.UNDOC_HEADER
    ruler = settings.DOCS_RULER

    def preloop(self):
        """ Runs all program initialization tasks"""

        self.manager =  FacilityManager()

    
    def do_load(self, line):
        """ 
        Loads data from text files to populate either the 'team' or 'rooms' lists.
        e.g. load team './data/input_persons.txt' a

        """
        cmd_args = io.parse_cmd_args(line, io.load_cmd_pattern)
        if cmd_args:
            success = self.manager.load(**cmd_args)
            if success:
                self.console_print("Yippee! load successful!", settings.INFO_FORMAT)
            else:
                self.console_print("Sorry, the data could not be loaded from file.", settings.ERROR_FORMAT)
        else:
            self.console_print(settings.COMMMAND_ARGS_ERROR_MSG, settings.ERROR_FORMAT)
    

    def do_input(self, line):
        """ 
        Collects data from command line to populate either the 'team' or 'rooms'.
        e.g. input team 'ANDREW PHILLIPS FELLOW Y M, MATTHEW O'CONNOR STAFF' :o

        """
        cmd_args = io.parse_cmd_args(line, io.input_cmd_pattern)
        if cmd_args:
            success = self.manager.input(
                cmd_args.get('target'), 
                cmd_args.get('cslist'), 
                mode=cmd_args.get('mode')
            )
            if success:
                self.console_print("Yippee! input successfull!", settings.INFO_FORMAT)
            else:
                self.console_print("Sorry, something kinda went wrong! You can try again.", settings.ERROR_FORMAT)
        else:
            self.console_print(settings.COMMMAND_ARGS_ERROR_MSG, settings.ERROR_FORMAT)


    def do_allocate(self, line):
        """ 
        Allocates persons to rooms using optional or default constraints.
        e.g.  allocate g+ r-

        """
        cmd_args = io.parse_cmd_args(line, io.allocate_cmd_pattern)
        if cmd_args:
            success = self.manager.allocate(**cmd_args)
            if success:
                self.console_print("Noice! Allocation complete!", settings.INFO_FORMAT)
            else:
                self.console_print("Awww...something went wrong while allocating.", settings.ERROR_FORMAT)
        else:
            self.console_print(settings.COMMMAND_ARGS_ERROR_MSG, settings.ERROR_FORMAT)
    

    def do_print(self, line):
        """ 
        Outputs team or room data to the console. Filter options are available.

        """
        cmd_args = io.parse_cmd_args(line, io.output_cmd_pattern)
        if cmd_args:
            success = self.manager.print_to_console(
                cmd_args.get('target'), 
                cmd_args.get('filters')
            )
            if success:
                self.console_print("There, you asked for it!", settings.INFO_FORMAT)
            else:
                self.console_print("Sorry, something kinda went wrong! You can try again.", settings.ERROR_FORMAT)
        else:
            self.console_print(settings.COMMMAND_ARGS_ERROR_MSG, settings.ERROR_FORMAT)


    def do_save(self, line):
        """ 
        Outputs team or room data to the console. Filter options are available.

        """
        cmd_args = io.parse_cmd_args(line, io.output_cmd_pattern)
        if cmd_args:
            success = self.manager.save_to_file(**cmd_args)
            if success:
                self.console_print("Yippee! saved successfully!", settings.INFO_FORMAT)
            else:
                self.console_print("Sorry, something kinda went wrong! You can try again tho.", settings.ERROR_FORMAT)
        else:
            self.console_print(settings.COMMMAND_ARGS_ERROR_MSG, settings.ERROR_FORMAT)


    def default(self, line):
        self.console_print(settings.COMMMAND_ERROR_MSG, settings.ERROR_FORMAT)
        return 


    def do_exit(self, line):
        """ 
        Exits the program. Simply enter 'exit' or the shorter 'x'.

        """
        return True


    def do_x(self, line):
        """ 
        Exits the program. Simply enter 'exit' or the shorter 'x'.

        """
        return True


    def help_load(self):

        print """

        load:       Loads data from text files to populate either the 'team' or 'rooms'.

                    Use the format: load  [<target>(team|rooms)  ['<filepath>'] ]  [<mode>(:o|:a)]

                    target:     The target data to populate. Either 'team' or 'rooms'.
                                Note that although <target> is optional, the other options have no effect unless it is specified.
                                calling load without target loads both rooms and teams with the default filepath and mode settings.

                    filepath:   Optional. Path to the input file wrapped in single-quotes ''.
                                Can be absolute or relative. 
                                Defaults to '/data/input_persons_ext.txt' for team 
                                and '/data/input_rooms_ext.txt' for rooms.

                    mode:       Optional. Specifies how the data is added to target. 
                                ':o' to overwrite previously loaded data.
                                ':a' to append to previously loaded data.
                                Defaults to ':o'.
                    
                    e.g.        load team './data/input_persons_ext.txt' :a
                                load rooms

        """

    def help_input(self):

        print """

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

        """

    def help_allocate(self):

        print """
        
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

        """

    def help_print(self):

        print """
        
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

        """

    def help_save(self):

        print """
        
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

        """

    def console_print(self, message, msg_format="{}"):
        print msg_format.format(message)


# launch Allocator:
if __name__ == "__main__":
    Allocator().cmdloop()