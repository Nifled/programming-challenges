/*
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

Create a function that removes the first and last characters 
of a string. Leave strings with less than two characters alone.
*/

const removeChar = s => s.length <= 2 ? s : s.slice(1, -1)
