from tkinter import *
from tkinter import ttk

import module.dbconnection


def format_details(details):
    if details is None:
        return []
    data = []
    for x in details:
        temp = []
        temp.append(x.id)
        temp.append(x.name)
        temp.append(x.aadhar_card_number)
        temp.append(x.parents_name)
        temp.append(x.ph_number)
        temp.append(x.class_name)
        temp.append(x.section)
        temp.append(x.fee_paid)
        data.append(temp)
    return data


def format_mark_details(details):
    if details is None:
        return []
    data = []
    for x in details:
        temp = []
        temp.append(x.student.id)
        temp.append(x.student.name)
        temp.append(x.examtype)
        temp.append(x.mark.math)
        temp.append(x.mark.science)
        temp.append(x.mark.social)
        temp.append(x.mark.language)
        data.append(temp)
    return data


def print_student_table(ws, data):
    set = ttk.Treeview(ws)
    set.pack()
    set['columns'] = (
        'id', 'name', 'aadhar_card_number', 'parents_name', 'ph_number', 'class_name', 'section', 'fee_paid')
    set.column("#0", width=0, stretch=NO)
    set.column("id", anchor=CENTER, width=80)
    set.column("name", anchor=CENTER, width=80)
    set.column("aadhar_card_number", anchor=CENTER, width=80)
    set.column("parents_name", anchor=CENTER, width=80)
    set.column("ph_number", anchor=CENTER, width=80)
    set.column("class_name", anchor=CENTER, width=80)
    set.column("section", anchor=CENTER, width=80)
    set.column("fee_paid", anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("id", text="Student ID", anchor=CENTER)
    set.heading("name", text="Student Name", anchor=CENTER)
    set.heading("aadhar_card_number", text="Aadhar Card Number", anchor=CENTER)
    set.heading("parents_name", text="Parents Name", anchor=CENTER)
    set.heading("ph_number", text="Phone Number", anchor=CENTER)
    set.heading("class_name", text="Class Name", anchor=CENTER)
    set.heading("section", text="Section", anchor=CENTER)
    set.heading("fee_paid", text="Fee Paid", anchor=CENTER)

    global count
    count = 0
    for record in data:
        set.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
        count += 1


def view_student_details():
    list = module.dbconnection.fetch_all_students()
    data = format_details(list)
    ws = Tk()
    ws.title('Student Details')
    ws.geometry('700x700')
    print_student_table(ws, data)

    Input_frame = Frame(ws)
    Input_frame.pack()

    id = Label(Input_frame, text="ID")
    id.grid(row=0, column=0)

    fee_paid = Label(Input_frame, text="Fees Paid ?")
    fee_paid.grid(row=0, column=1)

    id_entry = Entry(Input_frame)
    id_entry.grid(row=1, column=0)

    fee_paid_entry = Entry(Input_frame)
    fee_paid_entry.grid(row=1, column=1)

    def refresh():
        ws.destroy()
        view_student_details()

    def input_record():
        print("Updating fees paid details for student id : " + id_entry.get() + " Status : " + fee_paid_entry.get())
        module.dbconnection.update_fee_paid(id_entry.get(), fee_paid_entry.get())
        refresh()

    # button
    Input_button = Button(ws, text="Update", command=input_record)
    Input_button.pack()
    ws.mainloop()


def print_mark_table(ws, data):
    set = ttk.Treeview(ws)
    set.pack()
    set['columns'] = (
        'id', 'name', 'exam', 'math', 'science', 'social', 'language')
    set.column("#0", width=0, stretch=NO)
    set.column("id", anchor=CENTER, width=80)
    set.column("name", anchor=CENTER, width=80)
    set.column("exam", anchor=CENTER, width=80)
    set.column("math", anchor=CENTER, width=80)
    set.column("science", anchor=CENTER, width=80)
    set.column("social", anchor=CENTER, width=80)
    set.column("language", anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("id", text="Student ID", anchor=CENTER)
    set.heading("name", text="Student Name", anchor=CENTER)
    set.heading("exam", text="Exam Type", anchor=CENTER)
    set.heading("math", text="Maths", anchor=CENTER)
    set.heading("science", text="Science", anchor=CENTER)
    set.heading("social", text="Social", anchor=CENTER)
    set.heading("language", text="Language", anchor=CENTER)

    global count
    count = 0
    for record in data:
        set.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[5]))
        count += 1


def view_marks():
    ws = Tk()
    ws.title('Student Mark Details')
    ws.geometry('700x700')

    Input_frame = Frame(ws)
    Input_frame.pack()

    id = Label(Input_frame, text="Enter Student ID")
    id.grid(row=0, column=0)

    id_entry = Entry(Input_frame)
    id_entry.grid(row=1, column=0)

    def input_record():
        list = module.dbconnection.fetch_marks_by_student_id(id_entry.get())
        data = format_mark_details(list)
        print_mark_table(ws, data)

    # button
    Input_button = Button(ws, text="Fetch Marks", command=input_record)
    Input_button.pack()
    ws.mainloop()


def project2():
    print("Please enter module id from below \n 1. Admin \n 2.Teacher")
    module_id = input("Type Module id and press Enter : ")
    if module_id == "1":
        view_student_details()
    elif module_id == "2":
        view_marks()
    else:
        print("Invalid Option. Please try again later... Thank You !!!")
