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
from app.persons import Person, Staff, Fellow
from app.spaces import Room, OfficeSpace, LivingSpace


class Allocator(Cmd):
    """ -------- """

    intro = settings.SPLASH
    prompt = settings.PROMPT
    doc_header = 'Allocator Help'
    misc_header = 'Allocator:'
    undoc_header = 'Other:'
    ruler = '-'
    
    def do_load(self, line):
        """ 
        Loads data from text files to populate either the 'teamdir' or 'roomdir'.
        e.g. load teamdir '/data/input_persons.txt' a
        See README for more details.
        
        """
        pass  
    
    def do_exit(self, line):
        return True

    def do_x(self, line):
        return True


# launch Allocator:
if __name__ == "__main__":
    Allocator().cmdloop()