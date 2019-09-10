# -*- coding: utf-8 -*-
import random
import string

import pytest

from fixture.application import Application
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)