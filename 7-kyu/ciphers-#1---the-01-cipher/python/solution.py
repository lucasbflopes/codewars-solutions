from string import ascii_lowercase as s

encode = lambda string: "".join([x if x not in s else "0" if s.index(x) % 2 == 0 else "1" for x in string.lower()])
