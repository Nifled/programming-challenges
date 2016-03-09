/*
Your task is to write a program which reconstructs each sentence out 
of a set of words and prints out the original sentences.

For example:

2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2

output: 
However, it was not implemented until 1998 and 2000
 */
package codeevalchallenges;

import java.util.Arrays;

/**
 *
 * @author Erick
 */
public class DataRecovery_easy {
    
    public static void main(String[] args) {
        
        String line = "programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9";
        String[] splitParts = line.split(";");
        
        
        String[] arraySentence = splitParts[0].split(" ");
        String[] arrayNumbers = splitParts[1].split(" ");
        
        int count = 0;
        String[] result = new String[arraySentence.length];
        
        for (int i = 0; i < arrayNumbers.length; i++) {
            
            result[i] = arraySentence[count];
            count++;
        }
        
        String[] output = new String[arraySentence.length];
      
        for (int i = 0; i < arrayNumbers.length; i++) {
            
            if (result[i] == null) {
                
                output[i] = result[i];
                
            } else {
                
                output[(Integer.parseInt(arrayNumbers[i])-1)] = result[i];
            }
        }
        
        for (String word : output) {
            System.out.print(word + " ");
        }
    }
    
}
