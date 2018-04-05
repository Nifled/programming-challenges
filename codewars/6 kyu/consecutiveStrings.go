/*
https://www.codewars.com/kata/56a5d994ac971f1ac500003e

You are given an array strarr of strings and an integer k. 
Your task is to return the first longest string consisting 
of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", 
  "zas", "theta", "abigail"], 2) --> "abigailtheta"
*/

package kata

func LongestConsec(strarr []string, k int) string {
  if len(strarr) == 0 || k > len(strarr) || k <= 0 {
    return ""
  }
  
  var longest string
  for i := 0; i < len(strarr); i++ {
    joinedStr := strarr[i]
    for j := 1; j < k; j++ {
      if i + j > len(strarr) - 1 { break }
      
      joinedStr += strarr[i + j] // append the consecutive strings
    }
    if len(joinedStr) > len(longest) {
      longest = joinedStr
    }
  }
  return longest
}
