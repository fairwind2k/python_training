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

    # def get_contact_list_with_all_pones_and_emails(self):
    #     list = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(
    #             "select id, firstname, lastname, address, concat(home, mobile, work, phone2) as all_phones, concat(email, email2, email3) as all_emails from addressbook where deprecated='0000-00-00 00:00:00'")
    #
    #         for row in cursor:
    #             (id, firstname, lastname, address, all_phones, all_emails) = row
    #             list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
    #                                 address=address, all_phones_from_home_page=all_phones,
    #                                 all_e_mails_from_home_page=all_emails))
    #     finally:
    #         cursor.close()
    #     return list

    def destroy(self):
        self.connection.close()
