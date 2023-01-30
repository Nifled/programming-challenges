// https://leetcode.com/problems/longest-substring-without-repeating-characters/

function lengthOfLongestSubstring(s: string): number {
  let usedChars: Record<string, number> = {}; // hash that stores chars
  let longestLen = 0;
  let startIdx = 0;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    // if the char is repeated (already in `usedChars`) and the index for
    // the char is === start, update start to the last occurence index + 1
    if (usedChars[char] != null && startIdx <= usedChars[char]) {
      // update the window and continue looking for repeats
      startIdx = usedChars[char] + 1;
    } else {
      // if the window length (current index - start) is greater
      // than `longestLen`, update `longestLen`
      if (i - startIdx + 1 > longestLen) {
        longestLen = i - startIdx + 1;
      }
    }

    // store the index for that char
    usedChars[char] = i;
  }

  return longestLen;
}
