/*
https://www.codewars.com/kata/56747fd5cb988479af000028

Your job is to return the middle character of a word. If 
the word's length is odd, return the middle character. If 
the word's length is even, return the middle 2 characters.
*/

const getMiddle = str => {
  const n = str.length
  return str.slice(n%2===0 ? Math.floor(n/2-1) : n/2, n/2+1)
}
