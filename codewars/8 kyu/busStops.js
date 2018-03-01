/*
https://www.codewars.com/kata/number-of-people-in-the-bus
*/

const number = busStops => busStops.map(x => x[0] - x[1])
  .reduce((a, b) => a + b)
