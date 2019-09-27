import random

from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(db, orm, app):
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="Test", lastname="Testov", address="addressTest", homephone="1111",
                          mobile="22222", workphone="3333", fax="44444", email="rttyru@com",
                          email2="fgghjj@mail.ru", homepage="wwwfghgj", secondaryphone="5555")
        app.contacts.create_new_contact(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # get all groups
    old_groups = db.get_group_list()
    # get random group from group list
    group = random.choice(old_groups)
    print("\nselected group", group)
    # get list of contacts which are not in selected group
    list_of_contacts_not_from_group = list(orm.get_contacts_not_in_group(group))
    print("\nlist_of_contacts_not_from_group ", list_of_contacts_not_from_group)
    contact = random.choice(list_of_contacts_not_from_group)
    print('contact', contact)
    app.contacts.add_contact_in_group(contact.id, group.id)
    print("\norm.get_contacts_in_group(group) new ", orm.get_contacts_in_group(group))
    contacts_from_selected_group = app.contacts.get_contact_in_selected_group(group.id)
    print("contacts_from_selected_group new", contacts_from_selected_group)
    assert orm.get_contacts_in_group(group) == sorted(contacts_from_selected_group)
