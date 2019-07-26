# -*- coding: utf-8 -*-
from contact import Contact
from application_contacts import ApplicationContacts
import pytest


@pytest.fixture
def app(request):
    fixture = ApplicationContacts()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login( username="admin", password="secret")
    app.create_new_contact(Contact( firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
                            mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                            email2="fgghjj", homepage="wwwfghgj"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact( firstname="", lastname="",
                            address="", home="", mobile="", work="", fax="", email="",
                            email2="", homepage=""))
    app.logout()
