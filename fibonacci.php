<?php declare(strict_types=1);

function fibonacci_nth(int $n): int {
	if($n === 0) return 0;
	if($n === 1) return 1;
	else return fibonacci_nth($n - 2) + fibonacci_nth($n - 1);
}

function fibonacci_series(int $n): array {
	return array_map('fibonacci_nth', range(0, $n));
}

// fibonacci_series(7); returns
