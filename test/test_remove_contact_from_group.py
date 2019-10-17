import random

import allure

from model.contact import Contact
from model.group import Group
import re


def test_remove_contact_from_group(db, orm, app):

    with allure.step('I check if exist any group with any contact in database '):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))

        if len(db.get_contact_list()) == 0 :
            contact = Contact(firstname="Test", lastname="Testov", address="addressTest", homephone="1111",
                              mobile="22222", workphone="3333", fax="44444", email="rttyru@com",
                              email2="fgghjj@mail.ru", homepage="wwwfghgj", secondaryphone="5555")
            app.contacts.create_new_contact(contact)
        #  get set of contacts that are in groups :
        contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
        # check existence of set contacts in groups:
        if len(contacts_in_groups_list) == 0:
            group = random.choice(db.get_group_list())
            contact = random.choice(db.get_contact_list())
            app.contacts.add_contact_in_group(contact.id, group.id)

    with allure.step('Random contact selected from contacts in group'):
        if len(contacts_in_groups_list) > 1:
            contact_id = int(clear(random.choice(contacts_in_groups_list)))
        else:
            contact_id = int(clear(contacts_in_groups_list[0]))
        contact = db.get_contact_from_id(contact_id)[0]

    with allure.step('I get a group ID with selected contact'):
        group_id = clear([item.id for item in db.get_group_by_contact_id(contact_id)][0])
        group = db.get_group_by_id(int(group_id))[0]

    with allure.step('I get list of contacts in selected group %s' % group):
        old_contacts = orm.get_contacts_in_group(group)

    with allure.step('When I remove a contact %s from the group' % contact):
        app.contacts.remove_contact_from_group(group.id, contact.id)

    with allure.step('Then the selected groups list of contacts is equal to the old list without selected contact'):
        new_contacts = orm.get_contacts_in_group(group)
        assert len(old_contacts) - 1 == len(new_contacts)


def clear(s):
    return re.sub("[() ,]", "", s)


