// https://leetcode.com/problems/two-sum/

const twoSum = (nums: number[], target: number): number[] => {
  return nums.reduce<number[]>((acc, current, currentIndex) => {
    for (let i = currentIndex + 1; i < nums.length; i++) {
      if (current + nums[i] === target) {
        acc.push(currentIndex, i);
        return acc;
      }
    }

    return acc;
  }, []);
};

console.log(twoSum([2, 7, 11, 15, 2], 9));
