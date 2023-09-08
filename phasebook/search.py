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
    if args:
        ret = []
        if len(args) > 0:
            for key, value in args.items():
                if key == "id":
                    if int(value) <= len(USERS):
                        insert(USERS[int(value)-1], ret)
                        
                elif key == "name":
                    temp = [k for k in USERS if value.lower() in k["name"].lower()]
                    insert(temp, ret)
                        
                elif key == "age":
                    temp = [k for k in USERS if int(k["age"]) in range(int(value)-1, int(value)+2)]
                    insert(temp, ret)

                elif key == "occupation":
                    temp = [k for k in USERS if value.lower() in k["occupation"].lower()]
                    insert(temp, ret)

        return ret
    else:
        return USERS
    
def is_exists(user, ret):
     return bool([k["id"] for k in ret if k["id"] == user["id"]]) 

def insert(temp, ret):
    if type(temp)== list:
        for x in temp:
            if not is_exists(x, ret):
                ret.append(x)
    else:
        if not is_exists(temp, ret):
            ret.append(temp)