function ISOtoDateArray(s) {
    //https://stackoverflow.com/questions/14667713/how-to-convert-a-string-to-number-in-typescript
    var year = +s.slice(0, 4);
    var month = +s.slice(5, 7);
    var day = +s.slice(8, 10);
    var ret = [year, month, day];
    return ret;
}
var daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
//Days M0, T1, W2, T3, F4, S5, S6
//ISO 8601 - YYYY-MM-DD
function sundaysBetween(y1, y2) {
    var datesArray = [ISOtoDateArray(y1), ISOtoDateArray(y2)];
    var sundayCount = 0;
    var currentDay = 0;
    //Year difference
    for (var i = datesArray[0][0]; i <= datesArray[1][0]; i++) {
        if (((i % 4 == 0) && !(i % 100 == 0)) || ((i % 100 == 0) && (i % 400 == 0))) {
            daysPerMonth[1] = 29;
        }
        else {
            daysPerMonth[1] = 28;
        }
        for (var j = 0; j < 12; j++) {
            for (var k = 0; k < daysPerMonth[j]; k++) {
                currentDay += 1;
                currentDay %= 7;
                if ((currentDay == 6) && (k == 0)) {
                    sundayCount += 1;
                }
            }
        }
    }
    console.log(sundayCount);
}
sundaysBetween("1901-01-01", "2000-12-31");
