'''
Parameters:

file_name: This parameter as the name suggests, is the name of the file that we want to open.

mode: This parameter is a string that is used to specify the mode in which the file is to be opened. The following strings can be used to activate a specific mode:

“r”: This string is used to read(only) the file. It is passed as default if no parameter is supplied and returns an error if no such file exists.
“w”: This string is used for writing on/over the file. If the file with the supplied name doesn’t exist, it creates one for you.
“a”: This string is used to add(append) content to an existing file. If no such file exists, it creates one for you.
“x”: This string is used to create a specific file.
“b”: This string is used when the user wants to handle the file in binary mode. This is generally used to handle image files.
“t”: This string is used to handle files in text mode. By default, the open() function uses the text mode.
'''

# by default open set a mode file in a read mode


# After you open a file, the next thing to learn is how to close it.

# Warning: You should always make sure that an open file is properly closed.
 

'''
The with statement automatically takes care of closing the file once it leaves the with block, even in cases of error. I highly recommend that you use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.
'''
import os


print(os.path.dirname(os.path.realpath(".")))

# read a text , return from txt a str class where we can apply strings methods
with open('test.txt','r') as redable:
   print(redable.read().upper())

# get the lines text into a list
with open('test.txt','r') as redable:
   list_lines= redable.readlines() 
   print(list_lines)
      
