// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference

function sym(...arrays: number[][]): number[] {
  const [arr1, arr2, ...rest] = arrays;

  const uniqueArr1 = arr1.filter((num) => !arr2.includes(num));
  const uniqueArr2 = arr2.filter((num) => !arr1.includes(num));
  const result = [...new Set([...uniqueArr1, ...uniqueArr2])]; // remove dups from result

  if (rest?.length) {
    return sym(result, ...rest);
  }
  return result;
}

const test1 = sym([1, 2, 3], [5, 2, 1, 4]);
const test2 = sym([1, 2, 3, 3], [5, 2, 1, 4]);
const test3 = sym([1, 2, 5], [2, 3, 5], [3, 4, 5]);
