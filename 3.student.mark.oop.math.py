import math
import numpy as np
import curses as cus
class Entity:
    def __init__(self):
        self._id = 0
        self._name = ''
    
    def input(self):
        id =input("Enter the ID:\n")
        name = input("Enter the name:\n")
        self._id = id
        self._name = name
    def list(self):
        print(f"{self._id} | {self._name}")
    
    def get_id(self):
        return self._id

class Course(Entity):
    def input(self):
        id =int(input("Enter the course's ID:\n"))
        name = input("Enter the course's name:\n")
        self._id = id
        self._name = name

class Student(Entity):
    def __init__(self):
        super().__init__()

        self.__dob = ''
    def input(self):
        id =int(input("Enter the student's ID:\n"))
        name = input("Enter the student's name:\n")
        dob = input("Enter the student's DoB:\n")
        self._id = id
        self._name = name
        self.__dob = dob
    def list(self):
        print(f'ID: {self._id} | Name: {self._name} | DoB: {self.__dob}')

class Mark:
    def __init__(self):
        self._student_id = 0
        self._course_id = 0
        self._mark = 0.0 

    def setter(self,sid,cid,mark):
        self._student_id = sid
        self._course_id = cid
        self._mark = (float(mark))

    def list(self):
        print(f"Student ID: {self._student_id} | Course ID: {self._course_id} | Score: {self._mark}")

class School:
    def __init__(self):
        self.courses = []
        self.students = []
        self.marks = []
        self.gpa = np.empty(10,dtype=float)
    
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
        for i in range(num):
            m = input("Enter the marks(Input as follow: m1 m2 m3 ...)\n").split()
            n = input("Enter the credits(Input as follow: c1 c2 c3 ...):\n").split()

            marr = np.array(m,dtype=float)
            narr = np.array(n,dtype=int)

            gpa = np.sum(np.multiply(marr,narr))/np.sum(narr)
            self.gpa[i] = gpa
            print(gpa)
            
    def student_sort_by_gpa(self):
        np.sort(self.gpa)
        print(self.gpa)
    
school = School()
school.Input_Student()
school.Input_Courses()
school.Input_Marks()
school.List_Student()
school.List_Courses()
school.List_Marks()
school.calc_GPA()
#school.student_sort_by_gpa()

        
