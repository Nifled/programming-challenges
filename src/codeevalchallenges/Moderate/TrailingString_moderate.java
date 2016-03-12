/*
https://www.codeeval.com/open_challenges/32/
TRAILING STRING

CHALLENGE DESCRIPTION:

There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.
 */
package codeevalchallenges.Moderate;

/**
 *
 * @author Erick
 */
public class TrailingString_moderate {
    
    public static void main(String[] args) {
        
        String line = "San Francisco,San Jose";
        
        String[] splitter = line.split(",");
        
        String stringA = splitter[0].trim();
        String stringB = splitter[1].trim();
        
        if (stringA.endsWith(stringB)) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
        
    }
    
}
