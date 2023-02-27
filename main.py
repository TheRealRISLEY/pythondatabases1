from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "RealRisley.db"))

class People(Model):
    name = CharField()
    phonenumber = CharField()
    email = CharField()
    county = CharField()
    gender = CharField()
    religion = CharField()
    password = CharField()

    class Meta:
        database = db


People.create_table(fail_silently=True)
