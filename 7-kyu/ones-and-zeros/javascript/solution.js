const binaryArrayToNumber = arr => arr.reduce((sum, bit, idx) => sum + (bit << (arr.length - idx - 1)), 0)