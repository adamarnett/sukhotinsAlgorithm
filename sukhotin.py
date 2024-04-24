
from letter import letter

#███████╗██╗   ██╗██╗  ██╗██╗  ██╗ ██████╗ ████████╗██╗███╗   ██╗███████╗
#██╔════╝██║   ██║██║ ██╔╝██║  ██║██╔═══██╗╚══██╔══╝██║████╗  ██║██╔════╝
#███████╗██║   ██║█████╔╝ ███████║██║   ██║   ██║   ██║██╔██╗ ██║███████╗
#╚════██║██║   ██║██╔═██╗ ██╔══██║██║   ██║   ██║   ██║██║╚██╗██║╚════██║
#███████║╚██████╔╝██║  ██╗██║  ██║╚██████╔╝   ██║   ██║██║ ╚████║███████║
#╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝
# █████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗
#██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║
#███████║██║     ██║  ███╗██║   ██║██████╔╝██║   ██║   ███████║██╔████╔██║
#██╔══██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║
#██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║
#╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝


# initLetters   --> Returns a dictionary of letter objects with each letter
#                   in the alphabet. Each key is a string of a letter, and each
#                   value is a letter object to represent that letter.
#                   This allows for easier indexing compared to an array, as
#                   you can use the letter as a string, rather than having to do
#                   math to represent each character.
#                   Below is a graphical representation of the dictionary. It can
#                   be represented more abstractly as a table, which will also be
#                   pictured. Note that both are abbreviated to save space.
#                   To get the overall frequency of one letter in the text, use:
#                       letters[c1].freq()
#                       (where c1 is some letter as a string ie c1="a")
#                   To get the adjacency frequency of one and another in the text, use:
#                       letters[c1].freqOf(c2)
#                       (where c1 is some letter as a string and c2 is another
#                       letter as a string, ie c1="a" and c2="b")
#
#               ┌───────────────────┐
#               |D I C T I O N A R Y|
#               └───────────────────┘
#   String                                Letter Object
#  _|__   __________________________________|___________________________________
# |   |  |                                                                     |
#        name (str)        .adjFreq (dictionary)               .ovrFreq (int)
# "a" :     "a"     {"a":0, "b":0, "c":0, "d":0,  ... "z":0}     0
# "b" :     "b"     {"a":0, "b":0, "c":0, "d":0,  ... "z":0}     0
# "c" :     "c"     {"a":0, "b":0, "c":0, "d":0,  ... "z":0}     0
# "d" :     "d"     {"a":0, "b":0, "c":0, "d":0,  ... "z":0}     0
# ... :     ...                         ...                     ...
# "z" :     "z"     {"a":0, "b":0, "c":0, "d":0,  ... "z":0}     0
#
#
#               ┌─────────┐
#               |T A B L E|
#               └─────────┘
#
#               Letter Object name
#             "a" "b" "c" ... "z"  Sum
#    S       ┌───┬───┬───┬───┬───┐          *Letter Object .adjFreq["b"]
#        "a" │ 0 │ 0*│ 0 │ 0 │ 0 │  0**
#    T       ├───┼───┼───┼───┼───┤         **Letter Object .ovrFreq
#        "b" │ 0 │ 0*│ 0 │ 0 │ 0 │  0
#    R       ├───┼───┼───┼───┼───┤  
#        "c" │ 0 │ 0*│ 0 │ 0 │ 0 │  0
#    I       ├───┼───┼───┼───┼───┤  
#        ... │ 0 │ 0*│ 0 │ 0 │ 0 │  0
#    N       ├───┼───┼───┼───┼───┤  
#        "z" │ 0 │ 0*│ 0 │ 0 │ 0 │  0
#    G       └───┴───┴───┴───┴───┘    
#
#
#
# ret letters - A dictionary. See above.
#
def initLetters(diaeresis, justLen):
    # init letters dictionary
    # {"<letter>" : <letter class>}
    # to access the adjacenct frequency of "a" for "b" use:
    #   letters["b"].freqOf("a")
    # that will return the number of times a is adjacent to b
    letters = {};
    for i in range(26):
        # diaeresis=False, justLen=6
        letters.update({chr(97+i) : letter(chr(97+i),diaeresis, justLen)})
    if(diaeresis):
        letters.update({"ä" : letter("ä",diaeresis, justLen)})
        letters.update({"ö" : letter("ö",diaeresis, justLen)})
        letters.update({"ü" : letter("ü",diaeresis, justLen)})
    
    return letters

