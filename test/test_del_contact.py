from model.contact import Contact


def test_delete_first_contact(app):
    if app.contacts.count_contacts() == 0:
        contact = Contact(firstname="Ivan", lastname="Ivanov", address="fghghjhkkvb", home="333333333",
                          mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                          email2="fgghjj", homepage="wwwfghgj")
        app.contacts.create_new_contact(contact)
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.delete_first_contact()
    assert len(old_contacts) - 1 == app.contacts.count_contacts()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
