function evenFib(n) {
    var fibNumbers = [1, 2];
    while (true) {
        var f = fibNumbers[fibNumbers.length - 1] + fibNumbers[fibNumbers.length - 2];
        if (f > n) {
            break;
        }
        else {
            fibNumbers.push(f);
            console.log(f);
        }
    }
    var fibEvens = [];
    for (var _i = 0, fibNumbers_1 = fibNumbers; _i < fibNumbers_1.length; _i++) {
        var each = fibNumbers_1[_i];
        if (each % 2 == 0) {
            fibEvens.push(each);
        }
    }
    var count = 0;
    for (var _a = 0, fibEvens_1 = fibEvens; _a < fibEvens_1.length; _a++) {
        var each = fibEvens_1[_a];
        count += each;
    }
    console.log(count);
}
evenFib(4000000);
