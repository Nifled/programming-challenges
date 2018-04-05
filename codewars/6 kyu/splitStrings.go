/*
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into
pairs of two characters. If the string contains an odd
number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Example:
Solution("abc") //should return ["ab", "c_"]
*/

package kata

import "strings"

func Solution(str string) []string {
	slice := strings.Split(str, "")

	var res []string
	for i := 0; i <= len(slice)-1; i += 2 {
		// Check if last iteration by step 2
		if i == len(slice)-1 {
			if len(slice)%2 != 0 {
				res = append(res, slice[i]+"_")
				break
			}
		}

		res = append(res, slice[i]+slice[i+1])
	}
	return res
}
