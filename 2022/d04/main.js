const fs = require('fs');

function readFile(path){
    try {
        return fs.readFileSync(path, 'utf-8')
    } catch (error) {
        console.log(error)
        return null;
    }
}
const solvePuzzleOne = (path)=>{
    let data = []
    let count = 0;

    readFile(path).split('\n').forEach( x => {
        x = x.replace(',', '-').split('-')
        if(x.length == 4) data.push(x);
    })

    data = data.map((a = []) => a.map(b => parseInt(b)))
    data.map(l => {
        let [a,b,x,y] = l;
        if((x >= a  && y <= b) || (a >= x && b <= y)) count += 1;
    })

    console.log(count)
}
const solvePuzzleTwo = (path)=>{
    let data = []
    let count = 0;

    readFile(path).split('\n').forEach( x => {
        x = x.replace(',', '-').split('-')
        if(x.length == 4) data.push(x);
    })

    data = data.map((a = []) => a.map(b => parseInt(b)))
    data.map(l => {
        let [a,b,x,y] = l;
        if((x >= a  && y <= b) || (a >= x && b <= y) || (a >= x && a <= y) || (b >= x && b <= y) || (x >= a && x <= b) || (y >= a && y <= b)) count += 1;
    })

    console.log(count)
}

console.log("puzzle one: ")
solvePuzzleOne("d04/input")
console.log("puzzle two: ")
solvePuzzleTwo("d04/input")
