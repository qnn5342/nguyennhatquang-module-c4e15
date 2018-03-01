import mlab
from Module.customer import Customer
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()
for i in range (50):
    print("Saving Customer", i +1, '.....')
    customer = Customer(name=fake.name(),
                        gender= randint(0,1),
                        email= fake.ascii_free_email(),
                        phone = fake.phone_number(),
                        job= fake.job(),
                        company= fake.company(),
                        contacted=choice([True, False]))
    customer.save()
