/*

CHALLENGE DESCRIPTION:

Print out the prime numbers less than a given number N. For bonus points your 
solution should run in N*(log(N)) time or better. You may assume that N is always 
a positive integer.

 */
package codeevalchallenges.Moderate;

import static java.lang.Math.sqrt;
import java.util.*;

/**
 *
 * @author Erick
 */
public class PrimeNumbers_moderate {
    
    public static void main(String[] args) {
        int n = 20;
        
        int x = primeNumbersB4(n).length; //x = total number of prime numbers
        
        for (int i = 0; i < x - 1; i++) { //prints the numbers all the way to last number
            System.out.print(primeNumbersB4(n)[i] + ",");
        }
        System.out.println(primeNumbersB4(n)[x - 1]); //prints last element without comma
    }
    
    //returns true if a certain number is PRIME
    public static boolean isPrime(int number) {
        int root = (int)sqrt(number);
        
        int factorCount = 0;
        
        for (int i = 1; i <= root; i++) {
            if (number%i == 0) {
                factorCount++;
            }
        }
        return factorCount <= 1;
    }
    
    //returns array of all prime numbers before n
    public static int[] primeNumbersB4(int number) { //Prime numbers before
        List<Integer> list = new ArrayList<>();
        
        for (int i = 2; i < number; i++) {
            
            if (isPrime(i)) {
                list.add(i);
            }
            
        }
        int [] primeNumbers = new int[list.size()];
        
            for (int i = 0; i < primeNumbers.length; i++) {
                
                primeNumbers[i] = list.get(i);
                
            }
        return primeNumbers;
    }
}
