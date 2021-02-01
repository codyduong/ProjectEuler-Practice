function findMultiples(max: number){
    let count: number;
    count = 0;

    let i: number;
    for (i = 0; i<=max; i+=3) {
        count+=i;
    }
    for (i = 0; i<=max; i+=5) {
        count+=i;
    }

    console.log(count);
}

findMultiples(1000);