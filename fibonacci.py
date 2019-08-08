def fibonacci_nth(n):
	if(n == 0): return 0
	if(n == 1): return 1
	else: return fibonacci_nth(n-1) + fibonacci_nth(n-2)

def fibonacci_series(n):
	return [fibonacci_nth(x) for x in range(n)]

# fibonacci_series(7) returns [0, 1, 1, 2, 3, 5, 8]
