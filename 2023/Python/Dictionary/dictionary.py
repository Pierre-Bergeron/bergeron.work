# Python Dictionary Basics
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

temp = []
dictionary = {}

def get_data():
    file = open("PO00001.txt", "r")
    
    value = "NOVAL"
    while value != "":
        value_raw = file.readline() 
        value = value_raw.strip()
        temp = value.split(",")
        if str(temp[0]) != "":
            upc = str(temp[0])
            del temp[0]
            dictionary[upc] = temp
    file.close()
            
        
def print_all():
    print("-----UPCs-----|--QTY--|--VAL--|--VAL--|")
    for upc in dictionary:
        val = []
        val = list(dictionary[upc])
        val1 = val[0]
        val2 = val[1]
        val3 = val[2]
        
        print(f"{upc:^14}  {val1:^5}   {val2:^5}   {val3:^5}")


get_data()
print_all()