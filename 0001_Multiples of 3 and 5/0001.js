function findMultiples(max) {
    var count = 0;
    var i;
    for (i = 0; i < max; i += 3) {
        if (!(i % 5 == 0)) {
            count += i;
        }
    }
    for (i = 0; i < max; i += 5) {
        count += i;
    }
    console.log(count);
}
findMultiples(1000);
