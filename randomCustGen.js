const fs = require("fs");

const weightedRandom = (min, max) => {
    return Math.round(max / (Math.random() * max + min))
}

const calculateOrderPrice = () => {
    let hundreds = (weightedRandom(1, 4) - 1) * 100
    let tens = Math.floor(Math.random() * 100)
    let ones = Math.floor(Math.random() * 10)
    let total = hundreds + tens + ones

    return Math.floor(total / 2 + 10)
}

const calculateYears = () => {
    return Math.abs(
        (weightedRandom(1, 100) / 10 - Math.floor(Math.random() * 5)) / 2
    ).toFixed(1)
}

const calculatePriorRequests = () => {
    let rawNumber = Math.floor(Math.random() * 20) - 10
    if (rawNumber < 0) {
        return 0
    } else return rawNumber
}

const calculateAccountsOnIp = () => {
    let rawNumber = weightedRandom(1, 50) - 10
    if (rawNumber <= 0) {
        return 1
    } else return rawNumber
}

const generateOrderData = () => {
    let stringOut =
        calculateOrderPrice() +
        ',' +
        calculateYears() +
        ',' +
        calculatePriorRequests() +
        ',' +
        calculateAccountsOnIp()
    return stringOut
}

let orderDataOut = ''

for (let i = 0; i <= 500; i++) {
    orderDataOut += generateOrderData() + '\n'
}

console.log(orderDataOut)

fs.writeFileSync('./order-data.csv', orderDataOut)
