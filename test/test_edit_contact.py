# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", homephone="333333333",
                          mobile="333333", workphone="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                          email2="fgghjj", homepage="wwwfghgj", secondaryphone="777777")
        app.contacts.create_new_contact(contact)
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    index = old_contacts.index(random_contact)
    contacts_data = Contact(firstname="Mod", lastname="Mod")
    contacts_data.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contacts_data)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contacts_data
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)





#
# def test_edit_contact_lastname(app):
#     if app.contacts.count_contacts() == 0:
#         app.contacts.create_new_contact(
#             Contact(firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
#                     mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
#                     email2="fgghjj", homepage="wwwfghgj"))
#     app.contacts.modify_first_contact(Contact(lastname="New_lastname"))