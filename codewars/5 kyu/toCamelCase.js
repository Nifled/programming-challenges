/*
https://www.codewars.com/kata/convert-string-to-camel-case/train/javascript

Complete the method/function so that it converts dash/underscore delimited
words into camel casing. The first word within the output should be
capitalized only if the original word was capitalized.
*/

function toCamelCase(str) {

 return str.split(/-|_/).map( function(word, i) {
   if (i==0) return word
   return word.charAt(0).toUpperCase() + word.slice(1)
 }).join('')
}

// returns "TheStealthWarrior"
toCamelCase("The_Stealth_Warrior")
