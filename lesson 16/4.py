class LoginError(Exception):
    pass

def simple_login(name, password):
    all_users = {"user1": {"name": "Narek", "pass": "nar123"},
                 "user2": {"name": "Karen", "pass": "Kar123"}
                 }

    for username, user_data in all_users.items():
        if user_data["name"] == name:
            for key, value in user_data.items():
                if key == "pass" and value == password:
                    return "You logged in successfully!"
            raise LoginError("Wrong password")
    raise LoginError("Username not found")

# Example usage:
try:
    print(simple_login("Karen", "Kar123"))
except LoginError as e:
    print("Login failed:", e)