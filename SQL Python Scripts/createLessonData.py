import random
genre = ["rock", "classic", "jazz", "metal", "country"]
skill = ["beginner", "advanced", "intermediate"]
gtype = ["individual", "ensemble", "group"]
locations = ["zoom", "local school", "homeadress"]
emp = ["EI1000", "EI1001", "EI1002"]

for x in range(100):
    time1 = random.randint(1, 12)*100
    time2= random.randint(1, 30)
    num1 = 210000+time1+time2
    num2 = random.randint(1, 5)
    price = 100+(50*num2)
    num3 = 1000+x
    r3 = random.randint(0,2)
    q = (x)
    r1 = random.randint(0,4)
    r2 = random.randint(0,2)
    r3 = random.randint(0,2)
    r4 = random.randint(0,2)
    r5 = random.randint(0,2)
    print("""INSERT INTO "receipt" ("receipt", "time", "genre", "price", "skill_level", "lesson_type")
    VALUES ('RI"""+str(num3)+"""', '"""+str(num1)+"""', '"""+str(genre[r1])+"""', '"""+str(price)+"""', '"""+str(skill[r2])+"""', '"""+str(gtype[r3])+"""');""")
    print("""INSERT INTO "lesson" ("lesson_id", "location", "instrument", "employment_id", "receipt")
    VALUES ('LI"""+str(num3)+"""', '"""+str(locations[r4])+"""', '', 'EI100"""+str(r3)+"""', 'RI"""+str(num3)+"""');""")
