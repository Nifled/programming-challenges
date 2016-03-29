/*
https://www.codeeval.com/open_challenges/4/
Sum of Primes

CHALLENGE DESCRIPTION:

Write a program which determines the sum of the first 1000 prime numbers.
 */
package codeevalchallenges.Easy;

/**
 *
 * @author Erick
 */
public class SumOfPrimes_easy {

    public static void main(String[] args) {

        int sum = 0;
        int numberOfPrimes = 0;
        int i = 2;
        final int limit = 1000;

        while (true) {

            if (isPrime(i)) {
                sum += i;
                numberOfPrimes++;
            }

            if (numberOfPrimes >= limit) {
                break;
            } 
            i++;
        }

        System.out.println(sum);
    }

    public static boolean isPrime(int number) {
        int root = (int) Math.sqrt(number);

        int factorCount = 0;

        for (int i = 1; i <= root; i++) {
            if (number % i == 0) {
                factorCount++;
            }
        }
        return factorCount <= 1;
    }

}
