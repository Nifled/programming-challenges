/*
 CHALLENGE DESCRIPTION:

Score: 90/100

 You are given a sorted array of positive integers and a number 'X'. 
 Print out all pairs of numbers whose sum is equal to X. Print out 
 only unique pairs and the pairs should be in ascending order.

 INPUT SAMPLE:

 Your program should accept as its first argument a filename. This 
 file will contain a comma separated list of sorted numbers and then 
 the sum 'X', separated by semicolon. Ignore all empty lines. If no 
 pair exists, print the string NULL e.g.

 input: 1,2,3,4,6;5

 output: 1,4;2,3
 */
package codeevalchallenges;

/**
 *
 * @author Erick
 */
public class NumberPairs_moderate {

    public static void main(String[] args) {

        String line = "1,2,3,4,6;5";
        String[] parts = line.split(";");

        String[] numbers = parts[0].split(",");
        int n = numbers.length;

        int sum = Integer.parseInt(parts[1]);
        String output = "";

        //iterates through numbers
        for (int i = 0; i < n; i++) {

            for (int j = n - 1; j >= i; j--) {

                int x = Integer.parseInt(numbers[i]);
                int y = Integer.parseInt(numbers[j]);

                if (x + y == sum) {
                    output += Integer.toString(x) + "," + Integer.toString(y) + ";";
                }
            }
        }
        
        //checks to see if there are actually numbers that equal the sum
        if (output.length() == 0) {
            System.out.println("NULL");
        } else {
            System.out.println(output.substring(0, output.length()-1));
        }
    }

}
