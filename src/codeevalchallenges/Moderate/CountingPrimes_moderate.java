/*
https://www.codeeval.com/open_challenges/63/
Counting Primes
CHALLENGE DESCRIPTION:
Given two integers N and M, count the number of prime numbers 
between N and M (both inclusive)
 */
package codeevalchallenges.Moderate;

/**
 *
 * @author Erick
 */
public class CountingPrimes_moderate {

    public static void main(String[] args) {
        
        String line = "20,30"; // Codeeval example
        String[] separator = line.split(",");
        
        int from = Integer.parseInt(separator[0]);
        int to = Integer.parseInt(separator[1]);
        
        int countResult = 0;
        for (int i = from; i <= to; i++) {
            if (isPrime(i)) {
                countResult++;
            }
        }
        System.out.println(countResult);
    }
    
    // Returns true if number IS prime
    public static boolean isPrime(int x) {
        if (x >= 2) {
            int root = (int) Math.sqrt(x);

            int count = 0;
            for (int i = 1; i < root + 1; i++) {
                if (x % i == 0) {
                    count++;
                }
            }
            return count <= 1;
        } 
        return false;
    }
}
