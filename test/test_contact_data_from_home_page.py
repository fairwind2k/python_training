from random import randrange

from model.contact import Contact
import re
import allure


def test_name_on_home_page(app):
    with allure.step('Given a contact list from home page'):
        all_contacts = app.contacts.get_contacts_list()

    with allure.step('Random index selected from contact list'):
        index = randrange(len(all_contacts))

    with allure.step('Then I choose a contact from home page with index %s to the list' % index):
        contact_from_home_page = app.contacts.get_contacts_list()[index]

    with allure.step('Then I choose a contact from edit page with index %s to the list' % index):
        contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)

    with allure.step('Then the contact data from home page is equal to contact data from edit page'):
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


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
