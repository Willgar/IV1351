import random
import names
import sys

genre = ["rock", "classic", "jazz", "metal", "country"]
skill = ["beginner", "advanced", "intermediate"]
gtype = ["individual", "ensemble", "group"]
locations = ["zoom", "local school", "homeadress"]
instruments = ["guitar","drums","piano","flute","bass", "violin","saxophone", "trumpet"]
brands = ["gibson", "harman professional", "shure", "yamaha", "fender musical instruments", "steinway musical instruments",
          "sennheiser", "roland", "kawai", "c.f. martin and company"]
p=0;
orig_stdout = sys.stdout
f = open('data.txt', 'w')
sys.stdout = f
#students
for x in range(200):
    year = random.randint(1980, 2019)*100000000
    month = random.randint(1,12)*1000000
    if(month==4 or month==6 or month==9 or month==11):
        day = random.randint(1,31)*10000
    elif(month==2):
        day = random.randint(1,28)*10000
    else:
        day = random.randint(1,30)*10000
    lastfour = random.randint(1000, 9999)
    PN = year+month+day+lastfour
    firstname = names.get_first_name();
    lastname = names.get_last_name();
    age = int(2020-(year/100000000));
    phone = random.randint(1000000,9999999)
    phonenumber = 46730000000+phone
    ID = 1000+x
    r1 = random.randint(0,2)
    email = firstname + "@" + lastname + ".com"
    print("""INSERT INTO "contact_details" ("person_number", "first_name", "last_name", "age", "home_number", "parent_number", "mobile_number", "street", "zip", "city")
    VALUES ('"""+str(PN)+"""', '"""+str(firstname)+"""', '"""+str(lastname)+"""', '"""+str(age)+"""', '"""+str(phonenumber)+"""', NULL, NULL, NULL, NULL, NULL);""")
    print("""INSERT INTO "student" ("student_id", "email", "skill_level", "person_number", "family_id")
    VALUES ('SI"""+str(ID)+"""', '"""+str(email)+"""', '"""+str(skill[r1])+"""', '"""+str(PN)+"""', 'FI"""+str(ID)+"""');""")
    
#rental instruments    
for x in range(100):
    year = 210000
    month = random.randint(1,12)*100
    if(month==4 or month==6 or month==9 or month==11):
        day = random.randint(1,31)
    elif(month==2):
        day = random.randint(1,28)
    else:
        day = random.randint(1,30)
    date = year+month+day
    RID = 1000+x
    SID = random.randint(0,99)+1000
    r1 = random.randint(0, 7)
    r = random.randint(0,9)
    num2 = random.randint(1, 5)
    freeToRent = random.randint(1,10)
    price = 50+(20*num2)
    if(freeToRent<7):
        print("""INSERT INTO "rental_instrument" ("instrument_id", "instrument_type", "return_date", "student_id", "monthly_price", "instrument_brand")
        VALUES ('II"""+str(RID)+"""', '"""+str(instruments[r1])+"""', '"""+str(date)+"""', 'SI"""+str(SID)+"""', '"""+str(price)+"""', '"""+str(brands[r])+"""');""")
    else:
        print("""INSERT INTO "rental_instrument" ("instrument_id", "instrument_type", "return_date", "student_id", "monthly_price", "instrument_brand")
        VALUES ('II"""+str(RID)+"""', '"""+str(instruments[r1])+"""', """+str("NULL")+""", """+str("NULL")+""", '"""+str(price)+"""', '"""+str(brands[r])+"""');""")


#staff
for x in range(10):
    year = random.randint(1980, 2019)*100000000
    month = random.randint(1,12)*1000000
    if(month==4 or month==6 or month==9 or month==11):
        day = random.randint(1,31)*10000
    elif(month==2):
        day = random.randint(1,28)*10000
    else:
        day = random.randint(1,30)*10000
    lastfour = random.randint(1000, 9999)
    PN = year+month+day+lastfour
    firstname = names.get_first_name();
    lastname = names.get_last_name();
    age = int(2020-(year/100000000));
    phone = random.randint(1000000,9999999)
    phonenumber = 46730000000+phone
    ID = 1000+x
    r1 = random.randint(0,2)
    email = firstname + "@" + lastname + ".com"
    print("""INSERT INTO "contact_details" ("person_number", "first_name", "last_name", "age", "home_number", "parent_number", "mobile_number", "street", "zip", "city")
    VALUES ('"""+str(PN)+"""', '"""+str(firstname)+"""', '"""+str(lastname)+"""', '"""+str(age)+"""', '"""+str(phonenumber)+"""', NULL, NULL, NULL, NULL, NULL);""")
    print("""INSERT INTO "staff" ("employment_id", "email", "person_number")
    VALUES ('EI"""+str(ID)+"""', '"""+str(email)+"""', '"""+str(PN)+"""');""")
    
