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
   *  make a duplicate copy of the file and store it in the same directory where the original resides, but the copy should have .dup     (short for "duplicate") appended to its filename, and print them out
- [x] T 
   *  modify its last modified timestamp to be the current date/time, and print them out

