# This decorator will create a function and replace the 
# original function with the secure one so you can't get 
# the admin password without the admin access level
user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