# step1 --> Reads the file fileName and records the frequency of all
#               letters read from the file in the letters dictionary.
#               Python is always pass by reference, so no need to return
#               anything. What is passed to the function is modified.
#               Below is a graphical representation of the step utilizing
#               the table format mentioned previously. The text "SMOOTH"
#               is read. Notice that for each time two letters are
#               adjacent to each other, their intersection on the table
#               is incremented by one.
#
#               <E M P T Y>                       S M O O T H                     
#            h   m   o   s   t                 h   m   o   s   t            
#          ┌───┬───┬───┬───┬───┐             ┌───┬───┬───┬───┬───┐          
#        h │ 0 │ 0 │ 0 │ 0 │ 0 │           h │ 0 │ 0 │ 0 │ 0 │ 1 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        m │ 0 │ 0 │ 0 │ 0 │ 0 │           m │ 0 │ 0 │ 1 │ 1 │ 0 │
#          ├───┼───┼───┼───┼───┤   --->      ├───┼───┼───┼───┼───┤
#        o │ 0 │ 0 │ 0 │ 0 │ 0 │           o │ 0 │ 1 │ 2 │ 0 │ 1 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        s │ 0 │ 0 │ 0 │ 0 │ 0 │           s │ 0 │ 1 │ 0 │ 0 │ 0 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        t │ 0 │ 0 │ 0 │ 0 │ 0 │           t │ 1 │ 0 │ 1 │ 0 │ 0 │
#          └───┴───┴───┴───┴───┘             └───┴───┴───┴───┴───┘
#
# param fileName  --> name of file to be read, "words.txt" for example.
# param letters   --> unmodified dictionary returned by initLetters()
# param showErrors  --> bool, prints rejected characters if true
#
def step1(fileName, letters, showErrors):
    # open the text file and read in characters
    # lastChar keeps track of whatever the last read character is
    lastChar = ""
    # open text file and call it txtFile
    with open(fileName, "r") as txtFile:
        # read each char in the file, one at a time
        # on first iteration, char = first char found in file
        # on second iteration, char = second char found in file
        # and so on...
        for char in iter(lambda: txtFile.read(1), ''):
            # only consider alphabetic characters, no punctuation, spaces, etc
            if (char.isalpha()):
                try:
                    # increment the frequency of char
                    letters[char.lower()].incThis()
                    # if not the first iteration of the loop
                    if (lastChar != ""):
                        # increment adjacent frequency of char in lastChar
                        # i.e. if char = "a" and lastChar = "b", increment the number of 
                        #   occurances of "a" next to "b".
                        letters[lastChar].incThat(char.lower())
                        # increment adjacent frequency of lastChar in char
                        #   - vice versa of last operation
                        # i.e. if char = "a" and lastChar = "b", increment the number of 
                        #   occurances of "b" next to "a".
                        letters[char.lower()].incThat(lastChar)

                    # reassign lastChar
                    # if this is not done lastChar will always be ""
                    lastChar = char.lower()

                # except any characters not usually part of the alphabet, like æ or é
                except:
                    # display message about unknown character
                    if (showErrors):
                        print("--------------------")
                        print(f"| REJECTED CHAR: {char} |")
                        print("--------------------")


