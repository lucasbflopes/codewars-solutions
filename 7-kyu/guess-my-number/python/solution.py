import re

def guess_my_number(guess, number = '123-451-2345'):
	return re.sub(r"[^%s]" % (guess + '-'), '#', number)