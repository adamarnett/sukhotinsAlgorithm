Math 5248 Final Project  
Adam Arnett, April 2024  
  
## Repo Tour
The repository contains the following:
- README.md
    - You're reading the repo tour
    - Details how to use the program
    - Description and demonstration of Sukhotin's algorithm
- main.py
    - Driver code for the program, run on command line/terminal
-  sukhotin.py
    - Functions that implement the algorithm
    - Description on how the algorithm and the implementation work
- printFunctions.py
    - Functions to print algorithm output to the command line/terminal
- letter.py
    - Object class to represent a single letter, used in sukhotin.py and 
    printFunctions.py
- Several sample .txt files, acquired from https://www.gutenberg.org/
    -  aliceInWonderland.txt, Alice in Wonderland by Lewis Carroll
    -  frankenstein.txt, Frankenstein; Or, The Modern Prometheus by Mary 
    Shelley
    -  kalevala.txt, National Epic of Finland by Elias Lönnrot (in Finnish)
    -  verwandlung.txt, The Metamorphosis by Franz Kafka (in German)

## How To Run The Program
First, download the code as a zip file and unzip it. Then, open the terminal in 
the folder with the extracted files. Once you have a terminal session with the 
same directory as the extracted files, use the following command to use the 
program:  
`python3 ./main.py [textFile]`  

[textFile] should be replaced by whatever .txt file you want to use the 
algorithm on. Note that the program has only been tested on .txt files. If you 
use the following command, it will run the program with the included copy 
of Frankenstein:  
`python3 ./main.py frankenstein.txt`  

The program also has the following options:  
`[cellWidth] - set the width in characters of the cells in the printed table. Must follow immediately after the [textFile] argument.`  
`[-c] - Disable high contrast colors, if the program does not run on MacOS or Windows, using this option may help.`  
`[-d] - Enable use of characters with diaeresis like ä and ö.`  
`[-f] - Enable printing of entire table, including characters not appearing in the text`  
`[-r] - Enable printing of characters not considered by the algorithm like æ.`  
To run the program with all the options, use:  
`python3 ./main.py frankenstein.txt 7 -c -d -f -r`  

    
# Sukhotin's Algorithm
Sukhotin's algorithm is an algorithm designed by the Russian Mathematician Boris
Viktorovich Sukhotin in the 1970s. It's purpose is to determine which characters
in a given text are vowels. It's accuracy can vary depending on the language and
length of the text, but for most texts it will correctly identify all of the 
vowels - possibly with a false positive.
### Assumption
Sukhotin's algorithm works by relying on the following assumption:
>Vowels are more likely to be adjacent to consonants, rather than other vowels.  

For most languages, this is fair to assume. Incorrect results are more likely 
for languages whose phonetic system is not always well represented by the 
script - like english. What is meant by not being well represented by the 
script, is that one letter can produce different sounds based on different 
contexts. For example, think about how the "*C* " is pronounced in each of the 
following words:
> Case  
> Cent  
> Chat  

