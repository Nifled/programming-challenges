/*
https://www.codewars.com/kata/sudoku-solution-validator/train/javascript/59004571cb3c49d8e4000047

Sudoku Solution Validator Write a function validSolution that accepts
a 2D array representing a Sudoku board, and returns true if it is a
valid solution, or false otherwise. The cells of the sudoku board may
also contain 0's, which will represent empty cells. Boards containing
one or more zeroes are considered to be invalid solutions.
*/

function validSolution(board){
    for (var i = 0; i < board.length; i++) {
        var setCol = new Set()
        var setRow = new Set()
        var setGrid = new Set()

        for (var j = 0; j < board.length; j++) {

        if (j % 3 === 0 && i % 3 === 0) {
            for (var z = 0; z < 3; z++) {
                for (var w = 0; w < 3; w++) {
                    setGrid.add(board[i+z][j+w])
                }
            }
            if (setGrid.size !== board.length) return false
        }

            setCol.add(board[j][i])
            setRow.add(board[i][j])
        }
        if (setCol.size !== board.length || setCol.has(0)) return false
        if (setRow.size !== board.length) return false
    }
    return true
}

// returns true
validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 0, 3, 4, 8],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]])
