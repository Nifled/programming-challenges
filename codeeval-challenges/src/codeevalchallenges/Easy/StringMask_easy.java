/*

CHALLENGE DESCRIPTION:

You’ve got a binary code which has to be buried among words in order to unconsciously 
pass the cipher. 
Create a program that would cover the word with a binary mask. If, while covering, 
a letter finds itself as 1, you have to change its register to the upper one, if 
it’s 0, leave it as it is. Words are always in lower case and in the same row with 
the binary mask.

 */
package codeevalchallenges.Easy;

/**
 *
 * @author Erick
 */
public class StringMask_easy {
    
    public static void main(String[] args) {
        
        String line = "hello 11001";
        
        System.out.println(mask(line));
        
    }
    public static String mask(String line) {
        
        String[] seperator = line.split(" ");
        String word = seperator[0];
        String binary = seperator[1];
        
        String endOutput = "";

        for (int i = 0; i < word.length(); i++) {
            String tempBinary = binary.substring(i, i + 1);
            String tempWord = word.substring(i, i + 1);
            
            if (tempBinary.equals("1")) {
                endOutput += tempWord.toUpperCase();
            } else {
                endOutput += tempWord;
            }
        }
        return endOutput;
    }
}
