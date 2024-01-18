# Python Import Data from Text File and Edit Data Back to Text File.
# Copyright (C) 2023  Pierre Bergeron
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

def wright_file_prg2(s_name, s_grade, file_name):
    student_entry = s_name + "  %" + str(s_grade)
    file = open(file_name+".txt", "a")
    file.write(student_entry + "\n")
    file.close()
    
def write_file_prg1(f_name, l_name, file_name):
    name_entry = f_name + " " + l_name
    file = open(file_name+".txt", "a")
    file.write(name_entry + "\n")
    file.close()

def read_file(file_name):
    if os.path.exists(file_name+".txt"):
        file = open(file_name+".txt", "r") 
        file_data = file.read()
        file.close()
        return file_data
    
    else:
        print("""
File could not be found.
              """)
        return "UNKNOWN"

def display_data(file_data, file_name):
    print(f'''
The data available from the file {file_name}.txt;

{file_data}
------\n
          ''')
def option_prg2():
    print('''
Enter students name and grades, to exit this option enter a blank name.\n
          ''')
    file_name = input("Enter a file name for the records (ex. 'FileName): ")
    s_name = "StudentName"
    while not s_name == "":
        s_name = input("\nEnter the studnet's name: ")
        if s_name != "":
            s_grade = str(0)
            collecting_valid_num = True
            while collecting_valid_num == True:
                s_grade = input("Enter the student's grade (0-100): %")
                if s_grade.isnumeric() == True: #REF_PULL
                    s_grade = int(s_grade)
                    if s_grade >= 0 and s_grade<= 100:
                      wright_file_prg2(s_name, s_grade, file_name)
                      collecting_valid_num = False
                      
                    else:
                        print("Student grade must be between 0-100.")
                else: 
                    print("Student's grade must be a number!")
       
        else:
            print("\nWelcome Back to menu!")

def option_prg1():
    f_name = "FirstName"
    l_name = "LastName"
    file_name = input("Enter a file name for the name list (ex. filename): ")
    print(f'''
Enter names, to stop this program enter a blank name.
          ''')
    while not f_name == "":
        f_name = input("Enter the first name: ")
        if f_name != "":
            l_name = input("Enter the last name: ")
            write_file_prg1(f_name, l_name, file_name)
            
            
        else:
            print("\nWelcome Back to menu!")
            
def option_prg3():
    file_name = "Defult"
    print('''
Enter a file name to read, leave blank to go back to menu.
          ''')
    while not file_name == "":
        file_name = input("\nEnter the name of the file to read (ex. 'FileName): ")
        if file_name != "":
            file_data = read_file(file_name)
            if file_data != "UNKNOWN":
                display_data(file_data, file_name)
            else:
                print()
        else:
            print("\nWelcome Back to menu!")





def main():

    menu = ""
    while not (menu == 'X' or menu =='x'):

        print('''\n
        
Program by Pierre Bergeron.
        
              
Welcome to document controller
Select any of the following option;
1 - Program 1 - Create List of Names
2 - Program 2 - Create a record of students name & gardes
3 - Program 3 - Read File Data
              
X - Quit the program without viewing.\n          
                ''')
        menu = input("Option selected: ")
    
        if menu == "1":
            option_prg1()
        
        elif menu == "2":
            option_prg2()
        
        elif menu == "3":
            option_prg3()
            
        elif menu == "X" or menu =='x':
            print("Good bye.\n")
        
        else:
            print("The option selected does not exist, Try again!")
            


if __name__ == '__main__':
    main()