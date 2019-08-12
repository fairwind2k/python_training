from random import randrange
from model.group import Group


def test_delete_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    #  строка выше дублирует нижний код.
    old_groups[index:index+1] = []
    assert old_groups == new_groups
