/*

CHALLENGE DESCRIPTION:

Print the odd numbers from 1 to 99. 

*/
package codeevalchallenges;

/**
 *
 * @author Erick
 */
public class OddNumbers_easy {
    
    public static void main(String[] args) {
        printOddNumbers();
    }
    
    public static void printOddNumbers() {
        int limit = 100;
        for (int i = 0; i < limit; i++) {
            
            if (!(i%2 == 0)) {
                System.out.println(i);
            }
            
        }
    }
    
}