#lessons    
for x in range(500):
    time1 = random.randint(1, 12)*100
    time2= random.randint(1, 28)
    num1 = 210000+time1+time2
    num2 = random.randint(1, 5)
    price = 100+(50*num2)
    num3 = 1000+x
    SID = random.randint(0,9)+1000
    r3 = random.randint(0,2)
    r1 = random.randint(0,4)
    r2 = random.randint(0,2)
    r5 = random.randint(0,7)
    r4 = random.randint(0,2)
    maxsize=random.randint(12,32)
    minsize=random.randint(2,11)
    if(gtype[r3]=="individual"):
        print("""INSERT INTO "receipt" ("receipt", "time", "genre", "price", "skill_level", "lesson_type", "max_students", "min_students")
        VALUES ('RI"""+str(num3)+"""', '"""+str(num1)+"""', '"""+str(genre[r1])+"""', '"""+str(price)+"""', '"""+str(skill[r2])+"""', '"""+str(gtype[r3])+"""', NULL, NULL);""")
        print("""INSERT INTO "lesson" ("lesson_id", "location", "instrument", "employment_id", "receipt")
        VALUES ('LI"""+str(num3)+"""', '"""+str(locations[r4])+"""', '"""+str(instruments[r5])+"""', 'EI"""+str(SID)+"""', 'RI"""+str(num3)+"""');""")
        randomStudent = random.randint(1, 100)+1000;
        p = p+1
        pq = 1000+p
        print("""INSERT INTO "lesson_attendees" ("lesson_id", "student_id", "attendance_id")
        VALUES ('LI"""+str(num3)+"""', 'SI"""+str(randomStudent)+"""', 'AI"""+str(pq)+"""');""")
    if(gtype[r3]=="group"):
        print("""INSERT INTO "receipt" ("receipt", "time", "genre", "price", "skill_level", "lesson_type", "max_students", "min_students")
        VALUES ('RI"""+str(num3)+"""', '"""+str(num1)+"""', '"""+str(genre[r1])+"""', '"""+str(price)+"""', '"""+str(skill[r2])+"""', '"""+str(gtype[r3])+"""', '"""+str(maxsize)+"""', '"""+str(minsize)+"""');""")
        print("""INSERT INTO "lesson" ("lesson_id", "location", "instrument", "employment_id", "receipt")
        VALUES ('LI"""+str(num3)+"""', '"""+str(locations[r4])+"""', '"""+str(instruments[r5])+"""', 'EI"""+str(SID)+"""', 'RI"""+str(num3)+"""');""")
        index = random.randint(minsize, maxsize)
        for q in range(index):
            randomStudent = random.randint(1, 100)+1000;
            p = p+1
            pq = 1000+p
            print("""INSERT INTO "lesson_attendees" ("lesson_id", "student_id", "attendance_id")
            VALUES ('LI"""+str(num3)+"""', 'SI"""+str(randomStudent)+"""', 'AI"""+str(pq)+"""');""")
    if(gtype[r3]=="ensemble"):
        print("""INSERT INTO "receipt" ("receipt", "time", "genre", "price", "skill_level", "lesson_type", "max_students", "min_students")
        VALUES ('RI"""+str(num3)+"""', '"""+str(num1)+"""', '"""+str(genre[r1])+"""', '"""+str(price)+"""', '"""+str(skill[r2])+"""', '"""+str(gtype[r3])+"""', '"""+str(maxsize)+"""', '"""+str(minsize)+"""');""")
        print("""INSERT INTO "lesson" ("lesson_id", "location", "instrument", "employment_id", "receipt")
        VALUES ('LI"""+str(num3)+"""', '"""+str(locations[r4])+"""', '', 'EI"""+str(SID)+"""', 'RI"""+str(num3)+"""');""")
        index = random.randint(minsize, maxsize)
        for q in range(index):
            randomStudent = random.randint(1, 100)+1000;
            p = p+1
            pq = 1000+p
            print("""INSERT INTO "lesson_attendees" ("lesson_id", "student_id", "attendance_id")
            VALUES ('LI"""+str(num3)+"""', 'SI"""+str(randomStudent)+"""', 'AI"""+str(pq)+"""');""")

sys.stdout = orig_stdout
f.close()