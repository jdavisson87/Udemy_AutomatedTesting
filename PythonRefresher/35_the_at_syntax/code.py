import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    # using functools.wraps decorates current function that it is a wrapper for func,
    # and keeps the name and documentation of the passed function. Be sure to decorate the inner function, not the full function

    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


# if you put an @ decorator above a function or definition, that will prevent the function from
# being passed as is, and instead will create and pass through the decorator in one go


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())
