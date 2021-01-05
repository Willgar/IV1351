import random
import names
import sys

genre = ["rock", "classic", "jazz", "metal", "country"]
skill = ["beginner", "advanced", "intermediate"]
gtype = ["individual", "ensemble", "group"]
locations = ["zoom", "local school", "homeadress"]
instruments = ["guitar","drums","piano","flute","bass", "violin","saxophone", "trumpet"]
#lessons
p = 0;
orig_stdout = sys.stdout
f = open('sql.txt', 'w')
sys.stdout = f
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
