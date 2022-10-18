#!/usr/bin/env python3

import csv
from copy import deepcopy
from re import I
from turtle import color

import cv2
import numpy as np
from functions import Student, Teacher


def addCourseToStudent(course_to_add, courses_list):
    return courses_list.append(course_to_add)
    

def main():


    # define one instance of a DEM student
#     num_mec = 15543
#     nome = 'kmasido'
#     courses = ['PSR', 'SFP', 'SAVI']
#     age = 33
# 
#     num_mec1 = 15543
#     nome1 = 'kmasido'
#     courses1 = ['PSR', 'SFP', 'SAVI']
#     age1 = 33
# 
#     num_mec_a = 15543
#     nome_a = 'kmasido'
#     courses_a = ['PSR', 'SFP', 'SAVI']
#     age_a = 33
# 
#     # Alternative 2
#     num_mecs = [123123, 123123 , 12312 ]
#     names = ['Miguel', 'Armando', 'Pedro']
#     courses = [['PSR'],['PSR', 'SAVI'], ['PSR', 'SAVI', 'SFP']]
# 
# 
#     # Alternative 3
#     all_in_one = [{'name': 'Miguel', 'num_mec': 123124, 'courses': ['PSR']}, 
#                   {'name': 'Armando', 'num_mec': 123124, 'courses': ['PSR']}]
                  

    # Alternative 4
    # CLASSES
    a = int(4)

    s1 = Student('Andre', 14234, ['SAVI', 'TAC'], 56)
    s2 = Student('Joao', 32434, ['SAVI', 'PSR'], int(58))
    t1 = Teacher('José', ['SAVI'], int(44) )
    t1 = Teacher('José', ['SAVI'], int(30) , ['Gil'])

    print(s1.name)

#     print(s2)
#     print(t1)
# 
#     s1.addCourse('PSR')
#     t1.addStudent('Gil')
#     
#     print(s1)
#     print(t1)

if __name__ == "__main__":
    main()
