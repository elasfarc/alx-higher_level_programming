def add_integer(a:int, b=98):
	are_type = [n == n and type(n) in [float, int] for n in [a, b]]
	if not all(are_type):
		raise TypeError(f"{'a' if not are_type[0] else 'b'} must be an integer")
	return int(a) + int(b)
