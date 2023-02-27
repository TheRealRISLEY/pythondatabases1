from main import People

mypeole = People.select()
for x in mypeole:
    print(x.name,x.phonenumber,x.email,x.county,x.gender,x.religion,x.password)
