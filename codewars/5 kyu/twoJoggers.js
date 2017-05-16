/*
https://www.codewars.com/kata/5274d9d3ebc3030802000165

Your job is to complete the function nbrOfLaps(x, y) that, given the
length of the laps for two joggers, finds the number of laps that
each jogger has to complete before they meet each other again, at the
same time, at the start.
*/

function gcd(a,b) {
  var max = Math.max(a,b);
  var min = a + b - max
  while(true) {

    var r = max % min;
    if (r === 0) return min;

    max = min;
    min = r;

  }
}

var nbrOfLaps = function (x, y) {
  var lcm = (x*y)/gcd(x,y)
  return [lcm/x, lcm/y];
}

// returns [3, 5]
nbrOfLaps(5, 3);
