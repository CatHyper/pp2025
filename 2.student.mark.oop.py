class Student:
    def __init__(self,id,name,DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
    #
    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__DoB}"
    #
    def get_student_ID(self):
        return self.__id
    def get_student_name(self):
        return self.__name
    def get_student_DoB(self):
        return self.__DoB
    #
    def set_student_ID(self,id):
        self.__id = id
    def set_student_name(self,name):
        self.__name = name
    def set_student_DoB(self,DoB):
        self.__DoB = DoB

class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    #
    def __str__(self):
        return f"ID: {self.__id} | Course: {self.__name}"
    #Getter
    def get_course_id(self):
        return self.__id
    def get_course_name(self):
        return self.__name
    #Setter
    def set_course_id(self,id):
        self.__id=id
    def set_course_name(self,name):
        self.__name = name

class ManageStudent:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    
    def inputStudent(self):
        try:
            n = int(input("Enter the number of students:\n"))
            for i in range(1,n+1):
                studentID = input(f"Enter student {i}'s ID:\n")
                studentName = input(f"Enter student {i}'s name:\n")
                studentDoB = input(f"Enter student {i}'s DoB:\n")
                student = Student(studentID,studentName,studentDoB)
                self.students.append(student)
            print("Done!\n")
        except ValueError:
            print("Please enter a reasonable amount of student:\n")
    def listStudent(self):
        print("--/Students/--\n")
        for i in self.students:
            print(i)
        print("\n")

    def inputCourse(self):
        try:
            n = int(input("Enter the number of courses:"))
            for i in range(1,n+1):
                courseID = input(f"Course {i}'s ID:\n")
                courseName = input(f"Course {i}'s name:\n")
                course = Course(courseID,courseName)
                self.courses.append(course)
            print("Done!\n")
        except ValueError:
            print("Please enter a reasonable amount of courses:\n")
    def listCourse(self):
        print("--/Available Courses/--\n")
        for i in self.courses:
            print(i)
        print("\n")

    def inputMark(self):
        pass

    def listMark(self):
        pass

def main():
    call = ManageStudent()
    while True:
        print("Student Management System")
        print("-------------------------")
        print("1.Input Course Infos\n")
        print("2.List Courses\n")
        print("3.Input Student Info\n")
        print("4.List Students\n")
        print("5.Input Marks\n")
        print("6.List Marks\n")
        print("0.Exit\n")
        choice = int(input("Enter your selection(0-6):\n"))
        if choice == 1:
            call.inputCourse()
        elif choice == 2:
            call.listCourse()
        elif choice == 3:
            call.inputStudent()
        elif choice == 4:
            call.listStudent()
        elif choice == 5:
            pass
            #inputMark()
        elif choice == 6:
            pass
            #listMark()
        elif choice == 0:
            print("Exiting...")
            break
        elif choice <0 or type(choice) != 'int':#try catch value error
            print("Please enter the choice available in the selection!\n")
            print("--------------------")
if __name__=="__main__":
    main()
