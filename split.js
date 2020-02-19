// clone of javascripts standard string split metod

function split(s) {
    return s.length === 0 ? []
    : [s[0], ...split(s.slice(1))];
}
