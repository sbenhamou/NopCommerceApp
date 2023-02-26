# from faker import Faker
# from openpyxl import Workbook
#
# wb = Workbook()
# ws = wb.active
# fake_data = Faker('fr_FR')
#
# for i in range(1, 11):
#     ws.cell(row=i, column=1).value = fake_data.name()
#     ws.cell(row=i, column=2).value = fake_data.email()
#     ws.cell(row=i, column=3).value = fake_data.address()
# wb.save("./TestData/testData.csv")

import csv
from faker import Faker

# create a Faker instance
fake = Faker('fr_FR')

# create a list of headers for the csv file
headers = ['Name', 'Address', 'Email', 'Phone Number']

# create a list of fake data to write to the csv file
data = []
for _ in range(10):
    row = [fake.name(), "12 rue Vincent Scotto 72000 Le Mans", fake.email(), fake.phone_number()]
    data.append(row)

# open the csv file in write mode
with open('fake_data.csv', mode='w', newline='') as file:

    # create a csv writer object
    writer = csv.writer(file)

    # write the headers to the csv file
    writer.writerow(headers)

    # write the fake data to the csv file
    writer.writerows(data)

    # close the file
    file.close()