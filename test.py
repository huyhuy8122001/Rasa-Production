NOT_SUCCESS = {"success": False}
SUCCESS = {"success": True}


def get_dau_so(data, searchValue):
    if not data:
        return SUCCESS

    dauso = data["DAU_SO"]

    if type(dauso) != list:
        return {"success": False}

    for v in dauso:
        if searchValue == v["NAME"]:
            v.update(SUCCESS)
            return v
