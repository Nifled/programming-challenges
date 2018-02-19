/*
https://www.codewars.com/kata/57e1e61ba396b3727c000251

Your program will take in a string and clean out all numeric 
characters, and return a string with spacing and special 
characters ~#$%^&!@*():;"'.,? all intact.
*/

const stringClean = s => s.replace(/\d/g, '')
