/*

CHALLENGE DESCRIPTION:

Write a program which determines the largest prime palindrome less than 1000.

 */
package codeevalchallenges.Easy;

import static java.lang.Math.sqrt;

/**
 *
 * @author Erick
 */
public class PrimePalindrome_easy {
    
    public static void main(String[] args) {
        
        int highestValue = 0;
        
        for (int i = 1; i <= 1000; i++) {
            if (isPrime(i) && isPalindrome(i)) { //checks if current number i is prime AND a palindrome
                if (i > highestValue) {
                    highestValue = i;
                }
            }
        }
        System.out.println(highestValue);
        
    }
    
    //returns true if a certain number is a PALINDROME
    public static boolean isPalindrome(int number) {
        String palindrome = Integer.toString(number);
        String backwards = ""; 
        
        int length = palindrome.length();
        
        for (int i = (length - 1); i >= 0; i--) {
            backwards += palindrome.charAt(i);
        }
        return palindrome.equals(backwards);
    }
    
    //returns true if a certain number is PRIME
    public static boolean isPrime(int number) {
        int root = (int) Math.sqrt(number);
        
        int factorCount = 0;
        
        for (int i = 1; i <= root; i++) {
            if (number%i == 0) {
                factorCount++;
            }
        }
        return factorCount <= 1;
    }
    
}
