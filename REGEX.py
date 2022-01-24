import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

contacts_list = ''
with open('phonebook_raw.csv', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=',')
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
new_contacts = []
new_line = []
first_line = contacts_list[0]
contacts_list.pop(0)
for contact in contacts_list:
   new_line = contact[0].split(' ')
   firstname = contact[1].split(' ')
   surname = contact[2].split(' ')
   if len(firstname) > 1:
       new_line.extend(firstname)
   if len(surname) > 1:
       new_line.extend(surname)
   if len(new_line) == 2:
       new_line.insert(2,'')
   elif len(new_line) == 1:
       new_line.insert(1, '')
       new_line.insert(2, '')
   new_line.insert(3,contact[3])
   new_line.insert(4,contact[4])
   phone = contact[5].split('доб')
   f_phone = re.sub(r"(\+?7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\W*",
                   r"+7(\2)\3-\4-\5", phone[0])
   if len(phone) > 1:
       f_phone += re.sub(r"\W*(\d{4})\W*",r" доб.(\1)", phone[1])
   new_line.insert(5, f_phone)
   new_line.insert(6, contact[6])
   new_contacts.append(new_line)

temp_contacts = new_contacts.copy()
good_contacts = []
good_contacts.append(first_line)
for i in range(len(new_contacts)):
    temp_contacts.remove(new_contacts[i])
    isNeedAdd = True

    for l in range(len(good_contacts)):
        if new_contacts[i][0] == good_contacts[l][0]:
            isNeedAdd = False
    if isNeedAdd == True :
        good_contacts.append(new_contacts[i])

    for j in range(len(temp_contacts)):
        if new_contacts[i][0] == temp_contacts[j][0]:
            good_line = []

            for k in range(len(temp_contacts[j])):
                if new_contacts[i][k] == temp_contacts[j][k] :
                    good_line.append(new_contacts[i][k])
                else:
                    good_line.append(new_contacts[i][k]+temp_contacts[j][k])
            good_contacts.pop()
            good_contacts.append(good_line)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(good_contacts)