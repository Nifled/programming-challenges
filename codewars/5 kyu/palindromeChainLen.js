/*
https://www.codewars.com/kata/525f039017c7cd0e1a000a26

Write a method palindrome_chain_length which takes a positive number and
returns the number of special steps needed to obtain a palindrome.
The special step is: "reverse the digits, and add to the original number".
If the resulting number is not a palindrome, repeat the procedure with
the sum until the resulting number is a palindrome.
*/

function reverse(s){
    return Number(s.split("").reverse().join(""));
}

var palindromeChainLength = function(n) {
  if (n === reverse(n.toString())) return 0;
  var steps = 1;
  while (true) {
    var rev = reverse(n.toString())
    var sum = n + rev;
    console.log(sum);

    if (sum === reverse(sum.toString())) break;

    n = sum;
    steps++;
  }
  console.log(steps);
  return steps;
};

// returns 4
palindrome_chain_length(87)
