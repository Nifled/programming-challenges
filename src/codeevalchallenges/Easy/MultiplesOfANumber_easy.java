/*
https://www.codeeval.com/open_challenges/18/
Multiples of a Number

CHALLENGE DESCRIPTION:

Given numbers x and n, where n is a power of 2, print out the smallest 
multiple of n which is greater than or equal to x. Do not use division
or modulo operator.
 */
package codeevalchallenges.Easy;

/**
 *
 * @author Erick
 */
public class MultiplesOfANumber_easy {
    
    public static void main(String[] args) {
        
        String line = "17,16";
        String[] numbers = line.split(",");
        
        int x = Integer.parseInt(numbers[0]);
        int n = Integer.parseInt(numbers[1]);
        
        int i = 1;
        while (true) {
            
            long currentNumber = n * i;
            
            if (currentNumber >= x) {
                System.out.println(currentNumber);
                break;
            } else {
                i++;
            }
            
        }
        
        
    }
    
}
