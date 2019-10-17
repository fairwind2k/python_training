import allure

from model.group import Group
from timeit import timeit


def test_group_list(app, db):

    with allure.step('Given a group list from home page'):
        ui_list = app.group.get_group_list()

    with allure.step('Given a group list from a database'):
        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, db.get_group_list())

    with allure.step('Then the group list from UI is equal to group list from the database'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)



#  Сравнение затраченного  времени на построение списков из UI и Db
# def test_group_list(app, db):
#     print(timeit(lambda: app.group.get_group_list(), number=1))
#
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#
#     print(timeit(lambda: map(clean, db.get_group_list()), number=10))
#     assert False
