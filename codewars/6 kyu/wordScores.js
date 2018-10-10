/*
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

Each letter of a word scores points according to it's position 
in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.
*/

const high = x => {
  const words = x.split(' ')
  
  let max = '', maxLen = 0;
  words.forEach(w => {
    let sum = w.split('').reduce((a, b) => a + (b.charCodeAt() - 96), 0)
    if (sum > maxLen) max = w, maxLen = sum
  })

  return max
}
