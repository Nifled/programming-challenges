/*
 https://www.codeeval.com/open_challenges/28/
 String Searching 

 CHALLENGE DESCRIPTION:

 You are given two strings. Determine if the second string is a 
 substring of the first (Do NOT use any substr type library 
 function). The second string may contain an asterisk(*) which 
 should be treated as a regular expression i.e. matches zero or
 more characters. The asterisk can be escaped by a \ char in which
 case it should be interpreted as a regular '*' character. To 
 summarize: the strings can contain alphabets, numbers, * and \ 
 characters.
 */
package codeevalchallenges.Hard;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author Erick
 */
public class StringSearching_hard {

    public static void main(String[] args) {

        String line = "CodeEval,C*Eval"; // Example

        String[] splitter = line.split(",");

        String phrase = splitter[0].trim();
        String stringToCheck = splitter[1].trim();

        Pattern p = Pattern.compile("[^a-z0-9 ]", Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher(stringToCheck);
        boolean b = m.find();  //returns true if there IS a special character in

        if (b) {

            int specialIndex = m.start();
            char specialChar = stringToCheck.charAt(specialIndex);

            String[] splitter2 = stringToCheck.split("\\" + specialChar);

            if (specialIndex == stringToCheck.length() - 1) {
                String onlyLeft = splitter[0];

                if (phrase.contains(onlyLeft)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }

            } else if (specialIndex == 0) {

                String str = stringToCheck;
                StringBuilder sb = new StringBuilder(str);
                sb.deleteCharAt(0); // to replace special character
                
                if (phrase.contains(sb)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }

            } else {

                String left = splitter2[0];
                String right = splitter2[1];

                if (phrase.contains(left) && phrase.contains(right)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }

            }

        } else {

            if (phrase.contains(stringToCheck)) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }

        }

    }

}
//( ͡° ͜ʖ ͡°)   <- supposed to be a lenny face
