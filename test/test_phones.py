import allure

from model.contact import Contact
import re


def test_phones_on_home_page(app):

    with allure.step('Given a phones list from home page'):
        contact_from_home_page = app.contacts.get_contacts_list()[0]

    with allure.step('Given a phones list from edit page'):
        contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)

    with allure.step('Then the pones list from home page is equal to pones list from edit page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):

    with allure.step('Given a phones list from view page'):
        contact_from_view_page = app.contacts.get_contact_from_view_page(0)

    with allure.step('Given a phones list from edit page'):
        contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)

    with allure.step('Then the pones list from view page is equal to pones list from edit page'):
        assert contact_from_view_page.homephone == contact_from_edit_page.homephone
        assert contact_from_view_page.workphone == contact_from_edit_page.workphone
        assert contact_from_view_page.mobile == contact_from_edit_page.mobile
        assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))
