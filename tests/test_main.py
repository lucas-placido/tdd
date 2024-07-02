import pytest
from tdd.main import create_user_id, create_user, remove_user, list_users


# Example parametrize
@pytest.mark.parametrize(
    ("users_dict,id_user"),
    [
        ({}, 1),
        ({1: "name"}, 2),
    ],
)
def test_create_user_id(users_dict: dict[int, str], id_user: int):
    new_id_user = create_user_id(users_dict)
    assert new_id_user == id_user


# Example 2 parametrize
@pytest.mark.parametrize(
    ("user_name, dict_base, dict_result"),
    [("carl", {}, {1: "carl"}), ("jon", {1: "carl"}, {1: "carl", 2: "jon"})],
)
def test_create_user(
    user_name: str, dict_base: dict[int, str], dict_result: dict[int, str]
):
    new_dict_user = create_user(user_name, dict_base)
    assert new_dict_user == dict_result


def test_remove_user():
    pass


def test_list_users():
    pass
