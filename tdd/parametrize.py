def create_user_id(users: dict[int, str]) -> int:
    if not users:
        return 1
    return max(users.keys()) + 1


def create_user(user_name: str, dict_base: dict[int, str]) -> dict[int, str]:
    new_user_id = create_user_id(dict_base)
    dict_base[new_user_id] = user_name
    return dict_base


def remove_user():
    pass


def list_users():
    pass


def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
