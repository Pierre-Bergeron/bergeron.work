# Python Import Data from Text File to Array
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

receiving_temp_list = []
tempA_list = []
tempB_list = []
inventory_2list = []

def add_inventory():
    r_tl = 0
    l_tl = len(receiving_temp_list)
        
    null_amnt = float(0.00)
    null_cnt = 0
    null_desc = "No Name Available"
    
    while r_tl < l_tl:
        tempB_list = [receiving_temp_list[r_tl][0], null_desc, null_amnt, null_amnt, receiving_temp_list[r_tl][1], null_cnt, null_cnt]
        inventory_2list.append(tempB_list)
        r_tl += 1
        
    print(inventory_2list)
        
def save_inventory():
    outfile = open("inventory.txt", "w")
    
 
def get_receiving(file_id):
    file = open(file_id + ".txt", "r")
    
    mixed_line_article1 = "NoVal"
    while mixed_line_article1 != "":
        mixed_line_article1 = file.readline()
        if mixed_line_article1 != "":
            mixed_line_article2 = mixed_line_article1.strip()
            tempA_list = mixed_line_article2.split(",")
            receiving_temp_list.append(tempA_list)
        else:
            print()
    
    r = 0
    c = 1 # Column 1 (qty amnt)
    l = len(receiving_temp_list)
    while r < l:
        none_int = receiving_temp_list[r][c]
        value_int = int(none_int)
        receiving_temp_list[r][c]
        
        r += 1
        
def view_po_BfAcc():
    f_msg_str = ""
    r = 0
    l = len(receiving_temp_list)
    while r < l:
        msg_str = str(receiving_temp_list[r][0] + " " + str(receiving_temp_list[r][1]) + "pc \n" )
        f_msg_str = f_msg_str + msg_str
        r += 1
        
    print(f'''
The order contains the following items;
----UPC---|-QTY-
{f_msg_str}''')
              
def main():
    menu_selection = "A"
    while not (menu_selection.upper == "X"):
        print("""
Welcome to menu
1 - Receive inventory by PO.
2 - View Current order content
3 - add to inventory file
E - Leave program              
              """)

        menu_selection = input("Option selected: ")
        if menu_selection == "1":
            file_name = input("What is the PO# for the order: ")
            get_receiving(file_name)
            
        elif menu_selection == "2":
            view_po_BfAcc()
            
        elif menu_selection == "3":
            add_inventory()
            
        elif menu_selection == "X":
            print("Good Bye")
            
        else:
            print("Option not supported.\n")

main()