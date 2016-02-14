
package codeevalchallenges;

/**
 *
 * @author Erick
 */
public class LongestWord_easy { //challenge name goes here........

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        String line = "in this sentence the longest word is the 3rd word";
        System.out.println(longestWord(line));
        
    }
    
    //Method that returns the longest word in a given string
    //Time Complexity O(n)
    public static String longestWord(String sentence) {

        String[] words = sentence.split(" ");

        int temp = 0;
        String longest = null;

        for (String word : words) {
            int counter = word.length();
            if (counter > temp) {
                temp = counter;

                longest = word;
            }
        }
        return longest;

    }
    
}
