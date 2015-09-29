# allocator
Room allocation system for Andela's Amity.



COMMAND 	OPTIONS:


load 		filepath (default="data/input.txt")  	mode (o | a)
			
input  		cslist (e.g "ANDREW CAR FELLOW Y M, TONY LAGBAJA STAFF")		mode(o | a)

allocate	seperate-gender-living-spaces (g+ | g-)  	seperate-role-office-spaces (r- | r-) 	randomize (z+ | z-)

print		query (roomdir | teamdir) 	filters ( os  ls  oss  osf  lsm  lsf  c+  c-   s   f  fm  ff  o+  o-  l+  l- ) 

save		query (-- same as in print comand --)  	filters (-- same as in print comand --)		mode (o | a)