CREATE TABLE contact_details (
 person_number VARCHAR(12) NOT NULL,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(50) NOT NULL,
 age VARCHAR(3) NOT NULL,
 home_number VARCHAR(11),
 parent_number VARCHAR(11),
 mobile_number VARCHAR(11),
 street VARCHAR(50),
 zip VARCHAR(10),
 city VARCHAR(50)
);

ALTER TABLE contact_details ADD CONSTRAINT PK_contact_details PRIMARY KEY (person_number);


CREATE TABLE receipt (
 receipt VARCHAR(50) NOT NULL,
 time TIMESTAMP(6) NOT NULL,
 genre VARCHAR(50),
 price VARCHAR(10) NOT NULL,
 skill_level VARCHAR(50) NOT NULL,
 lesson_type VARCHAR(50) NOT NULL,
 min_students INT,
 max_students INT
);

ALTER TABLE receipt ADD CONSTRAINT PK_receipt PRIMARY KEY (receipt);


CREATE TABLE staff (
 employment_id VARCHAR(10) NOT NULL,
 email VARCHAR(50) NOT NULL,
 person_number VARCHAR(12) NOT NULL
);

ALTER TABLE staff ADD CONSTRAINT PK_staff PRIMARY KEY (employment_id);


CREATE TABLE student (
 student_id VARCHAR(10) NOT NULL,
 email VARCHAR(50) NOT NULL,
 skill_level VARCHAR(50) NOT NULL,
 person_number VARCHAR(12) NOT NULL,
 family_id VARCHAR(10) NOT NULL
);

ALTER TABLE student ADD CONSTRAINT PK_student PRIMARY KEY (student_id);


CREATE TABLE application (
 application_id CHAR(10) NOT NULL,
 email VARCHAR(50) NOT NULL,
 audition_video VARCHAR(500),
 employment_id VARCHAR(10) NOT NULL,
 student_id VARCHAR(10) NOT NULL,
 person_number VARCHAR(12) NOT NULL
);

ALTER TABLE application ADD CONSTRAINT PK_application PRIMARY KEY (application_id);


CREATE TABLE lesson (
 lesson_id VARCHAR(10) NOT NULL,
 location VARCHAR(50) NOT NULL,
 instrument VARCHAR(50),
 employment_id VARCHAR(10) NOT NULL,
 receipt VARCHAR(50) NOT NULL
);

ALTER TABLE lesson ADD CONSTRAINT PK_lesson PRIMARY KEY (lesson_id);


CREATE TABLE lesson_attendees (
 attendance_id CHAR(10) NOT NULL,
 lesson_id VARCHAR(10) NOT NULL,
 student_id VARCHAR(10) NOT NULL
);

ALTER TABLE lesson_attendees ADD CONSTRAINT PK_lesson_attendees PRIMARY KEY (attendance_id);


CREATE TABLE payment (
 student_id VARCHAR(10) NOT NULL,
 amount VARCHAR(10),
 due_date TIMESTAMP(6),
 sibling_discount VARCHAR(10)
);

ALTER TABLE payment ADD CONSTRAINT PK_payment PRIMARY KEY (student_id);


CREATE TABLE rental_instrument (
 instrument_id VARCHAR(10) NOT NULL,
 instrument_type VARCHAR(50) NOT NULL,
 return_date TIMESTAMP(6),
 student_id VARCHAR(10),
 monthly_price INT NOT NULL,
 instrument_brand VARCHAR(50)
);

ALTER TABLE rental_instrument ADD CONSTRAINT PK_rental_instrument PRIMARY KEY (instrument_id);


CREATE TABLE salary (
 employment_id VARCHAR(10) NOT NULL,
 amount VARCHAR(10),
 due_date TIMESTAMP(6)
);

ALTER TABLE salary ADD CONSTRAINT PK_salary PRIMARY KEY (employment_id);


ALTER TABLE staff ADD CONSTRAINT FK_staff_0 FOREIGN KEY (person_number) REFERENCES contact_details (person_number);


ALTER TABLE student ADD CONSTRAINT FK_student_0 FOREIGN KEY (person_number) REFERENCES contact_details (person_number);


ALTER TABLE application ADD CONSTRAINT FK_application_0 FOREIGN KEY (employment_id) REFERENCES staff (employment_id);
ALTER TABLE application ADD CONSTRAINT FK_application_1 FOREIGN KEY (student_id) REFERENCES student (student_id);
ALTER TABLE application ADD CONSTRAINT FK_application_2 FOREIGN KEY (person_number) REFERENCES contact_details (person_number);


ALTER TABLE lesson ADD CONSTRAINT FK_lesson_0 FOREIGN KEY (employment_id) REFERENCES staff (employment_id);
ALTER TABLE lesson ADD CONSTRAINT FK_lesson_1 FOREIGN KEY (receipt) REFERENCES receipt (receipt);


ALTER TABLE lesson_attendees ADD CONSTRAINT FK_lesson_attendees_0 FOREIGN KEY (lesson_id) REFERENCES lesson (lesson_id);
ALTER TABLE lesson_attendees ADD CONSTRAINT FK_lesson_attendees_1 FOREIGN KEY (student_id) REFERENCES student (student_id);


ALTER TABLE payment ADD CONSTRAINT FK_payment_0 FOREIGN KEY (student_id) REFERENCES student (student_id);


ALTER TABLE rental_instrument ADD CONSTRAINT FK_rental_instrument_0 FOREIGN KEY (student_id) REFERENCES student (student_id);


ALTER TABLE salary ADD CONSTRAINT FK_salary_0 FOREIGN KEY (employment_id) REFERENCES staff (employment_id);


