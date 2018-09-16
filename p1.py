##########################################################################################################
#   Program Name: Digging in the Dirt
#   Date:         15 Sep 2018
#   Description:  The program can find and display the paths of all of the files
#                 in a directory and take action on some particular files
##########################################################################################################
from os import listdir, scandir, stat, utime
from os.path import isfile, join
import sys
import time
import shutil
from datetime import datetime

command_valid_list = ['D', 'R', 'A', 'N', 'E', 'T', '<', '>', 'F', 'G']

def menu():
    ''' user interface '''
    flag=0
    while True:
        print('##############################################################################################')
        print('Welcome to the program: Digging in the Dirt\n')
        print('Command List:\n')
        print('   D: list all of the files in current directory ONLY\n')
        print('   R: list all of the files in current and sub directories\n')
        print('   G: quit\n')
        print('##############################################################################################')
        user_input = input('Please enter your command: ')
        input_path=''
        search_result=[]
        if len(user_input.split()) == 1:
            if user_input not in command_valid_list:
                print('ERROR')
            elif user_input == 'D' or user_input == 'R':
                print('ERROR')
            elif user_input == 'G':
                sys.exit(0)
        else:
            command, path = user_input.split(' ')
            input_path=path
            if command == 'D':
                search_result=cmd_D(path)
                for i in cmd_D(path):
                    print(i)
                flag=1
                break
            elif command == 'R':
                search_result=cmd_R(path)
                for i in cmd_R(path):
                    print(i)
                break
    
    while True:
        print('##############################################################################################')
        print('Search Command List:\n')
        print('   A: search for all files that are prevously listed\n')
        print('   N: search for files whose names exactly match a particular name\n')
        print('   E: search for files whose names have a particular extension\n')
        print('   T: search for text files that contain the given text\n')
        print('   <: search for files whose size, measured in bytes, is less than a specified threshold\n')
        print('   >: search for files whose size, measured in bytes, is greater than a specified threshold\n')
        print('   G: quit\n')
        print('##############################################################################################')
        search_input = input('Please enter your search command: ')
        narrow_search_result=[]
        error_flag=0
        if len(search_input.split()) == 1:
            if search_input not in command_valid_list:
                print('ERROR')
            elif search_input == 'N' or search_input == 'E' or search_input == 'T' or \
                 search_input == '>' or search_input == '<':
                print('ERROR')
            elif search_input == 'A':
                narrow_search_result=cmd_A( search_result)
                for i in narrow_search_result:
                    print(i)
                break
            elif search_input == 'G':
                sys.exit(0)
        else:
            command, pattern = search_input.split(' ', 1)
            if command == 'N':
                narrow_search_result=cmd_N(pattern, search_result)
                for i in narrow_search_result:
                    print(i)
                break
            elif command == 'E':
                narrow_search_result=cmd_E(pattern.lstrip('.'), search_result)
                for i in narrow_search_result:
                    print(i)
                break
            elif command == 'T':
                narrow_search_result=cmd_T(pattern,  search_result, error_flag)
                for i in narrow_search_result:
                    print(i)
                if error_flag == 0:
                    break
            elif command == '<':
                narrow_search_result=cmd_SizeLess(pattern,  search_result)
                for i in cmd_SizeLess(pattern,  search_result):
                    print(i)
                break
            elif command == '>':
                narrow_search_result=cmd_SizeGreater(pattern,  search_result)
                for i in cmd_SizeGreater(pattern,  search_result):
                    print(i)
                break
            else:
                print('ERROR')
    while True:
        print('##############################################################################################')
        print('Narrow Search Command List:\n')
        print('   F: print the first line of text from file if it is a text file; print NOT TEXT if not\n')
        print('   D: make a duplicate copy of the file and store it in the same directory where the original\n \
                     resides, but the copy should have .dup appended to its filename\n')
        print('   T: modify its last modified timestamp to be the current date/time\n')
        print('   G: quit\n')
        print('##############################################################################################')
        narrow_search_input = input('Please enter your narrow search command: ')
        if len(narrow_search_input.split()) == 1:
            if narrow_search_input not in command_valid_list:
                print('ERROR')
            elif narrow_search_input == 'F':
                cmd_F(narrow_search_result)
                break
            elif narrow_search_input == 'D':
                cmd_Dup(narrow_search_result, input_path, flag)
                break
            elif narrow_search_input == 'T':
                cmd_Touch(narrow_search_result)
                break
            elif narrow_search_input == 'G':
                sys.exit(0)
        else:
            print('ERROR')

def cmd_Touch(narrow_search_result):
    ''' modify its last modified timestamp to be the current date/time '''
    for i in narrow_search_result:
        utime(i)
        print(i+' '+str(datetime.fromtimestamp(stat(i).st_mtime)))

def cmd_Dup(narrow_search_result, input_path, flag):
    ''' make a duplicate copy of the file and store it in the same directory where the original
        resides, but the copy should have .dup appended to its filename '''
    for i in narrow_search_result:
        shutil.copy2(i, i+'.dup')
    if flag==1:
        for i in cmd_D(input_path):
            print(i)
    
            
def cmd_F(narrow_search_result):
    ''' print the first line of text from file if it is a text file; print NOT TEXT if not '''
    for i in narrow_search_result:
        if ".txt" not in i:
            print('NOT TEXT')
        else:
            line=open(i, 'r').readlines()
            print(line[0])
    

def cmd_SizeGreater(pattern, search_result):
    ''' search for files whose size, measured in bytes, is greater than a specified threshold '''
    r=[]
    for i in search_result:
        statinfo=stat(i)
        if int(pattern) > statinfo.st_size:
            r.append(i)
    return r

def cmd_SizeLess(pattern, search_result):
    ''' search for files whose size, measured in bytes, is less than a specified threshold '''
    r=[]
    for i in search_result:
        statinfo=stat(i)
        if int(pattern) < statinfo.st_size:
            r.append(i)
    return r
            
def cmd_T(pattern, search_result, error_flag):
    ''' search for text files that contain the given text '''
    r=[]
    for i in search_result:
        if ".txt" in i:
            file = open(i, "r")
            for line in file:
                if pattern in line:
                    r.append(i)
        else:
            error_flag=1
    return r

def cmd_E(pattern, search_result):
    ''' search for files whose names have a particular extension '''
    r=[]
    pattern='.'+pattern
    for i in search_result:
        if i.endswith(pattern)==True:
            r.append(i)
    return r

def cmd_N(pattern, search_result):
    '''search for files whose names exactly match a particular name '''
    r=[]
    for path_str in search_result:
        filename=path_str.split('/')[-1]
        if pattern == filename:
            r.append(path_str)
    return r

def cmd_A(search_result):
    '''search for files based on the previous result '''
    return search_result

def cmd_R(path):
    '''all of the files in that directory will be under consideration, along with all of the
       files in its subdirectories, all of the files in their subdirectories, and so on '''
    r1=r2=[]
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    for files in file_list:
        filepath=path+'/'+files
        if filepath not in r1 and filepath not in r2:
            r1.append(filepath)
    for entry in scandir(path):
        if entry.is_dir():
            subdir_filepath=path+'/'+entry.name
            r2=cmd_R(subdir_filepath)
    return r1+r2

def cmd_D(path):
    '''all of the files in that directory will be under consideration '''
    r=[]
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    for files in file_list:
        r.append(path+'/'+files)
    return r
    
if __name__ == '__main__':
    menu()
