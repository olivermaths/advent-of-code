import Foundation

enum PuzzleError : Error{
    case NoPathPassed
    case CouldNotReadData
}


extension StringProtocol{
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}


do{
    if CommandLine.arguments.count < 2 {
        throw PuzzleError.NoPathPassed
    }
    let path = CommandLine.arguments[1]
    let data = try String(contentsOfFile: path).split(separator: "\n")
    
    let rows = data.count
    let cols = data[0].count
    let edges = (rows * 2) + ((cols - 2)*2)
    var total = edges
    var scores: [Int] = []
    for row in 1...(rows-2) {
        for col in 1...(cols - 2) {
            let tree = data[row][col]
            var up:    [Character] = []
            var down:  [Character] = []
            var left:  [Character] = []
            var right: [Character] = []
            for i in 0...( row - 1) {
                up.append(data[i][col])
            }
            for i in (row+1)...(rows-1){
                down.append(data[i][col])
            }
            for i in 0...(col - 1){
                left.append(data[row][i])
            }
            for i in (col + 1)...(cols - 1){
                right.append(data[row][i])
            }
            if up.max()! < tree || down.max()! < tree || left.max()! < tree || right.max()! < tree {
                total += 1
            }
            var upScore = 0
            var downScore = 0
            var leftScore = 0
            var rightScore = 0
            
            up.reverse()
            left.reverse()
            for i in up{
                if(i >= tree){
                    upScore += 1
                    break;
                }
                upScore += 1
            }
           
            for i in down{
                if(i >= tree){
                    downScore += 1
                    break;
                }
                downScore += 1
            }
            for i in  left{
                if(i >= tree){
                    leftScore += 1
                    break;
                }
                leftScore += 1
            }
           
            for i in right {
                if(i >= tree){
                    rightScore += 1
                    break;
                }
                rightScore += 1
            }
           

            scores.append(upScore * leftScore * downScore * rightScore)
        }
    }


    print("puzzle one answer: ", total)
    print("puzzle two answer: ", scores.max()!)
    
}catch{
    print("could not solve your puzzle")    
}

