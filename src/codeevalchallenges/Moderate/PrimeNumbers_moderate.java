/*
https://www.codeeval.com/open_challenges/46
Prime Numbers

CHALLENGE DESCRIPTION:

Print out the prime numbers less than a given number N. For bonus points your 
solution should run in N*(log(N)) time or better. You may assume that N is always 
a positive integer.

 */
package codeevalchallenges.Moderate;

import static java.lang.Math.sqrt;
/**
 *
 * @author Erick
 */
public class PrimeNumbers_moderate {

    public static void main(String[] args) {
        int n = 20; // Example
        System.out.println(primeNumbersB4(n).substring(0, primeNumbersB4(n).length()-1));
    }

    //returns true if a certain number is PRIME
    public static boolean isPrime(int number) {
        int root = (int) sqrt(number);

        int factorCount = 0;

        for (int i = 1; i <= root; i++) {
            if (number % i == 0) {
                factorCount++;
            }
        }
        return factorCount <= 1;
    }

    //returns array of all prime numbers before n
    public static String primeNumbersB4(int number) { //Prime numbers before
        
        String result = "";
        for (int i = 2; i < number; i++) {
            
            if (isPrime(i)) {
                    result += i + ",";
            }
        }
        return result;
    }
}
