/*
https://www.codewars.com/kata/56269eb78ad2e4ced1000013

Make a method that finds the next integral perfect square after 
the one passed as a parameter (Recall that an integral perfect 
square is an integer n such that sqrt(n) is also an integer.).

If the parameter is itself not a perfect square, than -1 should be returned. 
*/

const stray = nums => {
    if (nums[0] !== nums[1]) return nums[0]
    for (let i = 0; i <= nums.length; i++) {
      if (nums[i] !== nums[i+1]) {
        return nums[i+1]
      }
    }
  }
