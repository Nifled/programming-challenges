/*
https://www.codewars.com/kata/5552101f47fc5178b1000050

Given a positive integer n written as abcd... 
(a, b, c, d... being digits) and a positive integer p we 
want to find a positive integer k, if it exists, such as 
the sum of the digits of n taken to the successive powers 
of p is equal to k * n. In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
*/

const digPow = (n, p) => {
  const digits = ('' + n).split('')

  const sum = digits.reduce((sum, curr, i) => {  
    const tmp = Math.pow(parseInt(curr), p+i)    
    return sum + tmp
  }, 0)
  
  return sum % n === 0 ? sum / n : -1
}
