import numpy as np
import math
from Domains.course import Course
from Domains.student import Student
from Domains.mark import Mark
import os


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high].get_gpa()
    i = low - 1
    for j in range(low, high):
        if arr[j].get_gpa() < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def Input_Student(self):
        n = int(input("How many students to add:\n"))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    
    def Input_Courses(self):
        n = int(input("How many courses to add:\n"))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
            
    def exists(self,id,id_list):
        for i in id_list:
            if i.get_id()==id:
                return True
        return False
    
    def get_course_by_id(self, course_id):
        for course in self.courses:
            if course.get_id() == course_id:
                return course
        return None

    def Input_Marks(self):
        cid = int(input("Enter the course's ID for which you want to enter marks:\n"))
        if not self.exists(cid, self.courses):
            print(f"The course with the ID {cid} does not exist!")
            return
        
        sid = int(input("Enter the student's ID for whom you want to enter a mark:\n"))
        if not self.exists(sid, self.students):
            print(f"The student with the ID {sid} does not exist!")
            return
        
        mark_value = float(input("Enter the mark (0-20):\n"))
        if mark_value < 0 or mark_value > 20:
            print("Invalid mark. Please enter a value between 0 and 20.")
            return
        
        mark = Mark()
        mark.setter(sid, cid, math.floor(mark_value))
        self.marks.append(mark)

    def List_Marks(self):
        print("--/Marks/--")
        for m in self.marks:
            m.list()

    def List_Student(self):
        print("--/Students/--")
        for i in self.students:
            i.list()
        print('\n')

    def List_Courses(self):
        print("--/Courses/--")
        for i in self.courses:
            i.list()
        print('\n')

    def calculate_gpas(self):
        for student in self.students:
            student_marks = [mark for mark in self.marks if mark._student_id == student.get_id()]
            if not student_marks:
                student.gpa = 0.0
                continue

            total_credits = 0
            weighted_sum = 0
            
            for mark in student_marks:
                course = self.get_course_by_id(mark._course_id)
                if course:
                    credits = course.get_credits()
                    weighted_sum += mark._mark * credits
                    total_credits += credits

            if total_credits == 0:
                student.gpa = 0.0
            else:
                student.gpa = weighted_sum / total_credits
            
    def student_sort_by_gpa(self):
        self.calculate_gpas()
        
        n = len(self.students)
        if n == 0:
            print("No students to sort.")
            return

        sorted_students = self.students[:]
        quickSort(sorted_students, 0, n - 1)

        print("--- Students Sorted by GPA (Highest to Lowest) ---")
        for s in reversed(sorted_students):
            print(f"ID: {s.get_id()} | Name: {s.get_name()} | GPA: {s.get_gpa():.2f}")
        print()
