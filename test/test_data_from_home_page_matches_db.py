from model.contact import Contact
import re
import allure


def test_name_on_home_page(app, db):

    with allure.step('Given a contact list from home page'):
        ui_all_contacts = sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)

    with allure.step('Given a contact list from a database'):
        all_contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    with allure.step('Then the contact data from home page is equal to contact data from the database'):
        for i in range(len(ui_all_contacts)):
            assert ui_all_contacts[i].lastname == all_contacts_from_db[i].lastname
            assert ui_all_contacts[i].firstname == all_contacts_from_db[i].firstname
            assert ui_all_contacts[i].address == all_contacts_from_db[i].address
            assert ui_all_contacts[i].all_e_mails_from_home_page == merge_e_mails_like_on_home_page(all_contacts_from_db[i])
            assert ui_all_contacts[i].all_phones_from_home_page == merge_phones_like_on_home_page(all_contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))


def merge_e_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
