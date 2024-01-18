# Python English to Morse Code Translator
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

morse_code = [[" ", " "],[",","--..--"],[".",".-.-.-"],["?","..--.."],
              ["0","-----"],["1",".----"],["2","..---"],["3","...--"],
              ["4","....-"],["5","....."],["6","-...."],["7","--..."],
              ["8","---.."],["9","----."],["A",".-"],["B","-..."],
              ["C","-.-."],["D","-.."],["E","."],["F","..-."],
              ["G", "--."],["H","...."],["I",".."],["J",".---"],
              ["K","-.-"],["L",".-.."],["M","--"],["N","-."],
              ["O","---"],["P",".--."],["Q","--.-"],["R",".-."],
              ["S","..."],["T","-"],["U","..-"],["V","...-"],
              ["W",".--"],["X","-..-"],["Y","-.-"],["Z","--.."]]
phrase_str = []

def  get_morse(value):
    r = 0
    l = len(morse_code)
    while r < l:
        if value == morse_code[r][0]:
            p_val = morse_code[r][1]
            return str(p_val)
        else:
            r += 1
            
    if r >= l:
        print("Does not exist")
            
def gen_morse(listA):
    l = len(listA)
    p = 0
    trans_msg = ""
    while p < l:
        if p < l:
            value = get_morse(listA[p])
            trans_msg = trans_msg + str(value)
            p += 1
        
    return trans_msg
 
def main():
    phrase = "My phrase"
    while phrase != "":
        phrase = input("Enter the phrase to translate (Blank to exit): ")
        if phrase != "":
            phrase_str[:] = phrase.upper()
            msg = gen_morse(phrase_str)
            print(f"The message in morse code is: {msg}")
            
main()