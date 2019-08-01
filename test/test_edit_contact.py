# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contacts.count_contacts() == 0:
        app.contacts.create_new_contact(
            Contact(firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
                    mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                    email2="fgghjj", homepage="wwwfghgj"))
    app.contacts.modify_first_contact(Contact(firstname="New name"))

    # app.contacts.modify_first_contact(Contact( firstname="New name", lastname="edit 2", address="edit 3", home="edit 4",
    #                         mobile="edit 5", work="edit 6", fax="edit 7", email="edit8@ru",
    #                         email2="test@edit9", homepage="www.test.test"))


def test_edit_contact_lastname(app):
    if app.contacts.count_contacts() == 0:
        app.contacts.create_new_contact(
            Contact(firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
                    mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                    email2="fgghjj", homepage="wwwfghgj"))
    app.contacts.modify_first_contact(Contact(lastname="New lastname"))