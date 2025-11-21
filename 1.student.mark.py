#global data struct
student_roster = []
course_catalog={}
marks_collection={}


#input number of students
def studentPopulation():
    number = int(input("Pls enter the number of students in the class:\n"))
    return number

#ask the user to input the student informations
def studentInfo():
    info = []
    for i in range(0,studentPopulation(),1):
        ID = int(input("The student ID:\n"))
        name = input("Student's name:\n")
        DoB = input("Enter the student's DoB:\n")
        info.append(ID,name,DoB)
    
    

def main():
    while True:
        print("Student management system!")
        print("1.New class\n")
        print("2.List\n")
        print("0.Exit\n")
        choice = int(input("Enter your selection(0-2):\n"))
        if choice == 1:
            print("test")   
             
        elif choice == 2:
            print("test")
            
        elif choice == 3:
            print("Exiting...")
            break

        if choice <=0 or type(choice) != 'int':
            print("Please enter the choice available in the selection!\n")
            print("--------------------")
if __name__=="__main__":
    main()
