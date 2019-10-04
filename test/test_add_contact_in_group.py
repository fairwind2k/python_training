import random

from model.contact import Contact
from model.group import Group
import re


def test_add_contact_in_group(db, orm, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    #  get set of contacts that are in groups :
    contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
    if len(db.get_contact_list()) == 0 or len(db.get_contact_list()) == len(contacts_in_groups_list):
        contact = Contact(firstname="Test", lastname="Testov", address="addressTest", homephone="1111",
                          mobile="22222", workphone="3333", fax="44444", email="rttyru@com",
                          email2="fgghjj@mail.ru", homepage="wwwfghgj", secondaryphone="5555")
        app.contacts.create_new_contact(contact)
    # get difference between list of all contacts from db and list of contacts in groups
    contacts_not_in_group = []
    if len(db.get_contact_list()) > len(contacts_in_groups_list):
        set_contacts_in_groups_list = sorted(set([item.id for item in db.get_all_contacts_in_groups_list()]))
        list_of_id_contacts_in_groups = [clear(elem) for elem in set_contacts_in_groups_list]
        contacts_id_list_from_db = sorted([item.id for item in db.get_contact_list()])
        contacts_not_in_group = list(set(contacts_id_list_from_db) - set(list_of_id_contacts_in_groups))
    # print('\ncontacts_not_in_group', contacts_not_in_group)
    #  тут надо взять те контакты, что не входят в группы  и рандомно выбрать из списка
    if len(contacts_not_in_group) > 1:
        contact_id = random.choice(contacts_not_in_group)
    else:
        contact_id = contacts_not_in_group[0]
    contact = db.get_contact_from_id(contact_id)[0]
    old_groups = db.get_group_list()
    # get random group from group list
    group = random.choice(old_groups)
    old_list_of_contacts_in_selected_group = sorted(orm.get_contacts_in_group(group))
    app.contacts.add_contact_in_group(contact.id, group.id)
    # print("\norm.get_contacts_in_group(group) new ", orm.get_contacts_in_group(group))
    assert len(old_list_of_contacts_in_selected_group) + 1 == len(orm.get_contacts_in_group(group))
    # old_list_of_contacts_in_selected_group.append(contact)
    # print('\nold_list_of_contacts_in_selected_group +new_elem ', old_list_of_contacts_in_selected_group)


def clear(s):
    return re.sub("[() ,]", "", s)