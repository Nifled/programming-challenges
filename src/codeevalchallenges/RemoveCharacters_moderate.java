/*

CHALLENGE DESCRIPTION:

Write a program which removes specific characters from a string.

Input example:  how are you, abc
Output example: how re you

 */
package codeevalchallenges;

/**
 *
 * @author Erick
 */
public class RemoveCharacters_moderate {

    public static void main(String[] args) {

        String line1 = "how are you, abc";
        
        String line2 = "hello world, def";
        
        System.out.println(splitAndRemove(line2));

    }

    public static String splitAndRemove(String x) {
        
        String[] seperate = x.split(", ");
        String sentence = seperate[0];
        char[] lettersToReplace = seperate[1].toCharArray();
        
        String output = null;
        
        for (int i = 0; i < sentence.length(); i++) {
            
            for (int j = 0; j < lettersToReplace.length; j++) {
                
                if (sentence.charAt(i) == lettersToReplace[j]) {
                    output = sentence.replace(sentence.charAt(i), '\0');
                }
                
            }
            
        }
        return output;
    }

}
