import random
instruments = ["guitar","drums","piano","flute","bass", "violin","saxophone", "trumpet"]
brands = ["gibson", "harman professional", "shure", "yamaha", "fender musical instruments", "steinway musical instruments",
          "sennheiser", "roland", "kawai", "c.f. martin and company"]
p=0
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
