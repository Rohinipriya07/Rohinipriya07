create schema studentmgnt;

CREATE TABLE  studentmgnt.student_details  (
   student_id  int NOT NULL AUTO_INCREMENT,
   student_name  varchar(45) DEFAULT NULL,
   aadhar_card_number  varchar(45) DEFAULT NULL,
   parents_name  varchar(45) DEFAULT NULL,
   ph_number  varchar(45) DEFAULT NULL,
   class_name  varchar(45) DEFAULT NULL,
   section  varchar(45) DEFAULT NULL,
  PRIMARY KEY ( student_id )
) ;


CREATE TABLE studentmgnt.student_marks  (
   id  int NOT NULL AUTO_INCREMENT,
   student_id  int DEFAULT NULL,
   exam_type  varchar(45) DEFAULT NULL,
   math  varchar(45) DEFAULT NULL,
   science  varchar(45) DEFAULT NULL,
   social  varchar(45) DEFAULT NULL,
   language  varchar(45) DEFAULT NULL,
  PRIMARY KEY ( id )
) ;

