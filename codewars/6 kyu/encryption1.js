/*
https://www.codewars.com/kata/57814d79a56c88e3e0000786

For building the encrypted string:
Take every 2nd char from the string, then the other chars, 
that are not every 2nd char, and concat them as new String.
Do this n times!
*/

const encrypt = (text, n) => {
  if (n <= 0 || text == null) return text
  
  let twos = text.split('').filter((x, i) => i % 2 !== 0)
  let ones = text.split('').filter((x, i) => i % 2 === 0)

  return encrypt(twos.concat(ones).join(''), n-1) // recursive
}

function decrypt(encryptedText, n) {
  if (n <= 0 || encryptedText == null) return encryptedText
  
  len = encryptedText.length
  
  let twos = encryptedText.slice(0, len / 2).split('')
  let ones = encryptedText.slice(len / 2).split('')
  
  res = ones.map((x, i) => {
    twos[i] = twos[i] ? twos[i] : ''
    return ones[i] + twos[i]
  }).join('')
  
  return decrypt(res, n-1)
}
