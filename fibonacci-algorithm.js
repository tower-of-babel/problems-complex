const fibonacci_nth = (n) => {
    if (n === 0) return 0;
    if (n === 1) return 1;
    else return fibonacci_nth(n-2) + fibonacci_nth(n-1);
}

const fibonacci_series = (n) => {
    if (n === 0) return [fibonacci_nth(0)];
    return [...fibonacci_series(n-1), fibonacci_nth(n)];
}
