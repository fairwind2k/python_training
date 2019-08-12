from random import randrange
from model.contact import Contact


def test_delete_contact_by_index(app):
    if app.contacts.count_contacts() == 0:
        contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", home="333333333",
                          mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                          email2="fgghjj", homepage="wwwfghgj")
        app.contacts.create_new_contact(contact)
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