# step2 --> Clears the fequency of two of the same letter occuring next to each other.
#           That is, for any given letter c, letters[c].freqOf(c) is set to zero, so the
#           frequency of "a" next to "a" is zero, "b" next to "b" is zero, and so on.
#           Below is another graphical representation. Notice that the interseciton of
#           "o" and "o"  changes from two to zero.
#
#                S M O O T H                      S M O O T H     
#            h   m   o   s   t                 h   m   o   s   t  
#          ┌───┬───┬───┬───┬───┐             ┌───┬───┬───┬───┬───┐
#        h │ 0 │ 0 │ 0 │ 0 │ 1 │           h │ 0 │ 0 │ 0 │ 0 │ 1 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        m │ 0 │ 0 │ 1 │ 1 │ 0 │           m │ 0 │ 0 │ 1 │ 1 │ 0 │
#          ├───┼───┼───┼───┼───┤   --->      ├───┼───┼───┼───┼───┤
#        o │ 0 │ 1 │ 2 │ 0 │ 1 │           o │ 0 │ 1 │ 2 │ 0 │ 1 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        s │ 0 │ 1 │ 0 │ 0 │ 0 │           s │ 0 │ 1 │ 0 │ 0 │ 0 │
#          ├───┼───┼───┼───┼───┤             ├───┼───┼───┼───┼───┤
#        t │ 1 │ 0 │ 1 │ 0 │ 0 │           t │ 1 │ 0 │ 1 │ 0 │ 0 │
#          └───┴───┴───┴───┴───┘             └───┴───┴───┴───┴───┘
#           
#
# param letters --> dictionary of letter objects to be modified
#
def step2(letters):
    # set all occurances of double adjacency to zero (ie don't count AA, BB, etc.)
    for char in letters:
        letters[char].clearDouble()

# step3 --> Sums the rows in the table (counts total number of times a letter is 
#           adjacent to other letters) and classifies all letters as consonants.
#           Returns a dictionary of sums for each row (indexed by string like 
#           the letters dictionary from step1) and a dictionary of the type of 
#           each letter - consonant or vowel - which is also indexed by string.
#           Below is a graphical representation using the text "GALES"
#
#                G A L E S                          G A L E S                         
#            a   e   g   l   s                  a   e   g   l   s   Sum 
#          ┌───┬───┬───┬───┬───┐              ┌───┬───┬───┬───┬───┐     
#        a │ 0 │ 0 │ 1 │ 1 │ 0 │            a │ 0 │ 0 │ 1 │ 1 │ 0 │  2
#          ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
#        e │ 0 │ 0 │ 0 │ 1 │ 1 │            e │ 0 │ 0 │ 0 │ 1 │ 1 │  2  
#          ├───┼───┼───┼───┼───┤    --->      ├───┼───┼───┼───┼───┤     
#        g │ 1 │ 0 │ 0 │ 0 │ 0 │            g │ 1 │ 0 │ 0 │ 0 │ 0 │  1  
#          ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
#        l │ 1 │ 1 │ 0 │ 0 │ 0 │            l │ 1 │ 1 │ 0 │ 0 │ 0 │  2  
#          ├───┼───┼───┼───┼───┤              ├───┼───┼───┼───┼───┤     
#        s │ 0 │ 1 │ 0 │ 0 │ 0 │            s │ 0 │ 1 │ 0 │ 0 │ 0 │  1  
#          └───┴───┴───┴───┴───┘              └───┴───┴───┴───┴───┘    
# 
# param letters --> dictionary of letter objects to be modified
#
# ret rowSums   --> dictionary of sums for each row
#                   {<letter as string> : <row sum as int >= 0>}
#
# ret letterTypes   --> dictionary of types of each letter, consonant or vowel
#                       {<letter as string> : <"CONSONANT" or "VOWEL">}
#
def step3(letters):
    rowSums = {}
    letterTypes = {}
    for char in letters:
        rowSums.update({char : letters[char].getSum()})
        letterTypes.update({char : "CONSONANT"})
    return rowSums, letterTypes

