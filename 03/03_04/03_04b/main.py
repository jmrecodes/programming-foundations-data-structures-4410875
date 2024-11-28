user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    return { key: value for key, value in user_pref.items() if value is not None }
    # new_user_pref = {}
    # for key, value in user_pref.items():
    #     if (value != None):
    #         new_user_pref[key] = value

    # return new_user_pref


print(update_preferences(user_preferences))
