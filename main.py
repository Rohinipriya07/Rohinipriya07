import module.studentdetails
import module.subjects
import module.dbconnection
from tabulate import tabulate

print("Hi... Please enter module id from below \n 1. Admin \n 2.Teacher")
module_id = input("Type Module id and press Enter : ")


def add_student():
    print("Please Enter Below Student Details : ")
    name = input("Name : ")
    aadhar_card_number = input("Aadhar Card Number : ")
    parents_name = input("Parents Name : ")
    ph_number = input("Phone Number : ")
    class_name = input("Class Name : ")
    section = input("Section : ")
    student_details = module.studentdetails.StudentDetails(id, name, aadhar_card_number, parents_name, ph_number,
                                                           class_name, section)
    student_id = str(module.dbconnection.add_student(student_details))
    print("Student Details Added Successfully with Student Id : " + student_id)


def print_table_format(list):
    if list is None:
        print("No Records Found...")
    else:
        data = []
        for x in list:
            temp = [6]
            temp.append(x.id)
            temp.append(x.name)
            temp.append(x.aadhar_card_number)
            temp.append(x.parents_name)
            temp.append(x.ph_number)
            temp.append(x.class_name)
            temp.append(x.section)
            data.append(temp)
    print(tabulate(data, headers=["Student Id", "Student Name", "Aadhar Card Number", "Parents Name", "Phone Number",
                                  "Class Name", "Section"]))


def view_student():
    list = module.dbconnection.fetch_all_students()
    print_table_format(list)


def update_student():
    student_id = int(input("Please Enter Student ID to be Updated : "))
    details = module.dbconnection.fetch_student_details_by_id(student_id)
    if details is None:
        print("Student Details Not Found with the Given Id. Thank you")
    else:
        list = []
        list.append(details)
        print_table_format(list)
        print("Please select which data to be updated. \n1.Name\n2.Aadhar Card Number\n3.Parents Name\n4.Phone "
              "Number\n5.Class Name\n6.Section")
        update_option = int(input("Select the Option : "))
        if update_option == 1:
            details.name = input("Name : ")
        elif update_option == 2:
            details.aadhar_card_number = input("Aadhar Card Number : ")
        elif update_option == 3:
            details.parents_name = input("Parents Name : ")
        elif update_option == 4:
            details.ph_number = input("Phone Number : ")
        elif update_option == 5:
            details.class_name = input("Class Name : ")
        elif update_option == 6:
            details.section = input("Section : ")
        else:
            print("Invalid Option. Please try again later... Thank You !!!")
        module.dbconnection.update_student_details(details)
        print("Student Details Updated Successfully...!!!")


def delete_student():
    student_id = int(input("Please Enter Student ID to be Deleted : "))
    details = module.dbconnection.fetch_student_details_by_id(student_id)
    if details is None:
        print("Student Details Not Found with the Given Id. Thank you")
    else:
        list = []
        list.append(details)
        print_table_format(list)
        delete = input("\nDo you want to delete ? Y/N  : ")
        if delete.lower() == "y":
            module.dbconnection.delete_student_details(student_id)
            print("Student Detail Deleted Successfully...!!!")
        else:
            print("\nThank You")


def enter_marks():
    student_id = int(input("Please Enter Student ID  : "))
    details = module.dbconnection.fetch_student_details_by_id(student_id)
    if details is None:
        print("Student Details Not Found with the Given Id. Thank you")
    else:
        list = []
        list.append(details)
        print_table_format(list)
        exam = input("\n Exam Type (Quarterly/Half Yearly/Annual) : ")
        print("Please Enter Below Mark Details : ")
        math = input("Maths : ")
        science = input("Science : ")
        social = input("Social : ")
        language = input("Language : ")
        mark_details = module.subjects.Subject(math, science, social, language)
        module.dbconnection.enter_marks(student_id, exam, mark_details)
        print("Student Mark Details Saved Successfully...!!!")


def filter_failed_students():
    print("\nSelect Subject Name from below.\n1.Math\n2.Science\n3.Social\n4.Language ")
    sub = int(input("Type your selection : "))
    if sub == 1:
        list = module.dbconnection.filter_failed_students("Math")
    elif sub == 2:
        list = module.dbconnection.filter_failed_students("Science")
    elif sub == 3:
        list = module.dbconnection.filter_failed_students("Social")
    elif sub == 4:
        list = module.dbconnection.filter_failed_students("Language")
    else:
        print("Invalid Option. Please try again later... Thank You !!!")

    if list is None:
        print("No Records Found...")
    else:
        data = []
        for x in list:
            temp = [6]
            temp.append(x.student.id)
            temp.append(x.student.name)
            temp.append(x.examtype)
            temp.append(x.mark.math)
            temp.append(x.mark.science)
            temp.append(x.mark.social)
            temp.append(x.mark.language)
            data.append(temp)
    print(tabulate(data, headers=["Student Id", "Student Name", "Exam Type", "Math", "Science",
                                  "Social", "Language"]))

if module_id == "1":
    print("You logged in as Admin User. Please select any one of the below options ")
    print("1. Add student details \n2. View student details \n3. Update student details \n4. Delete student details")
    option = input("Type Operation Id and press Enter : ")
    if option == "1":
        add_student()
    elif option == "2":
        view_student()
    elif option == "3":
        update_student()
    elif option == "4":
        delete_student()
    else:
        print("Invalid Option. Please try again later... Thank You !!!")


elif module_id == "2":
    print("You logged in as Teacher User. Please select any one of the below options ")
    print("1. Enter Marks \n2. Filter Failed Students")
    option = input("Type Operation Id and press Enter : ")
    if option == "1":
        enter_marks()
    elif option == "2":
        filter_failed_students()
    else:
        print("Invalid Option. Please try again later... Thank You !!!")
else:
    print("Invalid Option. Please try again later... Thank You !!!")
