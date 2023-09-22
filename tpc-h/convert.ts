import { readFileSync, writeFileSync } from 'fs';

const timingRegex = /^(?<index>\d\d?): (?<time>(?:\d|\.)+)/
const headerRegex = /dbgen sf=(?<sf>\d)\N*/

const file = readFileSync("./tpch_benchmark_data.txt", "utf-8").split("\n")

let output = ",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22"

for (const line of file) {
    const timingMatch = line.match(timingRegex)
    const headerMatch = line.match(headerRegex)
    if (timingMatch) {
        const index = timingMatch[1]
        const time = timingMatch[2]
        output += `,${time}`
    } else if (headerMatch) {
        const index = headerMatch[1]
        output += `\n${index}`
    } else {
        console.log("FUUUUUUUCK")
    }
}

writeFileSync("./data.csv", output)
