# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login( username="admin", password="secret")
    app.contacts.edit_contact(Contact( firstname="edit 1", lastname="edit 2", address="edit 3", home="edit 4",
                            mobile="edit 5", work="edit 6", fax="edit 7", email="edit8@ru",
                            email2="test@edit9", homepage="www.test.test"))
    app.session.logout()
