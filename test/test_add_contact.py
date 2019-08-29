# -*- coding: utf-8 -*-
import random
import string

import pytest

from fixture.application import Application
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)