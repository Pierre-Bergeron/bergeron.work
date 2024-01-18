# Python Add Student Grades to 2D Array.
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

table_str = "Student           |  Score  |  grade  | age |"


def get_grade(score):
    grade = (score / 20) * 100
    return grade

def table(table_str,name, score, grade, age):
    new_row = (f"{name}    |{score:.0f}/20   |{grade:.2f}%  |{age:.1f}")
    table_str = (f"""{table_str}\n{new_row}""")
    return table_str
   
    
def get_final_data(length, score, grade, age):
    avg_score = score / length
    avg_grade = grade / length
    avg_age = age / length
    return avg_score, avg_grade, avg_age

def main(table_str):
    print("""
Welcome to Grade Calculator!\n
          """)
    run_length = 0
    total_score = 0
    total_grade = 0
    total_age = 0
    keep_loop = ""
    
    
    while not (keep_loop == "X" or keep_loop == "x"):
        keep_loop = input("What is your name? ('X' to exit) ")
        if keep_loop == "X" or keep_loop == "x":
            print()
        else:
            score = int(input("What is the student score over 20pts? "))
            age = int(input("What is the student age? "))
            grade = get_grade(score)
            table_str = table(table_str, keep_loop, score, grade, age)
            run_length += 1
            total_score += score
            total_grade += grade
            total_age += age
        
        
    avg_score, avg_grade, avg_age = get_final_data(run_length, total_score, total_grade, total_age)   
    table_str = table(table_str, "Average:     ", avg_score, avg_grade, avg_age )
    print()
    print(table_str)
        
        
    
main(table_str)