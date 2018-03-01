from mongoengine import Document, StringField, IntField, BooleanField



class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1: male
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
