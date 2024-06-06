# Login System
# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).
def simple_login(name, password):
    all_users = {"user1": {"name": "Narek", "pass": "nar123"},
                 "user2": {"name": "Karen", "pass": "Kar123"}
                 }



    for key,value in all_users.items():
        if value["name"] == name and value["pass"] == password:
            return "You logged in succesfully"

    raise KeyError("Denied!")

print(simple_login("Kren", "Kar123"))