Languages that do have a phonetic system well represented by their script have 
letters that always produce the same sound, regardless of the context. Some 
languages that fall into this catergory are Russian, Czech, and Finnish.
### Uses
Sukhotin's algorithm was designed to quickly attack any substitution cipher. 
For that type of cipher, it is quite effective. For other types of ciphers, it 
does not work. This is because it also assumes that each letter is put through 
the exact same process for encryption. So, for a polyalphabetic cipher like the
Vigenere cipher, Sukhotin's algorithm would not work, since a single plaintext 
letter may be represented in the ciphertext by different letters depending on 
which part of the key was used to encrypt it.  
A different use of Sukhotin's algorithm is to assist in determining if a text is
actual language or not, and if it is, finding the vowels can help determine what
language the text it. One notable use of the algorithm is on the Voynich 
Manuscript, a one-of-a-kind book written in an also on-of-a-kind script and 
language, dated to the 15th century. So far, nobody has been able to determine 
what language it was written in or decipher the script. Sukhotin's algorithm 
revealed six likely vowels in the script, one of which appears very similar to 
the "*a* " in a Visigothic script used around the 13th century. Based on the 
frequencies and positions in words of the identified vowels, linguists believe 
that the Voynich Manuscript is written in a natural language that is not 
encrypted with a non-substitution cipher.
### Usage
The algorithm is described as having six steps. Each step will be explained and 
an example (the text "GALES") will be demonstrated, step by step.
#### Step One
Count how many times each letter occurs in a text adjacent with another and 
arrange the counts in a matrix with each row and column representing a letter. 
When assigning letters to rows and columns, go in alphabetic order, but feel 
free to exclude letters that don't appear in the text. Notice that once this 
step is complete, the value in each cell is the number of times the label for 
the row and column are adjacent to each other in the text.  
Example:  

               <E M P T Y>                        G A L E S     
            a   e   g   l   s                 a   e   g   l   s
          ┌───┬───┬───┬───┬───┐             ┌───┬───┬───┬───┬───┐
        a │ 0 │ 0 │ 0 │ 0 │ 0 │           a │ 0 │ 0 │ 1 │ 1 │ 0 │
          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
        e │ 0 │ 0 │ 0 │ 0 │ 0 │           e │ 0 │ 0 │ 0 │ 1 │ 1 │
          ├───┼───┼───┼───┼───┤   --->      ├───┼───┼───┼───┼───┤
        g │ 0 │ 0 │ 0 │ 0 │ 0 │           g │ 1 │ 0 │ 0 │ 0 │ 0 │
          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
        l │ 0 │ 0 │ 0 │ 0 │ 0 │           l │ 1 │ 1 │ 0 │ 0 │ 0 │
          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
        s │ 0 │ 0 │ 0 │ 0 │ 0 │           s │ 0 │ 1 │ 0 │ 0 │ 0 │
          └───┴───┴───┴───┴───┘             └───┴───┴───┴───┴───┘

#### Step Two
Fill the diagonals with zeros, such that the matrix shows that no letter occurs 
next to itself. Using "GALES" as an example would show no change since no letter
occurs next to another of itself, so for this step "SMOOTH" will be used as an
example instead. Notice that where the "*Oth*" row intersects the "*Oth*" 
column, the two is changed to a zero.  
Example:

             S M O O T H                      S M O O T H     
         h   m   o   s   t                 h   m   o   s   t  
       ┌───┬───┬───┬───┬───┐             ┌───┬───┬───┬───┬───┐
     h │ 0 │ 0 │ 0 │ 0 │ 1 │           h │ 0 │ 0 │ 0 │ 0 │ 1 │
       ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
     m │ 0 │ 0 │ 1 │ 1 │ 0 │           m │ 0 │ 0 │ 1 │ 1 │ 0 │
       ├───┼───┼───┼───┼───┤   --->      ├───┼───┼───┼───┼───┤
     o │ 0 │ 1 │ 2 │ 0 │ 1 │           o │ 0 │ 1 │ 0 │ 0 │ 1 │
       ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
     s │ 0 │ 1 │ 0 │ 0 │ 0 │           s │ 0 │ 1 │ 0 │ 0 │ 0 │
       ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
     t │ 1 │ 0 │ 1 │ 0 │ 0 │           t │ 1 │ 0 │ 1 │ 0 │ 0 │
       └───┴───┴───┴───┴───┘             └───┴───┴───┴───┴───┘

#### Step Three
Find the sum of each row, and assume that each letter is a consonant. We will 
return to using "GALES" as an example:

               G A L E S                          G A L E S           
           a   e   g   l   s                  a   e   g   l   s   Sum 
         ┌───┬───┬───┬───┬───┐              ┌───┬───┬───┬───┬───┐     
       a │ 0 │ 0 │ 1 │ 1 │ 0 │            a │ 0 │ 0 │ 1 │ 1 │ 0 │  2
         ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
       e │ 0 │ 0 │ 0 │ 1 │ 1 │            e │ 0 │ 0 │ 0 │ 1 │ 1 │  2  
         ├───┼───┼───┼───┼───┤    --->      ├───┼───┼───┼───┼───┤     
       g │ 1 │ 0 │ 0 │ 0 │ 0 │            g │ 1 │ 0 │ 0 │ 0 │ 0 │  1  
         ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
       l │ 1 │ 1 │ 0 │ 0 │ 0 │            l │ 1 │ 1 │ 0 │ 0 │ 0 │  2  
         ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
       s │ 0 │ 1 │ 0 │ 0 │ 0 │            s │ 0 │ 1 │ 0 │ 0 │ 0 │  1  
         └───┴───┴───┴───┴───┘              └───┴───┴───┴───┴───┘    

