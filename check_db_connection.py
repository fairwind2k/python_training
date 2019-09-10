# import pymysql.cursors
# from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # l = db.get_contact_list()
    l = db.get_contacts_not_in_group(Group(id="146"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass


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
