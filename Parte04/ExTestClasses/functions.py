#!/usr/bin/env python3

import csv
from copy import deepcopy

import cv2
import numpy as np
from colorama import Fore, Style


class Person:
    def __init__(self, name, age):
        self.name = name # copy local __init__ variable to class property

        print(type(age))
        if not type(age) == int:
            raise ValueError(Fore.RED +  'asneira !! a Idade tem de ser inteiro' + Style.RESET_ALL)
        self.age = age # copy local __init__ variable to class property
        print('Creating a new Person')

    def congratulate(self):
        print('Congratulations ' + self.name)
        self.age += 1

    def __str__(self):
        # Must return a string
        text = 'Person ' + self.name + ' has ' + str(self.age) + ' years old.'
        return text

    

class Student(Person):

    def __init__(self, name, num_mec, courses, age):
        print(type(age))
        super().__init__(name, age) # call the super class constructor
        self.num_mec = num_mec # copy local __init__ variable to class property
        self.courses = courses # copy local __init__ variable to class property
        print('Creating a new student')

    def addCourse(self, course_to_add):
        if not course_to_add in self.courses:
            self.courses.append(course_to_add)

    def __str__(self):
        # Must return a string
        text = self.name + ' has ' + str(self.age) + ' years old, num_mec=' + str(self.num_mec) + ' . Courses = ' + str(self.courses) 
        return text


class Teacher(Person):

    def __init__(self, name, courses, age, students=[]):
        super().__init__(name, age) # call the super class constructor
        self.courses = courses # copy local __init__ variable to class property
        self.students = students # copy local __init__ variable to class property
        print('Creating a new teacher')

    def addCourse(self, course_to_add):
        if not course_to_add in self.courses:
            self.courses.append(course_to_add)

    def addStudent(self, student_name):
        if not student_name in self.students:
            self.students.append(student_name)

    def __str__(self):
        # Must return a string
        text = 'Prof ' + self.name + ' has ' + str(self.age) + ' years old. ' + ' Courses = ' + str(self.courses) + ' , Students ' + str(self.students)
        return text
