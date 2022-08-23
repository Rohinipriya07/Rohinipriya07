import mysql.connector
import module.studentdetails
import module.subjects
import module.markdetails

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)


def add_student(student_details):
    # print("Inside DB Save :")
    mycursor = mydb.cursor()
    sql = "INSERT INTO studentmgnt.student_details ( student_name, aadhar_card_number, parents_name, ph_number, class_name, section) VALUES ( %s , %s , %s , %s , %s , %s )"
    val = (student_details.name, student_details.aadhar_card_number, student_details.parents_name
           , student_details.ph_number, student_details.class_name, student_details.section)

    mycursor.execute(sql, val)
    mydb.commit()
    # print("1 record inserted, ID:", mycursor.lastrowid)
    return mycursor.lastrowid


def fetch_student_details_by_id(student_id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studentmgnt.student_details where student_id = %s "
    val = (student_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    if len(result) != 0:
        myresult = result[0]
        details = module.studentdetails.StudentDetails(myresult[0], myresult[1], myresult[2], myresult[3], myresult[4],
                                                       myresult[5], myresult[6], myresult[7])
        return details
    else:
        return None


def update_student_details(student_details):
    mycurser = mydb.cursor()
    sql = "UPDATE studentmgnt.student_details SET student_name = %s, aadhar_card_number = " \
          "%s, parents_name = %s, ph_number = %s, class_name = %s, " \
          "section = %s WHERE student_id = %s "
    val = (student_details.name, student_details.aadhar_card_number, student_details.parents_name
           , student_details.ph_number, student_details.class_name, student_details.section, student_details.id)
    mycurser.execute(sql, val)
    mydb.commit()
    return None


def delete_student_details(student_id):
    mycurser = mydb.cursor()
    sql = "DELETE FROM studentmgnt.student_details WHERE student_id = %s "
    val = (student_id,)
    mycurser.execute(sql, val)
    mydb.commit()
    return None


def fetch_all_students():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studentmgnt.student_details"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) != 0:
        list = []
        for myresult in result:
            list.append(
                module.studentdetails.StudentDetails(myresult[0], myresult[1], myresult[2], myresult[3], myresult[4],
                                                     myresult[5], myresult[6], myresult[7]))
        return list
    else:
        return None


def enter_marks(student_id, exam, mark_details):
    mycurser = mydb.cursor()
    sql = "INSERT INTO studentmgnt.student_marks ( student_id, exam_type, math, science, social, language) VALUES " \
          "(%s, %s, %s, %s, %s, %s) "
    val = (student_id, exam, mark_details.math, mark_details.science, mark_details.social, mark_details.language)
    mycurser.execute(sql, val)
    mydb.commit()
    return None


def filter_failed_students(subject):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studentmgnt.student_marks where "
    if subject == "Math":
        sql += " math < 35 "
    elif subject == "Science":
        sql += "science <35 "
    elif subject == "Social":
        sql += "social <35 "
    elif subject == "Language":
        sql += " language <35"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) != 0:
        list = []
        for myresult in result:
            sub = module.subjects.Subject(myresult[3], myresult[4], myresult[5], myresult[6])
            student = fetch_student_details_by_id(myresult[1])
            if student is None:
                continue
            list.append(module.markdetails.MarkDetails(student, sub, myresult[2]))

        return list
    else:
        return None


def update_fee_paid(id, paid):
    mycurser = mydb.cursor()
    sql = "UPDATE studentmgnt.student_details SET fee_paid = %s WHERE student_id = %s "
    val = (paid, id)
    mycurser.execute(sql, val)
    mydb.commit()
    return None


def fetch_marks_by_student_id(id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studentmgnt.student_marks where student_id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    if len(result) != 0:
        list = []
        for myresult in result:
            sub = module.subjects.Subject(myresult[3], myresult[4], myresult[5], myresult[6])
            student = fetch_student_details_by_id(myresult[1])
            if student is None:
                continue
            list.append(module.markdetails.MarkDetails(student, sub, myresult[2]))

        return list
    else:
        return None