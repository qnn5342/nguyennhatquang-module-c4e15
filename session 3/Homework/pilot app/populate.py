import mlab
from Module.service import Service
from faker import Faker
from random import randint, choice
from random_data import new_list, char_list

mlab.connect()

girls_list = ["Tú Linh",'Midu','Chi Pu','Kiều Anh hera','Tâm tít','Khải Ngân','Mie Nguyễn']
image_list = ['https://media2.thethaovanhoa.vn/2017/02/25/14/54/tu-linh-8.jpg','https://znews-photo-td.zadn.vn/w660/Uploaded/Yfrur/2016_08_11/IMG_6915.JPG','https://cdn.tuoitre.vn/2017/chipu5-1507184976938-87-0-649-1000-crop-1507186319654.jpg','http://res1.talktv.vn/images/kieuanh.hera/designSetting/854x480/kieuanh.hera.jpg','http://anh.24h.com.vn/upload/2-2017/images/2017-06-12/1497240840-149723538838825-15590395-1190016414399936-7896151868935581809-n-1497197708380.jpg','http://image2.tin247.com/pictures/2014/04/09/mgo1397037399.jpg','http://image2.tin247.com/pictures/2015/03/21/aap1426885048.jpg']

fake = Faker()
for i in range(len(girls_list)):
    print("Saving service", i +1, '.....')
    service = Service(name= girls_list[i],
                        yob= randint(1990,2000),
                        gender= 1,
                        height= randint(150,180),
                        phone = fake.phone_number(),
                        address= fake.address(),
                        image = image_list[i],
                        measurements= new_list(),
                        description= char_list(),
                        status=choice([True, False]))
    service.save()
