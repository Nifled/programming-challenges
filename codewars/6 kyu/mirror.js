/*
https://www.codewars.com/kata/framed-reflection/javascript

You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see, complete with the mirror frame. Example:

'Hello World'

would give:

*********
* olleH *
* dlroW *
*********

***********
* A       *
* racecaR *
***********
*/

const mirror = (s) => {
  const words = s.split(' ')
  let max = Math.max(...(words.map(x => x.length)))

  let res = ''
  res += new Array(max + 5).join('*') + "\n"
  words.forEach( x => {
    let spaces = new Array(max - x.length + 1).join(' ')
    res += "* " + x.split('').reverse().join('') + spaces + " *\n"
  })
  res += new Array(max + 5).join('*')
  
  return res
}
