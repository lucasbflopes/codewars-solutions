def get_number_from_string(string):
    return int("".join(c for c in string if c.isdigit()))