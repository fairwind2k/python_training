# -*- coding: utf-8 -*-
import allure
import pytest
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups

    with allure.step('Given a group list'):
        old_groups = db.get_group_list()

    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)

    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)