# Digging in the Dirt #
The program can find and display the paths of all of the files in a directory and take action on some particular files

## Program Functional Specification ##
### Part 1 ###
The program reads a line of input that specifies which files are eligible to be found
- [x] D [path to a directory]
   *  print all the files in that directory
- [x] R [path to a directory]
   *  print all the files in that directory, along with all of the files in its subdirectories, recursively
### Part 2: ###
The program now reads a line of input that describes the search characteristics that will be used to decide whether files are "interesting"
- [x] A 
   *  print all of the files found in the previous step are considered interesting
- [x] N [filename]
   *  print the search whose it exactly matches a particular filename among all of the "interesting" files
- [x] E [file extension]
   *  print the search whose it exactly matches a particular file extension among all of the "interesting" files
- [x] T [text string]
   *  print the search whose belongs to text files and contains the given text string among all of the "interesting" files
- [x] < [threshold]
   *  print the search whose file size, measured in bytes, is less than a specified threshold among all of the "interesting" files
- [x] > [threshold]
   *  print the search whose file size, measured in bytes, is greater than a specified threshold among all of the "interesting" files
### Part 3: ###
The program will take action on the "interesting" files
- [x] F 
   *  print the first line of text from the "interesting" file if it's a text file; print NOT TEXT if it is not.
- [x] D 
   *  make a duplicate copy of the file and store it in the same directory where the original resides, but the copy should have .dup     (short for "duplicate") appended to its filename, and print all the files, including the duplicate one(s)
- [x] T 
   *  modify its last modified timestamp to be the current date/time, and print them out

