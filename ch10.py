# CH=10....... Reg Ex

'''
A RegEx, or Regular Expression, is a sequence
of characters that forms a search pattern.
RegEx can be used to check if a
string contains the specified search pattern.
'''



'''
RegEx Module
Python has a built-in package called re, 
which can be used to work with Regular Expressions.

Import the re module:
'''



'''
RegEx Functions
The re module offers a set of functions
that allows us to search a string for a match:

Function	         Description
findall	            Returns a list containing all matches
search	            Returns a Match object if there is a match anywhere in the string
split	            Returns a list where the string has been split at each match
sub	                Replaces one or many matches with a string
'''



'''

Metacharacters are characters with a special meaning:

Character	         Description	        
[]	              A set of characters	        	
\	              Signals a special sequence (can also be used to escape special characters)	
.	              Any character (except newline character)	
^	              Starts with		
$	              Ends with	
*	              Zero or more occurrences	
+	              One or more occurrences	
{}	              Exactly the specified number of occurrences	
|	              Either or		
()	              Capture and group

'''

