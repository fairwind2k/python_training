import random

import allure

from model.group import Group


def test_modify_group(app, db, check_ui):

    with allure.step('I check if exist any group in group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))

    with allure.step('Given a group list from database'):
        old_groups = db.get_group_list()

    with allure.step('Random group selected from list'):
        random_group = random.choice(old_groups)
        index = old_groups.index(random_group)

    with allure.step('Given a new group data'):
        new_group_data = Group(name="New group")
        new_group_data.id = old_groups[index].id

    with allure.step('When I add new data to a group %s from the list' % new_group_data.id):
        app.group.modify_group_by_id(random_group.id, new_group_data)

    with allure.step('Then the new group list is equal to the old list with the added new data %s' % new_group_data ):
        new_groups = db.get_group_list()
        old_groups[index] = new_group_data
        assert len(old_groups) == len(new_groups)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

