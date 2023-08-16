from Employee import Employee

choice = 0

while choice != 7:
    print("\n1. Insert Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Apply Raise")
    print("6. Update Salary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Employee.insert()
    elif choice == "2":
        Employee.display()
    elif choice == "3":
        Employee.search()
    elif choice == "4":
        Employee.delete()
    elif choice == "5":
        Employee.apply_raise()
    elif choice == "6":
        Employee.update_salary()
    elif choice == "7":
        break
    else:
        print("Invalid choice")

