from input import School
import gzip
import pickle
import os

# Define the name of the pickle file
pickle_filename = 'students.dat'

# Load the school object from the pickle file if it exists
if os.path.exists(pickle_filename):
    try:
        with gzip.open(pickle_filename, 'rb') as f:
            school = pickle.load(f)
            print(f"Data loaded from {pickle_filename}")
    except (pickle.UnpicklingError, EOFError, gzip.BadGzipFile) as e:
        print(f"Warning: Could not load data from '{pickle_filename}'. Starting fresh. Error: {e}")
        school = School()
    except Exception as e:
        print(f"An unexpected error occurred while reading {pickle_filename}: {e}")
        school = School()
else:
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

# Save the school object to a compressed pickle file
try:
    with gzip.open(pickle_filename, 'wb') as f:
        pickle.dump(school, f)
    print(f"Data saved and compressed into {pickle_filename}")
except Exception as e:
    print(f"An error occurred while saving data to {pickle_filename}: {e}")

print("Exiting program.")
