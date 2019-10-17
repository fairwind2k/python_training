import random

import allure

from model.contact import Contact
from model.group import Group
import re


def test_add_contact_in_group(db, orm, app):

    with allure.step('I check if exist any group with any contact in database '):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))

        contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
        if len(db.get_contact_list()) == 0 or len(db.get_contact_list()) == len(contacts_in_groups_list):
            contact = Contact(firstname="Test", lastname="Testov", address="addressTest", homephone="1111",
                              mobile="22222", workphone="3333", fax="44444", email="rttyru@com",
                              email2="fgghjj@mail.ru", homepage="wwwfghgj", secondaryphone="5555")
            app.contacts.create_new_contact(contact)

    with allure.step('I got a difference between list of all contacts from db and list of contacts in groups '):
        contacts_not_in_group = []
        if len(db.get_contact_list()) > len(contacts_in_groups_list):
            set_contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
            list_of_id_contacts_in_groups = [clear(elem) for elem in set_contacts_in_groups_list]
            contacts_id_list_from_db = sorted([item.id for item in db.get_contact_list()])
            contacts_not_in_group = list(set(contacts_id_list_from_db) - set(list_of_id_contacts_in_groups))

    with allure.step('Random contact selected from contacts not in group'):
        if len(contacts_not_in_group) > 1:
            contact_id = random.choice(contacts_not_in_group)
        else:
            contact_id = contacts_not_in_group[0]
        contact = db.get_contact_from_id(contact_id)[0]

    with allure.step('Random group selected from group list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)

    with allure.step('When I add a contact %s to the group' % contact ):
        old_list_of_contacts_in_selected_group = sorted(orm.get_contacts_in_group(group))
        app.contacts.add_contact_in_group(contact.id, group.id)

    with allure.step('Then the selected groups list of contacts is equal to the old list with the added contact'):
        assert len(old_list_of_contacts_in_selected_group) + 1 == len(orm.get_contacts_in_group(group))


def clear(s):
    return re.sub("[() ,]", "", s)