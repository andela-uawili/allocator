# =============================================================================
# 	OFFICE SPACE ALLOCATION SYSTEM (for Andela's Amity)
# =============================================================================
#	Description:	Python program to allocate people to rooms in Amity.
# 	Author:			Awili Uzochikwa Young (uzo.awili@andela.com).
#	Python Verson:	2.7.10
# ==============================================================================


import sys
import time
from cmd import Cmd

from app import settings


class Allocator(Cmd):
	""" -------- """
	
	def __init__(self):
		Cmd.__init__(self)
		self.setup()

	def setup(self):
		""" runs the progam initialization tasks """
		pass


# launch Allocator:
if __name__ == "__main__":
	Allocator().cmdloop()