# -*- coding: utf-8 -*-
from model.group import Group


def test_first_group(app):
    app.group.edit_first_group(Group(name="edit1", header="edit2", footer="edit3"))
