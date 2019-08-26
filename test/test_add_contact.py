# -*- coding: utf-8 -*-
import random
import string

import pytest

from fixture.application import Application
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="",
                      mobile="", workphone="", fax="", email="",
                      email2="", email3 ="", homepage="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
            homephone=random_string("homephone", 15), mobile=random_string("mobile", 15), workphone=random_string("workphone", 15),
            fax=random_string("fax", 15), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20),
            homepage=random_string("homepage", 15), secondaryphone=random_string("secondaryphone", 15)
            )
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)