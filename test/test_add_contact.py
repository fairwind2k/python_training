# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contact(firstname="Modest", lastname="Ivanov", address="fghghjhkkvb", home="333333333",
                            mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                            email2="fgghjj", homepage="wwwfghgj")
    app.contacts.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contacts.get_contacts_list()
#     contact = Contact( firstname="", lastname="",
#                             address="", home="", mobile="", work="", fax="", email="",
#                             email2="", homepage="")
#     app.contacts.create_new_contact(contact)
#     new_contacts = app.contacts.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)