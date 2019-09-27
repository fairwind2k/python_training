import random

from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(db, orm, app):
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="Test", lastname="Testov", address="addressTest", homephone="1111",
                          mobile="22222", workphone="3333", fax="44444", email="rttyru@com",
                          email2="fgghjj@mail.ru", homepage="wwwfghgj", secondaryphone="5555")
        app.contacts.create_new_contact(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # get random group from group list
    group = random.choice(old_groups)
    print("\nselected group", group)
    if len(orm.get_contacts_in_group(group)) > 0:
        print('\norm.get_contacts_in_group(group) ', orm.get_contacts_in_group(group))
        if len(orm.get_contacts_in_group(group)) > 1:
            contact = random.choice(list(orm.get_contacts_in_group(group)))
        else:
            contact = orm.get_contacts_in_group(group)[0]
        print('contact', contact)
        print('\ngroup.id ', group.id)
        print('\ncontact.id ', contact.id)
        app.contacts.remove_contact_from_group(group.id, contact.id)
        print('\norm.get_contacts_in_group(group) new', orm.get_contacts_in_group(group))
        contacts_from_selected_group = app.contacts.get_contact_in_selected_group(group.id)
        print('contacts_from_selected_group ' , contacts_from_selected_group)
        assert orm.get_contacts_in_group(group) == sorted(contacts_from_selected_group)
    else:
        print('Selected group has no contacts. Try again.')


        # else:
        #     print('Assertion failed. Try again or create contact in random group')



