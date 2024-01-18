# Python Keep Track of Treat Distributions.
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

def alert(treat_left_cnt):
    print(f"""
**********************************************      
You are running low on treats!
You only have {treat_left_cnt} treats to give!  
**********************************************\n
          """)
    add_treats = int(input("How many treats would you like to add?"))
    new_cnt = treat_left_cnt + add_treats
    return new_cnt

def show_count(treat_cnt, treat_left_cnt):
    print(f''' 
---------------------------------------------------
You have given out {treat_cnt} treats to this time.

And you have {treat_left_cnt} treats left.

The count hasn't stop yet, keep going! 
---------------------------------------------------\n
          ''')
    

def setup():
    start_cnt = int(input("How many treats do you have? "))
    main(start_cnt)
    
    
def main(treat_left_cnt):
    treat_left_cnt
    treat_cnt = 0
    treat_menu = ""
    while not (treat_menu == 'Q' or treat_menu =='q'):
        while treat_left_cnt < 5:
            treat_left_cnt = alert(treat_left_cnt)
            
        print('''
Welcome to the official treat counter!
Select any of the following option;
Y - A treat was given out.
N - No treats was given out.

V - View the amout of treats given.
Q - Quit the program without viewing.\n          
              ''')
        treat_menu = input("Option selected: ")
    
        if treat_menu == "Y" or treat_menu == 'y':
            treat_cnt += 1
            treat_left_cnt -= 1
            print("Treat count added to records.\n")
        
        elif treat_menu == "N" or treat_menu == 'n':
            print("Treat count has NOT changed.\n")
        
        elif treat_menu == "V" or treat_menu == 'v':
            show_count(treat_cnt, treat_left_cnt)
            
        elif treat_menu == "Q" or treat_menu =='q':
            print("Good bye.\n")
        
        else:
            print("The option selected does not exist, Try again!")
        
        
setup()