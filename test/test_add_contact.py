# -*- coding: utf-8 -*-
import random
import string
import pytest
import allure
from fixture.application import Application
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts

    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()

    with allure.step('When I add a contact %s to the list' % contact):
        app.contacts.create_new_contact(contact)

    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)