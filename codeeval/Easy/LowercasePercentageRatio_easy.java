//https://www.codeeval.com/open_challenges/147/
//Lowercase Percentage Ratio
//
//CHALLENGE DESCRIPTION:
//Your task is to write a program which determines (calculates) the
//percentage ratio of lowercase and uppercase letters.

package codeevalchallenges.Easy;

import java.text.DecimalFormat;

class LowercasePercentageRatio {

    public static void main(String[] args) {
        String line = "thisTHIS";

        char[] stringChars = line.toCharArray();

        int lowers = 0;
        for (char x: stringChars) {
            if (Character.isLowerCase(x)) lowers++;
        }
        DecimalFormat df = new DecimalFormat("0.00");

        double lowerPerc = (double)lowers/stringChars.length *100;
        double upperPerc = (double) 100-lowerPerc;
        System.out.println("lowercase: " + df.format(lowerPerc) + " " +
                            "uppercase: " + df.format(upperPerc));
    }
}