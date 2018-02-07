/*
https://www.codewars.com/kata/56f6ad906b88de513f000d96

Build a function that takes in two arguments (salary, bonus). 
Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If 
bonus is false, the fatcat did not make enough money and must 
receive only his stated salary.
*/

const bonusTime = (salary, bonus) => {
  return bonus ? `£${salary * 10}` : `£${salary}`
}
