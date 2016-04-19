// https://www.codeeval.com/open_challenges/37
// Pangrams

// CHALLENGE DESCRIPTION:
// The sentence 'A quick brown fox jumps over the lazy dog' contains 
// every single letter in the alphabet. Such sentences are called 
// pangrams. You are to write a program, which takes a sentence, and 
// returns all the letters it is missing (which prevent it from being 
// a pangram). You should ignore the case of the letters in sentence, 
// and your return should be all lower case letters, in alphabetical 
// order. You should also ignore all non US-ASCII characters.In case 
// the input sentence is already a pangram, print out the string NULL.
package codeevalchallenges.Moderate;
/**
 *
 * @author Erick
 */
public class Pangrams_moderate {

    public static void main(String[] args) {

        String line = "A slo[]w yello**w fox cRawls Unde;'pr the pRoaCtive dog";

        char[] lineChars = line.toCharArray();
        String lineLetters = "";
        for (char c : lineChars) {

            if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122)) {
                // Gets only the letters of the line.
                lineLetters += (c+"").toLowerCase();
            }
        }
        String missingLetters = lettersMissing(lineLetters);
        System.out.println((missingLetters.isEmpty()) ? "NULL" : missingLetters);
    }
    public static String lettersMissing(String line) {
        
        String result = "";
        String abc = "abcdefghijklmnopqrstuvwxyz";
        for (char c : abc.toCharArray()) {
            if (!line.contains(c+"")) {
                result += c;
            }
        }
        return result;
    }
}