# step4 --> Identifies vowels by finding the highest sum of adjacency frequencies.
#           All letters begin as being presumed to be consonants. The first vowel
#           will be whatever has the highest sum. If there's a tie then the letter 
#           that is closer to the beginning of the alphabet will be chosen. That is 
#           actually somewhat of a weakpoint in the algorithm! That is explained 
#           elsewhere though. Once the first vowel is identified, step five begins.
#           All the other letters (which are still presumed to be consonants) have
#           their sum subtracted from by two times the letters adjacency frequency
#           with the recently identified vowel.
#           This process repeats until there are no consonants with a sum greater 
#           than zero. The repeating of this process (the return to step four) is
#           considered step six.
#           A visual example of step four five and six follows, with the text "GALES":
#           ┌──────────────────────────────────────────────────────────────────────────┐ 
#           | STEP FOUR (Left)                                                         |
#           | Select "a" as a vowel because it's tied for greatest sum and is first    |
#           └──────────────────────────────────────────────────────────────────────────┘
#           ┌──────────────────────────────────────────────────────────────────────────┐
#           | Step FIVE (Right)                                                        |
#           | Then, subtract two times the frequency of "a" being adjacent to each of  |
#           | the consonants from each respective consonant's sum                      |
#           └──────────────────────────────────────────────────────────────────────────┘
#                G A L E S                                 G A L E S                         
#            a   e   g   l   s   Sum                    a   e   g   l   s   Sum              
#          ┌───┬───┬───┬───┬───┐                      ┌───┬───┬───┬───┬───┐                  
#        a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel          a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        e │ 0 │ 0 │ 0 │ 1 │ 1 │  2                 e │ 0 │ 0 │ 0 │ 1 │ 1 │  2 - 2 x 0 = 2   
#          ├───┼───┼───┼───┼───┤            --->      ├───┼───┼───┼───┼───┤                  
#        g │ 1 │ 0 │ 0 │ 0 │ 0 │  1                 g │ 1 │ 0 │ 0 │ 0 │ 0 │  1 - 2 x 1 = -1  
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        l │ 1 │ 1 │ 0 │ 0 │ 0 │  2                 l │ 1 │ 1 │ 0 │ 0 │ 0 │  2 - 2 x 1 = 0   
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        s │ 0 │ 1 │ 0 │ 0 │ 0 │  1                 s │ 0 │ 1 │ 0 │ 0 │ 0 │  1 - 2 x 0 = 1   
#          └───┴───┴───┴───┴───┘                      └───┴───┴───┴───┴───┘                  
#           ┌──────────────────────────────────────────────────────────────────────────┐ 
#           | Step SIX                                                                 |
#           | Return to step 4                                                         |
#           └──────────────────────────────────────────────────────────────────────────┘
#           ┌──────────────────────────────────────────────────────────────────────────┐
#           | STEP FOUR - again (Left)                                                 |
#           | Select "e" as a vowel because it's sum is the greatest of remaining      |
#           | possible consonants                                                      |
#           └──────────────────────────────────────────────────────────────────────────┘
#           ┌──────────────────────────────────────────────────────────────────────────┐
#           | Step FIVE - again (Right)                                                |
#           | Then, subtract two times the frequency of "e" being adjacent to each of  |
#           | the consonants from each respective consonant's sum                      |
#           └──────────────────────────────────────────────────────────────────────────┘
#                G A L E S                                 G A L E S                         
#            a   e   g   l   s   Sum                    a   e   g   l   s   Sum              
#          ┌───┬───┬───┬───┬───┐                      ┌───┬───┬───┬───┬───┐                  
#        a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel          a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel          e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel
#          ├───┼───┼───┼───┼───┤            --->      ├───┼───┼───┼───┼───┤                  
#        g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1                 g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1 - 2 x 0 = -1  
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        l │ 1 │ 1 │ 0 │ 0 │ 0 │  0                 l │ 1 │ 1 │ 0 │ 0 │ 0 │  0 - 2 x 1 = -2   
#          ├───┼───┼───┼───┼───┤                      ├───┼───┼───┼───┼───┤                  
#        s │ 0 │ 1 │ 0 │ 0 │ 0 │  1                 s │ 0 │ 1 │ 0 │ 0 │ 0 │  1 - 2 x 1 = -1   
#          └───┴───┴───┴───┴───┘                      └───┴───┴───┴───┴───┘                  
#           ┌──────────────────────────────────────────────────────────────────────────┐ 
#           | Step SIX                                                                 |
#           | Return to step 4                                                         |
#           └──────────────────────────────────────────────────────────────────────────┘
#           ┌──────────────────────────────────────────────────────────────────────────┐
#           | STEP FOUR - again                                                        |
#           | All remaining possible consonants have sums less than or equal to zero   |
#           | so they are all confirmed as consonants, and the algorithm terminates    |
#           └──────────────────────────────────────────────────────────────────────────┘
#               G A L E S                         
#            a   e   g   l   s   Sum              
#          ┌───┬───┬───┬───┬───┐                  
#        a │ 0 │ 0 │ 1 │ 1 │ 0 │  2, vowel        
#          ├───┼───┼───┼───┼───┤                  
#        e │ 0 │ 0 │ 0 │ 1 │ 1 │  2, vowel
#          ├───┼───┼───┼───┼───┤                  
#        g │ 1 │ 0 │ 0 │ 0 │ 0 │ -1, consonant
#          ├───┼───┼───┼───┼───┤   
#        l │ 1 │ 1 │ 0 │ 0 │ 0 │ -2, consonant
#          ├───┼───┼───┼───┼───┤   
#        s │ 0 │ 1 │ 0 │ 0 │ 0 │ -1, consonant
#          └───┴───┴───┴───┴───┘                  
#
# param letters --> dictionary of letter objects to be referenced (not modified)
#
# ret rowSums   --> dictionary of sums for each row
#                   {<letter as string> : <row sum as int >= 0>}
#
# ret letterTypes   --> dictionary of types of each letter, consonant or vowel
#                       {<letter as string> : <"CONSONANT" or "VOWEL">}
#
def step4(letters, rowSums, letterTypes):
    while(rowSums[max(rowSums, key=rowSums.get)] > 0):
        maxChar = max(rowSums, key=rowSums.get)
        letterTypes.update({maxChar : "VOWEL"})
        del rowSums[maxChar]
        step5(letters, rowSums, maxChar)
        step6()

