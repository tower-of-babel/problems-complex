const factorial = (n) => {
    if (n === 0) return 1;
    else return n * factorial(n-1);
}

// oneliner
// const factorial = (n) => (n === 0) ? 1 : n * factorial(n-1);

// tail recursive
