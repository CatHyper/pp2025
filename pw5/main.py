from input import School
import zipfile
import os

# Define the name of the zip file and the files to be included
zip_filename = 'students.dat'
data_files = ['students.txt', 'courses.txt', 'marks.txt']

# Unzip data files if the zip file exists
if os.path.exists(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zf:
            zf.extractall()
            print(f"Data extracted from {zip_filename}")
    except zipfile.BadZipFile:
        print(f"Warning: '{zip_filename}' is not a valid zip file. Starting fresh.")
    except Exception as e:
        print(f"An error occurred while reading {zip_filename}: {e}")

# Initialize the school, which will load data from the text files
school = School()

# Main menu loop
while True:
    print("\n--- School Management System ---")
    print("1. Add Students")
    print("2. Add Courses")
    print("3. Add Marks")
    print("4. List Students")
    print("5. List Courses")
    print("6. List Marks")
    print("7. Show Students Sorted by GPA")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        school.Input_Student()
    elif choice == '2':
        school.Input_Courses()
    elif choice == '3':
        school.Input_Marks()
    elif choice == '4':
        school.List_Student()
    elif choice == '5':
        school.List_Courses()
    elif choice == '6':
        school.List_Marks()
    elif choice == '7':
        school.student_sort_by_gpa()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please try again.")

# Save all data to text files
school.save_data()
print("Data saved to text files.")

# Zip the data files
try:
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in data_files:
            if os.path.exists(file):
                zf.write(file)
    print(f"Data compressed into {zip_filename}")
except Exception as e:
    print(f"An error occurred while creating {zip_filename}: {e}")

print("Exiting program.")
