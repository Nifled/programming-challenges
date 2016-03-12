/*
CHALLENGE DESCRIPTION:

Write a program which reverses the words in an input sentence.

EXAMPLE: 

input: Hello World
output: World Hello
 */
package codeevalchallenges.Easy;

/**
 *
 * @author Erick
 */
public class ReverseWords_easy {
    
    public static void main(String[] args) {
        
        String test = "hello world";
        
        System.out.println(reverseLine(test));
        
    }
    
    public static String reverseLine(String line) {
        
        String[] parts = line.split(" ");
        int n = parts.length;
        String output = "";
        
        for (int i = n-1; i >= 0; i--) {
            output += parts[i] + " ";
        }
        return output;
    }
    
}
