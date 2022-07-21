import json
from pathlib import Path
from utils import validate_password, hash_password
from typing import NewType, List, Dict, Union

User = NewType('user', Dict[str, Union[str, int]])
UserList = NewType('user_list', List[User])


# TODO: add Id to user using UUID

def get_file_path() -> Path:
    path: Path = Path("../data/users/users.json").resolve()

    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch(exist_ok=True)

    return path


def get_users() -> Union[User, List]:
    file_path: Path = get_file_path()

    with file_path.open(mode='r', encoding='utf-8') as file:
        try:
            users = json.load(file)
            return users
        except json.decoder.JSONDecodeError:
            return []


def save_user(user: User) -> None:
    user['password']: str = hash_password(user['password'])

    file_path: Path = get_file_path()
    users: Union[UserList, List] = get_users()

    if [u for u in users if u['username'] == user['username']]:
        print(f"User with username '{user['username']}' already exists")
        return

    users.append(user)

    with file_path.open(mode='w', encoding='utf-8') as file:
        json.dump(users, file)


def get_user_by_username(username: str) -> Union[User, str]:
    users: Union[UserList, List] = get_users()
    user_list: UserList = UserList([u for u in users if u['username'] == username])
    if user_list:
        return user_list[0]
    return f"User with username '{username}' not found"


user_details: User = User({
    "first_name": "Ololade",
    "last_name": "Boyo",
    "email": "asake@gmail.com",
    "phone": "0800404015",
    "username": "ashaks_special",
    "password": "pass123",
    "role": "OWNER"
})

if __name__ == '__main__':
    print("inside user main")
    save_user(user_details)
    print(get_user_by_username('ashaks_special'))
