from model.contact import Contact


def test_name_on_home_page(app, db):
    ui_all_contacts = app.contacts.get_contacts_list()
    contact_from_db = db.get_contact_list_with_all_pones_and_emails()
    assert sorted(ui_all_contacts, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
