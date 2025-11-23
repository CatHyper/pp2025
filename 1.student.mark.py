#global data struct
student_roster = []
course_catalog={}
marks_collection={}


#input number of students
def studentPopulation():
    number = int(input("Pls enter the number of students in the class:\n"))
    return number



#input the student informations
def studentInfo():
    for i in range(1,studentPopulation()+1,1):
        print(f"Student {i}:\n")
        ID = input("The student ID:\n")
        name = input("Student's name:\n")
        DoB = input("Enter the student's DoB:\n")
        student_roster.append({"ID": ID,"Name": name,"DoB":DoB})
    print("Here is what inside the student roster:\n")
    [print(x) for x in student_roster]
    print("\n")
    
    
    

def main():
    while True:
        print("Student management system!")
        print("1.New class\n")
        print("2.List\n")
        print("3.Test function sect")
        print("0.Exit\n")
        choice = int(input("Enter your selection(0-3):\n"))
        if choice == 1:
            print("test")   
             
        elif choice == 2:
            print("test")
        elif choice == 3:
            print("test3: Input student info")
            studentInfo()
            
            
        elif choice == 0:
            print("Exiting...")
            break

        elif choice <0 or type(choice) != 'int':
            print("Please enter the choice available in the selection!\n")
            print("--------------------")
if __name__=="__main__":
    main()
