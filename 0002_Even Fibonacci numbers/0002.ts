function evenFib(n: Number) {
    let fibNumbers = [1, 2]

    while (true) {
        let f: number = fibNumbers[fibNumbers.length-1] + fibNumbers[fibNumbers.length-2]
        if (f > n) {
            break
        } else {
            fibNumbers.push(f)
            console.log(f)
        }
    }

    let fibEvens = []
    for (let each of fibNumbers) {
        if (each % 2 == 0) {
            fibEvens.push(each)
        }
    }

    let count: number = 0
    for (let each of fibEvens) {
        count += each
    }

    console.log(count)
}

evenFib(4000000);