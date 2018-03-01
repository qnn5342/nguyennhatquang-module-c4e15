from mongoengine import Document, StringField, IntField, BooleanField



class Service(Document):
    name = StringField()
    gender = IntField() #0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