# step5 --> Subtracts two times the frequency of maxChar being adjacent to each of
#           the consonants from each respective consonant's sum. This function is
#           called in step four. See description of step four for further details
#           and a graphic.
#
# param letters --> dictionary of letter objects to be referenced (not modified)
#
# param rowSums --> dictionary of sums for each row
#                   {<letter as string> : <row sum as int >= 0>}
#
# param letterTypes --> dictionary of types of each letter, consonant or vowel
#                       {<letter as string> : <"CONSONANT" or "VOWEL">}
#
def step5(letters, rowSums, maxChar):
    for char in rowSums:
        rowSums[char] -= 2*letters[char].freqOf(maxChar)

# step6 --> The existence of this function in this program is for illustrative
#           purposes only. The sixth step in the algorithm is described as 
#           returning to step four, but python does that four us, since step for
#           is essentially a while loop. See step four for details.
def step6():
    # RETURN TO THE BEGINNING OF THE WHILE LOOP IN STEP 4
    pass

# sukhotinsAlgorithm    --> All of the steps put together! Give it a file of text
#                           to read and it will return the letters dictionary from
#                           before and a list of vowels found in the text!
#
# param fileName    --> Name of file to read. Must be a path. (ie, "./words.txt" or
#                       "/home/user/Desktop/words.txt")
# ret letters   --> dictionary of frequencies of letters, see initLetters for details
#
# ret vowels    --> list of strings representing the vowels that were found
#
def sukhotinsAlgorithm(fileName, diaeresis=False, justLen=6, showErrors=True):
    letters = initLetters(diaeresis, justLen)
    step1(fileName, letters, showErrors)
    step2(letters)
    rowSums, letterTypes = step3(letters)
    step4(letters, rowSums, letterTypes)
    #step5 --> in step4 function
    #step6 --> in step4 function
    vowels = []
    for char in letterTypes:
        if (letterTypes[char] == "VOWEL"):
            vowels.append(char)
    return letters, vowels

