from main import People

try:
    people_name = input("Enter Your Name")
    people_phonenumber = input("Enter Your Phone Number")
    people_email = input("Enter Your email")
    people_county = input("Enter Your County")
    people_gender = input("Enter Your Gender")
    people_religion = input("Enter Your Religion")
    people_password = input("Enter Your Password")

    People.create(name=people_name, phonenumber=people_phonenumber, email=people_email, county=people_county,
                  gender=people_gender, religion=people_religion, password=people_password)
    print("Registration Complete")

except:
    print("Incorrect input. Try Again")