## Result ##
### Case 1: ###
```
##############################################################################################
Welcome to the program: Digging in the Dirt

Command List:

   D: list all of the files in current directory ONLY

   R: list all of the files in current and sub directories

   G: quit

##############################################################################################
Please enter your command: R /Users/sophialee/Documents
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
/Users/sophialee/Documents/CS133/employee.txt.dup
/Users/sophialee/Documents/CS133/.DS_Store
/Users/sophialee/Documents/CS133/CS133-L4.pdf
/Users/sophialee/Documents/CS133/employee.txt
/Users/sophialee/Documents/CS133/CS133-L3.pdf
/Users/sophialee/Documents/CS133/employee/employee.txt
##############################################################################################
Search Command List:

   A: search for all files that are prevously listed

   N: search for files whose names exactly match a particular name

   E: search for files whose names have a particular extension

   T: search for text files that contain the given text

   <: search for files whose size, measured in bytes, is less than a specified threshold

   >: search for files whose size, measured in bytes, is greater than a specified threshold

   G: quit

##############################################################################################
Please enter your search command: A
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
/Users/sophialee/Documents/CS133/employee.txt.dup
/Users/sophialee/Documents/CS133/.DS_Store
/Users/sophialee/Documents/CS133/CS133-L4.pdf
/Users/sophialee/Documents/CS133/employee.txt
/Users/sophialee/Documents/CS133/CS133-L3.pdf
/Users/sophialee/Documents/CS133/employee/employee.txt
##############################################################################################
Narrow Search Command List:

   F: print the first line of text from file if it is a text file; print NOT TEXT if not

   D: make a duplicate copy of the file and store it in the same directory where the original
                      resides, but the copy should have .dup appended to its filename

   T: modify its last modified timestamp to be the current date/time

   G: quit

##############################################################################################
Please enter your narrow search command: F
NOT TEXT
NOT TEXT
NOT TEXT
NOT TEXT
NOT TEXT
NOT TEXT
100,Thomas,Sales,5000

100,Thomas,Sales,5000

NOT TEXT
NOT TEXT
100,Thomas,Sales,5000

NOT TEXT
100,Thomas,Sales,5000
```
### Case 2: ###
```
##############################################################################################
Welcome to the program: Digging in the Dirt

Command List:

   D: list all of the files in current directory ONLY

   R: list all of the files in current and sub directories

   G: quit

##############################################################################################
Please enter your command: D /Users/sophialee/Documents
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
##############################################################################################
Search Command List:

   A: search for all files that are prevously listed

   N: search for files whose names exactly match a particular name

   E: search for files whose names have a particular extension

   T: search for text files that contain the given text

   <: search for files whose size, measured in bytes, is less than a specified threshold

   >: search for files whose size, measured in bytes, is greater than a specified threshold

   G: quit

##############################################################################################
Please enter your search command: N employee.txt
/Users/sophialee/Documents/employee.txt
##############################################################################################
Narrow Search Command List:

   F: print the first line of text from file if it is a text file; print NOT TEXT if not

   D: make a duplicate copy of the file and store it in the same directory where the original
                      resides, but the copy should have .dup appended to its filename

   T: modify its last modified timestamp to be the current date/time

   G: quit

##############################################################################################
Please enter your narrow search command: D
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
```
### Case 3: ###
```
##############################################################################################
Welcome to the program: Digging in the Dirt

Command List:

   D: list all of the files in current directory ONLY

   R: list all of the files in current and sub directories

   G: quit

##############################################################################################
Please enter your command: D
ERROR
##############################################################################################
Welcome to the program: Digging in the Dirt

Command List:

   D: list all of the files in current directory ONLY

   R: list all of the files in current and sub directories

   G: quit

##############################################################################################
Please enter your command: D /Users/sophialee/Documents
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/exercise - China Citic.docx
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
##############################################################################################
Search Command List:

   A: search for all files that are prevously listed

   N: search for files whose names exactly match a particular name

   E: search for files whose names have a particular extension

   T: search for text files that contain the given text

   <: search for files whose size, measured in bytes, is less than a specified threshold

   >: search for files whose size, measured in bytes, is greater than a specified threshold

   G: quit

##############################################################################################
Please enter your search command: E oc
/Users/sophialee/Documents/iliveinthe.oc
##############################################################################################
Narrow Search Command List:

   F: print the first line of text from file if it is a text file; print NOT TEXT if not

   D: make a duplicate copy of the file and store it in the same directory where the original
                      resides, but the copy should have .dup appended to its filename

   T: modify its last modified timestamp to be the current date/time

   G: quit

##############################################################################################
Please enter your narrow search command: T
/Users/sophialee/Documents/iliveinthe.oc 2018-09-16 17:40:31.922970
```
### Case 4: ###
```
##############################################################################################
Welcome to the program: Digging in the Dirt

Command List:

   D: list all of the files in current directory ONLY

   R: list all of the files in current and sub directories

   G: quit

##############################################################################################
Please enter your command: R /Users/sophialee/Documents
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/.DS_Store
/Users/sophialee/Documents/employee.ctl
/Users/sophialee/Documents/.localized
/Users/sophialee/Documents/invoice.doc
/Users/sophialee/Documents/interview.docx
/Users/sophialee/Documents/iliveinthe.oc
/Users/sophialee/Documents/employee.txt
/Users/sophialee/Documents/CS133/employee.txt.dup
/Users/sophialee/Documents/CS133/.DS_Store
/Users/sophialee/Documents/CS133/CS133-L4.pdf
/Users/sophialee/Documents/CS133/employee.txt
/Users/sophialee/Documents/CS133/CS133-L3.pdf
/Users/sophialee/Documents/CS133/employee/employee.txt
##############################################################################################
Search Command List:

   A: search for all files that are prevously listed

   N: search for files whose names exactly match a particular name

   E: search for files whose names have a particular extension

   T: search for text files that contain the given text

   <: search for files whose size, measured in bytes, is less than a specified threshold

   >: search for files whose size, measured in bytes, is greater than a specified threshold

   G: quit

##############################################################################################
Please enter your search command: T Randy,
/Users/sophialee/Documents/employee.txt.dup
/Users/sophialee/Documents/employee.txt
/Users/sophialee/Documents/CS133/employee.txt.dup
/Users/sophialee/Documents/CS133/employee.txt
/Users/sophialee/Documents/CS133/employee/employee.txt
##############################################################################################
Narrow Search Command List:

   F: print the first line of text from file if it is a text file; print NOT TEXT if not

   D: make a duplicate copy of the file and store it in the same directory where the original
                      resides, but the copy should have .dup appended to its filename

   T: modify its last modified timestamp to be the current date/time

   G: quit

##############################################################################################
Please enter your narrow search command: F xx
ERROR
##############################################################################################
Narrow Search Command List:

   F: print the first line of text from file if it is a text file; print NOT TEXT if not

   D: make a duplicate copy of the file and store it in the same directory where the original
                      resides, but the copy should have .dup appended to its filename

   T: modify its last modified timestamp to be the current date/time

   G: quit

##############################################################################################
Please enter your narrow search command: F
100,Thomas,Sales,5000

100,Thomas,Sales,5000

100,Thomas,Sales,5000

100,Thomas,Sales,5000

100,Thomas,Sales,5000

```
