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
        
        /*
        The way the strings are formatted are the way it 
        had to be done on Codeeval, so I had no choice :/
        
        These are just examples, this could also be done
        with scanner, bufferedreader (for console input)
        */        
        
        splitAndRemove(line1);
        splitAndRemove(line2);

    }

    public static void splitAndRemove(String x) { //splits input sentence and characters and removes characters in sentence

        String[] seperate = x.split(", ");
        char[] lettersToRead = seperate[0].toCharArray();
        char[] lettersToReplace = seperate[1].toCharArray();

        for (int i = 0; i < lettersToRead.length; i++) {

            for (int j = 0; j < lettersToReplace.length; j++) {

                if (lettersToRead[i] == lettersToReplace[j]) {
                    lettersToRead[i] = '\0'; //replaces the character i with a null character ''
                    break;
                }
            }
        }
        charArrayToString(lettersToRead);
    }

    public static void charArrayToString(char[] array) { //prints a char array

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
        }
    }
}
