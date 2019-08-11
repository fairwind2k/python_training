# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contacts.count_contacts() == 0:
        contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", home="333333333",
                          mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                          email2="fgghjj", homepage="wwwfghgj")
        app.contacts.create_new_contact(contact)
    old_contacts = app.contacts.get_contacts_list()
    contacts_data = Contact(firstname="Test_firstname", lastname="Test_lastname")
    contacts_data.id = old_contacts[0].id
    app.contacts.modify_first_contact(contacts_data)
    assert len(old_contacts) == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0] = contacts_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#
# def test_edit_contact_lastname(app):
#     if app.contacts.count_contacts() == 0:
#         app.contacts.create_new_contact(
#             Contact(firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
#                     mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
#                     email2="fgghjj", homepage="wwwfghgj"))
#     app.contacts.modify_first_contact(Contact(lastname="New_lastname"))