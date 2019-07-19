// https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

/**
 * 
 *  Given an n x n array, return the array elements arranged from outermost 
 *  elements to the middle element, traveling clockwise.

 *  array = [[1,2,3],
 *          [4,5,6],
 *          [7,8,9]]
 *  snail(array) #=> [1,2,3,6,9,8,7,4,5]} array 
 */

// rotate a NxM dimensional array
const rotate = array => {
  const result = [];
  array.forEach(nums => {
    nums.forEach((_, i) => {
      if (!result[i]) result[i] = [];
      result[i].push(nums[nums.length - 1 - i]);
    });
  });
  return result;
};

function snail(array, result = []) {
  if (!array.length) return; // recursive stop
  let [first, ...rest] = array; // chop off the first set of nums from array
  result.push(...first); // push the first
  // rotate the rest of the array and repeat
  snail(rotate(rest), result);

  return result;
}
