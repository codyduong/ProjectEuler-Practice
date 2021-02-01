function findMultiples(max) {
    var count;
    count = 0;
    var i;
    for (i = 0; i <= max; i += 3) {
        count += i;
    }
    for (i = 0; i <= max; i += 5) {
        count += i;
    }
    console.log(count);
}
findMultiples(1000);
