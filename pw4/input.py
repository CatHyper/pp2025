import numpy as np
import math
from .Domains.course import Course
from .Domains.student import Student
from .Domains.mark import Mark

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
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
        self.courses = []
        self.students = []
        self.marks = []
        self.gpa = np.array([])
    
    def Input_Student(self):
        n = int(input("How many student:\n"))
        for i in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    
    def Input_Courses(self):
        n = int(input("How many courses:\n"))
        for i in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    
    def exists(self,id,id_list):
        for i in id_list:
            if i.get_id()==id:
                return True
        return False
    
    def Input_Marks(self):
        n1 = int(input("How many courses you want to enter mark:\n"))
        for i in range(n1):
            cid = int(input("Enter the course's ID for entering mark:\n"))
            if not self.exists(cid,self.courses):
                print(f"The course with the ID of {cid} does not exist!")
                print('\n')
                return
            n2 = int(input("How many students you want to give mark:\n"))
            for i in range(n2):
                sid = int(input("Enter the student' ID you want to enter the mark:\n"))
                if not self.exists(sid,self.students):
                    print(f"The student with the ID of {sid} does not exist!")
                    print('\n')
                    return
                mark = math.floor(float(input("Enter the mark(0-20):\n")))
                if mark < 0 or mark > 20:
                    print("Next time, enter the mark according to the instruction ;)")
                    return
                m = Mark()
                m.setter(sid,cid,mark)
                self.marks.append(m)
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

    def calc_GPA(self):
        num = int(input("How many student you want to calc GPA for:\n"))
        self.gpa = np.empty(num,dtype=float)
        for i in range(num):
            m = input("Enter the marks(Input as follow: m1 m2 m3 ...)\n").split()
            n = input("Enter the credits(Input as follow: c1 c2 c3 ...):\n").split()

            marr = np.array(m,dtype=float)
            narr = np.array(n,dtype=int)

            gpa = np.sum(np.multiply(marr,narr))/np.sum(narr)
            self.gpa[i] = gpa
            print('GPA = ',round(gpa))
            
    def student_sort_by_gpa(self):
        try: 
            n = len(self.gpa)
            if n == 0:
                print("No GPAs to sort.")
                return
            quickSort(self.gpa,0,n-1)
            print("Sorted GPAs:")
            for i in self.gpa:
                print(i, end=' ')
            print()
        except NameError:
            print('again!')
            return
        except TypeError:
            print('again')
            return
