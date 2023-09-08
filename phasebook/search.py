from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if not args:
        return USERS

    ret = []

    for key, value in args.items():
        if key == "id":
            user_id = int(value) - 1
            if 0 <= user_id < len(USERS):
                ret.append(USERS[user_id])
        elif key == "name":
            value_lower = value.lower()
            temp = [user for user in USERS if value_lower in user["name"].lower()]
            ret.extend(temp)
        elif key == "age":
            age = int(value)
            temp = [user for user in USERS if age - 1 <= int(user["age"]) <= age + 1]
            ret.extend(temp)
        elif key == "occupation":
            value_lower = value.lower()
            temp = [user for user in USERS if value_lower in user["occupation"].lower()]
            ret.extend(temp)

    return remove_duplicates(ret)

def remove_duplicates(users_list):
    unique_users = []
    user_ids = set()
    
    for user in users_list:
        if user["id"] not in user_ids:
            unique_users.append(user)
            user_ids.add(user["id"])
    
    return unique_users