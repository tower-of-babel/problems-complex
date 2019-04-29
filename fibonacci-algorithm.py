from functools import lru_cache

class Fibonacci:
	@lru_cache(maxsize = 1000)
	def fibonacci_nth(self, n):
		if(n == 0): return 0
		if(n == 1): return 1
		else: return self.fibonacci_nth(n-1) + self.fibonacci_nth(n-2)

	def fibonacci_series(self, n):
		return [self.fibonacci_nth(x) for x in range(n+1)]


# print(Fibonacci().fibonacci_series(7))
