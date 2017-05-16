/*
https://www.codewars.com/kata/moving-zeros-to-the-end/train/javascript/58f58afb7e516331bc000078

Write an algorithm that takes an array and moves all of the
zeros to the end, preserving the order of the other elements.
*/

function pushZero(array, k) {
  for (var i=0; i<k; i++) {
    array.push(0);
  }
}

var moveZeros = function (arr) {
  var newArr = arr.filter(x => x !== 0)
  pushZero(newArr, arr.length - newArr.length)

  return newArr
}

// returns[false,1,1,2,1,3,"a",0,0]
moveZeros([false,1,0,1,2,0,1,3,"a"])
