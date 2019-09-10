import random
from model.contact import Contact


def test_delete_contact_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", homephone="333333333",
                          mobile="333333", workphone="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                          email2="fgghjj", homepage="wwwfghgj", secondaryphone="55556")
        app.contacts.create_new_contact(contact)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)
