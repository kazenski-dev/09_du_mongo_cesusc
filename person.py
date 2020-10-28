from connection import MongoConnect

class MyPerson():

    def save(self, name, last_name, office):
        connection_db = MongoConnect()
        person = {'name': name, 'last_name': last_name, 'office': office}
        connection_db.save(person)