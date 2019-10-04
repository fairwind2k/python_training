# import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import re

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def clear(s):
    return re.sub("[() ,]", "", s)

try:

    print('db.get_group_from_id ', db.get_group_by_contact_id('215') )
    for item in db.get_group_by_contact_id('215'):
        print(item)


    group_id = clear([item.id for item in db.get_group_by_contact_id('215')][0])

    l = db.get_group_list()
    index = int(group_id)
    m = db.get_group_by_id(81)

    print('group_id ', group_id)
    print("l", l)
    print("get_group_by_id", m[0])



finally:
     db.destroy()

# try:
#     print("\nget_all_contacts_in_groups_list ", db.get_all_contacts_in_groups_list())
#     set_contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
#     print('\nget_all_contacts_in_groups', set_contacts_in_groups_list)
#     list_of_id_contacts_in_groups = [clear(elem) for elem in set_contacts_in_groups_list]
#     print('\nlist_of_id_contacts_in_groups', list_of_id_contacts_in_groups)
#
#     contacts_id_list_from_db = sorted([item.id for item in db.get_contact_list()])
#     print('\ncontacts_id_list_from_db ', contacts_id_list_from_db)
#
#     contacts_not_in_group = list(set(contacts_id_list_from_db) - set(list_of_id_contacts_in_groups))
#     print('\ncontacts_not_in_group', contacts_not_in_group)
#
#     print('\ncontact 215 ', db.get_contact_from_id(215)[0])
#
# finally:
#     db.destroy()



# check  connection with ORM
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_contacts_not_in_group(Group(id="148"))
#     for item in l:
#       print(item)
#     print(len(l))
# finally:
#     pass



# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()



# через pymysql:
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
