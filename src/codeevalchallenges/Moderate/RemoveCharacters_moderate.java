/*

 CHALLENGE DESCRIPTION:

 Write a program which removes specific characters from a string.

 Input example:  how are you, abc
 Output example: how re you

 */
package codeevalchallenges.Moderate;

/**
 *
 * @author Erick
 */
public class RemoveCharacters_moderate {

    public static void main(String[] args) {
        
        String line1 = "how are you, abc";

        String line2 = "e hegdelfin molina lopez sanches qlo, def";
        
        /*
        The way the strings are formatted are the way it 
        had to be done on Codeeval, so I had no choice :/
        
        These are just examples, this could also be done
        with scanner, bufferedreader (for console input)
        */        
        
        removeChars(line1);
        removeChars(line2);

    }

    public static void removeChars(String x) { //splits input sentence and characters and removes characters in sentence

        String[] seperator = x.split(", ");
        
        String words = seperator[0];
        String lettersToRemove = seperator[1];
        
        String output = ""; 
        
        for (int i = 0; i < words.length(); i++) {
            
            String currentChar = words.charAt(i) + "";
            
            if (!(lettersToRemove.contains(currentChar))) {
                output += currentChar;
            }
            
        }
        System.out.println(output.trim());
    }
}
