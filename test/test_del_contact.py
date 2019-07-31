from model.contact import Contact


def test_delete_first_contact(app):
    if app.contacts.count_contacts() == 0:
        app.contacts.create_new_contact(
            Contact(firstname="dfdfgh", lastname="ttttt", address="fghghjhkkvb", home="333333333",
                    mobile="333333", work="1111111111", fax="111111111111111111111", email="rttyru@rtrt",
                    email2="fgghjj", homepage="wwwfghgj"))
    app.contacts.delete_first_contact()
