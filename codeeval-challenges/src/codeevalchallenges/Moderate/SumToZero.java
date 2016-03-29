/*
https://www.codeeval.com/open_challenges/81/
Sum to Zero

CHALLENGE DESCRIPTION:

You are given an array of integers. Count the numbers of ways in which the sum of 4 elements in this array results in zero.
 */
package codeevalchallenges.Moderate;

/**
 *
 * @author Erick
 */
public class SumToZero {
    
    public static void main(String[] args) {
        
        String line = "0,-1,3,-2";
        
        String[] numbers = line.trim().split(",");
        int n = numbers.length;
        
        int totalSums = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    for (int l = k+1; l < n; l++) {
                        int x = Integer.parseInt(numbers[i]);
                        int y = Integer.parseInt(numbers[j]);
                        int z = Integer.parseInt(numbers[k]);
                        int t = Integer.parseInt(numbers[l]);
                        
                        if (x + y + z + t == 0) {
                            totalSums++;
                        }
                        
                    }
                }
            }
        }
        System.out.println(totalSums);
    }
    
}
