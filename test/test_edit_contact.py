# -*- coding: utf-8 -*-
import random

import allure

from model.contact import Contact


def test_edit_contact(app, db, check_ui):

    with allure.step('I check if exist contact in contact list'):
        if len(db.get_contact_list()) == 0:
            contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", homephone="333333333",
                              mobile="333333", workphone="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                              email2="fgghjj", homepage="wwwfghgj", secondaryphone="777777")
            app.contacts.create_new_contact(contact)

    with allure.step('Given a contact list from database'):
        old_contacts = db.get_contact_list()

    with allure.step('Random contact selected from contact list'):
        random_contact = random.choice(old_contacts)
        index = old_contacts.index(random_contact)

    with allure.step('Given a new contact data'):
        contacts_data = Contact(firstname="Mod", lastname="Mod")
        contacts_data.id = old_contacts[index].id

    with allure.step('When I edit a contact %s from the list' % contact):
        app.contacts.modify_contact_by_index(index, contacts_data)

    with allure.step('Then the new contact list is equal to the old list with the added new data %s' % contacts_data ):
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