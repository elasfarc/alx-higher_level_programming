def say_my_name(first_name, last_name=""):
    valid_args = [type(name) is str for name in [first_name, last_name]]
    if not all(valid_args):
        raise TypeError("{} must be a string".format(
            "first name" if not valid_args[0] else "last name")
        )
    print("My name is {} {}".format(
        first_name, last_name if last_name else "")
    )
