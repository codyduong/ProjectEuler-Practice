function ISOtoDateArray(s: string) {
    //https://stackoverflow.com/questions/14667713/how-to-convert-a-string-to-number-in-typescript
    let year: number = +s.slice(0,4) 
    let month: number = +s.slice(5,7)
    let day: number = +s.slice(8,10)

    let ret = [year, month, day]
    return ret
}

let daysPerMonth: number[] = [31,28,31,30,31,30,31,31,30,31,30,31]

//Days M0, T1, W2, T3, F4, S5, S6
//ISO 8601 - YYYY-MM-DD
function sundaysBetween(y1: string, y2: string) {
    let datesArray: Array<number[]> = [ISOtoDateArray(y1), ISOtoDateArray(y2)]
    let sundayCount: number = 0
    let currentDay: number = 0
    //Year difference
    for (let i: number = datesArray[0][0]; i<=datesArray[1][0]; i++) {
        if ( ((i%4 == 0) && !(i%100 == 0)) || ((i%100 == 0) && (i%400 == 0)) ) {
            daysPerMonth[1] = 29
        } else {
            daysPerMonth[1] = 28
        }
        for (let j: number = 0; j<12; j++) {
            for (let k: number = 0; k<daysPerMonth[j]; k++) {
                currentDay += 1
                currentDay %= 7
                if ((currentDay==6) && (k==0)) {
                    sundayCount += 1
                }
            }
        }
    }
    console.log(sundayCount)
}

sundaysBetween("1901-01-01", "2000-12-31")