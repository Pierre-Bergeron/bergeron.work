# Python Keep Track of Treat Distributions.
# Copyright (C) 2023  Pierre Bergeron, Matthew Lesenke, Rhea Rose, Henry Ybazeta-Best
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

# PO Management;
receiving_load = []
receiving_load_temp = []
rlt_B = []
receiving_load_Full_details = []
r_temp_A = []

fulfillment_temp = []
fulfillment_order = []

found_match = []
no_match = []
single_match = []
built_match = []
# Inventory Management;
inventory = []
i_temp_A = []

# Transaction processing list;
trans_temp_list = []
trans_cart = []

# Transaction log
trans_log = []
trans_log_temp = []
ID_NUM = 0

import os
import datetime
date_now = datetime.datetime.now()
y = str(date_now.year)
m = str(date_now.month)
d = str(date_now.day)
date_f_now = d + "-" + m +"-" + y # 00-00-0000



#PB
def isprice(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


#PB
def gen_trans_id():
    global ID_NUM 
    transNum = ID_NUM + 1
    transRef = "T-" + str(transNum)
    ID_NUM += 1
    return transRef

#PB    
def find_refId(upc, s_list): 
    s_list.sort(reverse=True)
    r = 0
    l = len(s_list) -1
    while r < l:
        if upc == s_list[r][0]:
            refId = r
            return str(refId)
        else:
            r += 1
    if r >= l:
        return "NoVal"
    
# menu for inventory , GROUP_EFFORT
def menuA():
    print("""
Authorized Access Only!      
     Better games  
          
Menu
1 - PO Management
2 - Inventory Management 
3 - Save inventory & Generate Daily Sale Report          
E - Exit""")
    
def menu_1():
    print("\n1 - Receive PO Order \n2 - Send PO Order")
    
def menu_2():
    print("\n1 - Complete a transaction \n2 - Change Retail Price")
    
# PO Management Functions; - PB
def get_PO_articles(po_name):
    receiving_load.clear()
    file = open(po_name + ".txt", "r")
    order_str = file.read()
    receiving_load_temp = order_str.split('\n')
    p = 0
    l_rlt = len(receiving_load_temp)
    while p < l_rlt:
        rlt_B = receiving_load_temp[p].split(",")
        receiving_load.append(rlt_B)
        p += 1
    
    del receiving_load[l_rlt - 1]
    rlt_B.clear()
    file.close()
    show_PO_articles()
    inventory.sort(reverse=True)
    
# HENRY   
def show_PO_articles():
    f_msg_str = ""
    r = 0
    l = len(receiving_load)
    while r < l:
        msg_str = str(receiving_load[r][0]) + " " + str(receiving_load[r][1]) + "pc \n"
        f_msg_str = f_msg_str + msg_str # Create a big formatted string for printing
        r += 1
        
    print(f'''
The order contains the following items;
----UPC---|-QTY-
{f_msg_str}''')
    
    keep_going = input("Would you like to add these items to inventory (Y/N): ")
    if keep_going.upper() == "Y":
        split_to_temps() 
    else:
        receiving_load.clear()
        
#PB    
def split_to_temps(): # Activate with Y/N
    global no_match
    global found_match
    global inventory
    r = 0
    l = len(receiving_load)
    no_match.clear()
    while r < l:
        check = find_refId(receiving_load[r][0], inventory)
        if check == "NoVal":
            no_match.append(receiving_load[r])
            r += 1
        else:
            found_match.append(receiving_load[r])
            r += 1
    update_found()
    inventory.sort(reverse=True)
            
#HENRY
def update_found():
    global found_match
    global inventory
    r = 0
    l = len(found_match)
    while r < l:
        p = int(find_refId(found_match[r][0], inventory))
        current_qty = int(inventory[p][4])
        add_qty = int(found_match[r][1])
        new_qty = current_qty + add_qty
        inventory[p][4] = str(new_qty)
        r += 1
        
    found_match.clear()
    no_found()
#PB    
def no_found():
    global no_match
    global inventory
    r = 0
    l = len(no_match)
    if r < l:
        print("Some items where not found in our system, Please fill in the details;")
    while r < l:
        if r <= l:
            print(f"for article {no_match[r][0]} enter the following information")
            desc = input("Article's Name: ")
            c_price_valid = True
            while c_price_valid == True:  
                c_price = input("Article's Purchased Price: $")
                if isprice(c_price) == False:
                    print("The COGS must be a number (ex: 10.99)")
                else:
                    c_price = float(c_price)
                    c_price_valid = False
            r_price_valid = True
            while r_price_valid == True:
                r_price = input("Article's Retail Price: $")
                if isprice(r_price) == False:
                    print("The retail price must be a number.")
                else:
                    r_price = float(c_price)
                    r_price_valid = False
            
            
            qty = no_match[r][1]
            built_match = (str(no_match[r][0])+","+str(desc)+","+str(c_price)+","+str(r_price)+","+str(qty)+","+"0,0").split(",")
        
            inventory.append(built_match)
            r += 1
            
    inventory.sort(reverse=True)
    

def po_send():
    global fulfillment_temp
    global fulfillment_order
    order_name = input("PO order name: ")
    upc = "val"
    while upc != "":
        print("\nEnter blank to complete PO order")
        if upc != "":
            upc = input("What is the upc of the products to send: ")
            position_row = find_refId(upc, inventory)
            if position_row.isdigit() == True:
                position_row = int(position_row)
                order_qty = int(input("QTY to send(ex. 1): "))
                current_qty = inventory[position_row][4]
                new_qty = int(current_qty) - order_qty
                inventory[position_row][4] = new_qty
                fulfillment_temp = (str(upc)+","+str(order_qty)+","+str(current_qty)).split(",")
                fulfillment_order.append(fulfillment_temp)

            else:
                print("\nThe article does not exist")
    r = 0
    l = len(fulfillment_order)
    file_string = ""
    
    while r < l:
        if r < l:
            row_value = str(fulfillment_order[r][0]) + "," + str(fulfillment_order[r][1])+ "\n"
            file_string = file_string + row_value
        r+=1

    outputfile = open(order_name + '.txt', 'w')
    outputfile.write(file_string)
    outputfile.close()

            
    print()

                       
# End of PO Management Functions;
# Start of Inventory Management
# ML
def get_inventory():
    inventory_file = "inventory"
    while not os.path.exists(inventory_file +".txt"):
        print("\nInventory database not found, enter new database")
        inventory_file = input("Enter Inventory file name: ")    

    inventory_file = open(inventory_file + ".txt", 'r')
    article_edit= "No"
    while article_edit != "":
        article_edit = inventory_file.readline()
        if article_edit != "":
            article_edit2 = article_edit.strip()
            temp = article_edit2.split(",")
            inventory.append(temp)
            
    inventory.sort(reverse=True)
    inventory_file.close()
    
#RHEA
def write_inv():
    r = 0
    l = len(inventory) - 1
    file_string = ""
    
    while r <= l:
        if r <= l:
            row_value = str(inventory[r][0]) + "," + str(inventory[r][1]) + "," + str(inventory[r][2]) + "," + str(inventory[r][3]) + "," + str(inventory[r][4]) + "," + str(inventory[r][5]) + "," + str(inventory[r][6]) + "\n"
            file_string = file_string + row_value
        r+=1

    outputfile = open('inventory.txt', 'w')
    outputfile.write(file_string)
    outputfile.close()
    
#RHEA
def change_sale_val ():
    global inventory
    UPC = input ('\nWhat is the UPC of the item to change : ')
    r = find_refId(UPC, inventory)
    if r.isdigit() == True:
        r = int(r)
        current_price = inventory[r][3]
        print (f"The current price is ${current_price}")
        new_price_valid = True
        while new_price_valid == True:  
            new_price = input("Update price to: $")
            if new_price.isalpha() or isprice(new_price) == False:
                print("The price must be a number (ex: 10.99)")
            else:
                new_price = float(new_price)
                new_price_valid = False
        inventory[r][3] = new_price

    else:
        print("UPC not found.")

#ML
def display_cart():
    t_ref = gen_trans_id()
    r = 0
    l = len(trans_cart)
    subtotal = 0
    hst = 0
    total = 0
    while r < l:
        subtotal += (float(trans_cart[r][2]) * int(trans_cart[r][4]))
        hst += ((float(trans_cart[r][2])* int(trans_cart[r][4])) * .13)
        total += ((float(trans_cart[r][2]) * int(trans_cart[r][4])) * 1.13)
        r+=1
    print("The cart from Better Games contains the following;")
    print("    Description    |---| QTY |---------|   Price   |----")
    r_1 = 0
    l_1 = len(trans_cart)
    while r_1 < l_1:
        description = trans_cart[r_1][1]
        qty = trans_cart[r_1][4]
        price = trans_cart[r_1][2]
        print(f"{description:^20}---{qty:^7}---------{price:^13}----")
        r_1 += 1
        
        
    print(f"Subtotal ------------------------------ ${subtotal:10,.2f}")
    print(f'HST ----------------------------------- ${hst:10,.2f}')
    print(f'Total --------------------------------- ${total:10,.2f}\n')
    print(f"Transaction Reference: {t_ref}")

    approve = input("Complete Transaction^ (Y/N): ")
    # PB & ML
    if approve.upper() == "Y":
        r_2 = 0
        l_2 = len(trans_cart)
        while r_2 < l_2:
            inv_r = int(find_refId(trans_cart[r_2][0], inventory))
            current_qty = int(inventory[inv_r][4])
            new_qty = current_qty - int(trans_cart[r_2][4])
            inventory[r_2][4] = new_qty
            r_2 += 1
        
        r_3 = 0
        l_3 = len(trans_cart)
        while r_3 < l_3:
            trans_log_temp = (str(t_ref+","+trans_cart[r_3][0]+','+trans_cart[r_3][1]+','+trans_cart[r_3][2]+','+trans_cart[r_3][4])).split(",")
            trans_log.append(trans_log_temp)
            r_3 += 1
            
        trans_cart.clear()
        print("\n Transaction has been approved, qty removed from inventory.\n")
        
    else:
        trans_cart.clear()

#PB
def transaction_processing():
    global inventory
    upc = "val"
    while upc != "":
        print("\nEnter blank to end transaction")
        if upc != "":
            upc = input("What is the upc of the products to purchase: ")
            position_row = find_refId(upc, inventory)
            if position_row.isdigit() == True:
                position_row = int(position_row)
                qty_verify = True
                while qty_verify == True:
                    pur_qty = input("Add to cart QTY (ex. 1): ")
                    if pur_qty.isdigit():
                        qty_verify = False
                    else:
                        print("Quantity must be a number.")
                description = inventory[position_row][1]
                price = inventory[position_row][3]
                current_qty = inventory[position_row][4]
                trans_temp_list = str(upc+","+description+','+price+','+current_qty+','+str(pur_qty)).split(",")
                trans_cart.append(trans_temp_list)
                

            else:
                print("\nThe article does not exist")

    display_cart()
    

def daily_report(): #RHEA & small help from PB
    file_name = date_f_now + "-Report.txt"
    file = open(file_name, "w")

    #Calculation part of code
    r_cal = 0
    l_cal = len(trans_log)
    Gross_Revenue, hst_collected, total = 0, 0, 0
    while r_cal < l_cal:
        Gross_Revenue += (float(trans_log[r_cal][3]) * int(trans_log[r_cal][4]))
        hst_collected += ((float(trans_log[r_cal][3])* int(trans_log[r_cal][4])) * .13)
        total = (float(Gross_Revenue) + float(hst_collected))
        r_cal += 1
    
    global ID_NUM
    number_of_sale = ID_NUM - 1
    file_content_items = ""                                                         
    file_content_title = "#REF# |  -----UPC-----  |  Article  Description  |  $Amount$  |  QTY\n"
    row = 0
    length = len(trans_log)

    revenue_2f = f'${Gross_Revenue:,.2f}'
    hst_2f = f'${hst_collected:,.2f}'
    total_2f = f'${total:,.2f}'
    
    while row < length:
        file_content_items += f"{str(trans_log[row][0]):^5}   {str(trans_log[row][1]):^15}   {str(trans_log[row][2]):^22}     ${float(trans_log[row][3]):,.2f}   {str(trans_log[row][4]):^5}\n"
        row += 1

    file_content = file_content_title + file_content_items
    file_header = f"""           Better Games daily report for {date_f_now}
      |  Total Collected  |   Taxes   |  Gross Revenue  |
         {total_2f:^17} {hst_2f:^11} {revenue_2f:^17}
\n\n\n\n\n\n"""
    full_str_output = file_header + file_content
    file.write(full_str_output)
    trans_log.clear()
    file.close()
   


# Start of menu - GROUP EFFORT
def main():
    get_inventory()
    choice = ""
    while choice.upper() != "E":
        menuA()
        choice = input("enter your choice: ")
        if choice == "1":
            menu_1()
            choice_1 = input("Enter your choice: ")
            if choice_1 == "1":
               po_name = input("Enter PO file name (ex. PO00001): ")
               while not os.path.exists(po_name + ".txt"): #PB
                   print("PO name does not exist.")
                   po_name = input("Enter PO file name: ")    
               get_PO_articles(po_name) 
            elif choice_1 == "2":
                po_send()
           
            else:
                print("The selection does not exist in po management.")

            
        elif choice == "2":
            menu_2()
            choice_2 = input("Enter your choice: ")
            if choice_2 == "1":
                transaction_processing()
            elif choice_2 == "2":
                change_sale_val()
            else:
                print()
            
        elif choice == "3":
            daily_report()
            write_inv()
        elif choice.upper() == "E":
            print("Have a nice day\n")
        else:
            print("The selected option does not exist.\n")
            
# End of menu
            
main()