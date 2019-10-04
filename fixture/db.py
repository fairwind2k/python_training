import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3, homepage, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3, homepage,
                 phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, homephone=home, mobile=mobile, workphone=work,
                                    fax=fax, email=email, email2=email2, email3=email3, homepage=homepage,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_all_contacts_in_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id = row
                list.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list

    def get_contact_from_id(self, contact_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3, homepage, phone2 from addressbook where id=%s AND deprecated='0000-00-00 00:00:00'",  contact_id)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3, homepage,
                 phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, homephone=home, mobile=mobile, workphone=work,
                                    fax=fax, email=email, email2=email2, email3=email3, homepage=homepage,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_group_by_contact_id(self, contact_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id from address_in_groups where id=%s and deprecated='0000-00-00 00:00:00'", contact_id)
            for row in cursor:
                group_id = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_group_by_id(self, selected_group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where group_id=%s", selected_group_id)
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
