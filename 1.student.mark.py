#global data struct
student_roster = []
course_catalog=[]
marks_collection={}


#input number of students
def studentPopulation():
    student = int(input("Pls enter the number of students in the class:\n"))
    return student

#input number of courses
def courseNumber():
    course = int(input("Pls enter the number of course:"))
    return course

#input the student informations
def studentInfo():
    for i in range(1,studentPopulation()+1,1):
        print(f"Student {i}:\n")
        ID = input("The student ID:\n")
        name = input("Student's name:\n")
        DoB = input("Enter the student's DoB:\n")
        student_roster.append({"ID": ID,"Name": name,"DoB":DoB})

#input the course infos
def courseInfo():
    for i in range(1,courseNumber()+1,1):
        print(f"Course {i}:\n")
        ID = input("The course ID:\n")
        name = input("Course's name:\n")
        course_catalog.append({"ID": ID,"Name": name})
    
def listStudent():
    print("Here is what inside the student roster:\n")
    [print(x) for x in student_roster]
    print("\n")

def listCourse():
    print("Here is what inside the course catalog:\n")
    [print(x) for x in course_catalog]
    print("\n")
    

def main():
    while True:
        print("Student Management System")
        print("1.Input Course Infos\n")
        print("2.List Courses\n")
        print("3.Input Student Info\n")
        print("4.List Students\n")
        print("0.Exit\n")
        choice = int(input("Enter your selection(0-4):\n"))
        if choice == 1:
            courseInfo()   
        elif choice == 2:
            listCourse()
        elif choice == 3:
            studentInfo()
        elif choice == 4:
            listStudent()
        elif choice == 0:
            print("Exiting...")
            break
        elif choice <0 or type(choice) != 'int':
            print("Please enter the choice available in the selection!\n")
            print("--------------------")
if __name__=="__main__":
    main()
