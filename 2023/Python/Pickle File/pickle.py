# Python Pickling File Basics
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

champions = {}
import pickle

def get_data():
    file = open("Stanley_Cup_Champions.txt", "r")
    
    value = "NoVal"
    year = "0000"
    champion = "None"
    val_position = 0
    while value != "":
        champions[year] = champion
        value_ncl = file.readline() 
        value = value_ncl.strip()
        val_position = (val_position + 1) % 2
        if val_position == 1:
            year = value
        else:
            champion = value
            
def print_all():
    for year in champions:
        print(year, champions[year])

def look_up(champions, year):
    print(champions.get(year, 'Not found.'))
    
def save_data(champions):
    outfile = open("champions.dat", "wb")
    pickle.dump(champions, outfile)
    outfile.close()

         
def main():
    value = "Value"
    get_data()
    while value != "":
        value = input("Enter a year (Blank to exit): ")
        if value != "":
            look_up(champions, value)
            
        else:
            print("Good Bye")
                  
    save_data(champions)
    
main()