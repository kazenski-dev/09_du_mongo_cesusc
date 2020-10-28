from person import MyPerson

user_name = ""
user_last_name = ""
user_office = ""

each_person = MyPerson()

user_name = input("Insert the name: ")
user_last_name = input("Insert the last name: ")
user_office = input("Insert the office: ")

each_person.save(user_name, user_last_name,user_office)