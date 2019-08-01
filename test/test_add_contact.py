# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact


def test_add_contact(app):
    app.contacts.create_new_contact(Contact( firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
                            mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                            email2="fgghjj", homepage="wwwfghgj"))


def test_add_empty_contact(app):
    app.contacts.create_new_contact(Contact( firstname="", lastname="",
                            address="", home="", mobile="", work="", fax="", email="",
                            email2="", homepage=""))
