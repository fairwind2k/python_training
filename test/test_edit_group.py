# -*- coding: utf-8 -*-
from model.group import Group


def test_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit1", header="edit2", footer="edit3"))
    app.session.logout()
