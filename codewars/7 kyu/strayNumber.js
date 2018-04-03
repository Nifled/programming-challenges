/*
https://www.codewars.com/kata/57f609022f4d534f05000024

You are given an odd-length array of integers, in which all 
of them are the same, except for one single number.

Complete the method which accepts such an array, and returns 
that single different number.
*/

const stray = nums => {
    if (nums[0] !== nums[1]) return nums[0]
    for (let i = 0; i <= nums.length; i++) {
      if (nums[i] !== nums[i+1]) {
        return nums[i+1]
      }
    }
  }