#### Step Four
Find the first consonant with the highest row sum and assume that letter is 
actually a vowel. If no consonants have a row sum greater than zero, the 
algorithm has completed. In the example, notice that "*a*" is the first letter 
tied for the highest sum, so it is selected.  
Example:

            G A L E S                 
        a   e   g   l   s   Sum       
      ┌───┬───┬───┬───┬───┐           
    a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel 
      ├───┼───┼───┼───┼───┤           
    e │ 0 │ 0 │ 0 │ 1 │ 1 │  2        
      ├───┼───┼───┼───┼───┤           
    g │ 1 │ 0 │ 0 │ 0 │ 0 │  1        
      ├───┼───┼───┼───┼───┤           
    l │ 1 │ 1 │ 0 │ 0 │ 0 │  2        
      ├───┼───┼───┼───┼───┤           
    s │ 0 │ 1 │ 0 │ 0 │ 0 │  1        
      └───┴───┴───┴───┴───┘           

#### Step Five
For each consonant, subtract two times that consonant's number of times it was 
adjacent to the new vowel from that consonants row sum. 
In pseudocode, each consonant's row sum undergoes the following operation:  
`consonant.rowSum = consonant.rowSum - (2 * consonant.numTimesNextTo(newVowel))
`  
In the example, two is 
subtracted from the row sum of "*g*", because "*g*" occurs next to "*a*" once. 


            G A L E S                                  G A L E S                         
        a   e   g   l   s   Sum                    a   e   g   l   s   Sum              
      ┌───┬───┬───┬───┬───┐                      ┌───┬───┬───┬───┬───┐                  
    a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel          a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
      ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
    e │ 0 │ 0 │ 0 │ 1 │ 1 │  2                 e │ 0 │ 0 │ 0 │ 1 │ 1 │  2 - 2 x 0 = 2   
      ├───┼───┼───┼───┼───┤            --->      ├───┼───┼───┼───┼───┤                  
    g │ 1 │ 0 │ 0 │ 0 │ 0 │  1                 g │ 1 │ 0 │ 0 │ 0 │ 0 │  1 - 2 x 1 = -1  
      ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
    l │ 1 │ 1 │ 0 │ 0 │ 0 │  2                 l │ 1 │ 1 │ 0 │ 0 │ 0 │  2 - 2 x 1 = 0   
      ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
    s │ 0 │ 1 │ 0 │ 0 │ 0 │  1                 s │ 0 │ 1 │ 0 │ 0 │ 0 │  1 - 2 x 0 = 1   
      └───┴───┴───┴───┴───┘                      └───┴───┴───┴───┴───┘                  

#### Step Six
Return to step four.  

For illustrative purposes, the remainder of the example is pictured below. In 
the second iteration of step four, "*e*" is selected as a vowel and in the 
second iteration of step five, each remaining consonant's row sum has two times 
that consonant's frequency next to "*e*" subtracted from it. After returning to 
step four in step six, the third iteration of step four finds that no consonants
 remaining have a row sum greater than zero, so the algorithm is finished and 
"*a*" and "*e*" have been identified as vowels - which is correct!

             G A L E S                                 G A L E S                         
         a   e   g   l   s   Sum                    a   e   g   l   s   Sum              
       ┌───┬───┬───┬───┬───┐                      ┌───┬───┬───┬───┬───┐                  
     a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel          a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
       ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
     e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel          e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel
       ├───┼───┼───┼───┼───┤            --->      ├───┼───┼───┼───┼───┤                  
     g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1                 g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1 - 2 x 0 = -1  
       ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
     l │ 1 │ 1 │ 0 │ 0 │ 0 │  0                 l │ 1 │ 1 │ 0 │ 0 │ 0 │  0 - 2 x 1 = -2  
       ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
     s │ 0 │ 1 │ 0 │ 0 │ 0 │  1                 s │ 0 │ 1 │ 0 │ 0 │ 0 │  1 - 2 x 1 = -1  
       └───┴───┴───┴───┴───┘                      └───┴───┴───┴───┴───┘                  
       
            G A L E S                         
         a   e   g   l   s   Sum              
       ┌───┬───┬───┬───┬───┐                  
     a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
       ├───┼───┼───┼───┼───┤                  
     e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel
       ├───┼───┼───┼───┼───┤                  
     g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1, consonant
       ├───┼───┼───┼───┼───┤   
     l │ 1 │ 1 │ 0 │ 0 │ 0 │ -2, consonant
       ├───┼───┼───┼───┼───┤   
     s │ 0 │ 1 │ 0 │ 0 │ 0 │ -1, consonant
       └───┴───┴───┴───┴───┘                  



















