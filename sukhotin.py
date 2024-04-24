
# true if you would like to consider ä, ö, and ü
UMLAUT = True
# length of justification for printing, makes everything line up if some characters
#   are much more abundant than others
# > 7 causes the row to spill into the next line with the terminal at max width on
#   my 14 inch laptop
JUSTLEN = 6

# read from this file
fileName = "kalevala.txt"
#fileName = "frankenstein.txt"
#fileName = "aliceInWonderland.txt"
#fileName = "collection.txt"
#fileName = "ShikéyahBidahNa'at'a'í.txt"
#fileName = "verwandlung.txt"
#fileName = "words.txt"
#fileName = "empty.txt"


#██████╗ ██████╗ ██╗███╗   ██╗████████╗    ███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗████████╗██╗███╗   ██╗ ██████╗ 
#██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ 
#██████╔╝██████╔╝██║██╔██╗ ██║   ██║       █████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║      ██║   ██║██╔██╗ ██║██║  ███╗
#██╔═══╝ ██╔══██╗██║██║╚██╗██║   ██║       ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║      ██║   ██║██║╚██╗██║██║   ██║
#██║     ██║  ██║██║██║ ╚████║   ██║       ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║      ██║   ██║██║ ╚████║╚██████╔╝
#╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
# pretty colors --> works on various UNIXes
# editor themes will modify the colors a bit
class bcolors:
    HEADER = '\033[95m' 
    OKBLUE = '\033[94m' 
    OKCYAN = '\033[96m' 
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printFmt(input):
    if (input < 2):
        if input:
            print(bcolors.OKCYAN, end="")
        else:
            print(bcolors.FAIL, end="")
    elif (input == 2):
        print(bcolors.FAIL, end="")
    elif (input == 3):
        print(bcolors.OKCYAN, end="")


def printFmtEnd():
    print(bcolors.ENDC, end="")


#██╗     ███████╗████████╗████████╗███████╗██████╗      ██████╗██╗      █████╗ ███████╗███████╗
#██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██║     ██╔══██╗██╔════╝██╔════╝
#██║     █████╗     ██║      ██║   █████╗  ██████╔╝    ██║     ██║     ███████║███████╗███████╗
#██║     ██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗    ██║     ██║     ██╔══██║╚════██║╚════██║
#███████╗███████╗   ██║      ██║   ███████╗██║  ██║    ╚██████╗███████╗██║  ██║███████║███████║
#╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝

# represent a single letter like "a", "b", or "c"
class letter:
    name = ""
    adjacentFrequencies = {}
    frequency = 0;

    def __init__(self, name):
        self = self
        # error checking
        if (len(name) > 1):
            return
        # actual letter, ie "a"
        self.name = name.lower()

        # frequencies of letters adjacent to this one
        self.adjFreq = {}

        # for each letter, init frequency to zero
        # {"<letter>" : <frequency of adjacency>}
        for i in range(26):
            self.adjFreq.update({chr(97+i) : 0})
        if (UMLAUT):
            self.adjFreq.update({"ä" : 0})
            self.adjFreq.update({"ö" : 0})
            self.adjFreq.update({"ü" : 0})
        
        # frequency of this letter in the text
        self.ovrFreq = 0;
    
    def __repr__(self):

        retStr = f"{self.name}: [" 

        for i in range(25):
            retStr += (f"{self.adjFreq[chr(97+i)]}|").rjust(JUSTLEN)

        if (UMLAUT):
            retStr += (f"{self.adjFreq[chr(97+25)]}|").rjust(JUSTLEN)
            äFreq = self.adjFreq["ä"]
            retStr += (f"{äFreq}|").rjust(JUSTLEN)
            öFreq = self.adjFreq["ö"]
            retStr += (f"{öFreq}|").rjust(JUSTLEN)
            üFreq = self.adjFreq["ü"]
            retStr += (f"{üFreq}").rjust(JUSTLEN-1)
        
        retStr += f"]  {self.getSum()}"
        
        return retStr
    
    def justifiedRepr(self, maxLen):
        retStr = f"{self.name}: [" 

        for i in range(25):
            retStr += (f"{self.adjFreq[chr(97+i)]}|").rjust(maxLen)

        if (UMLAUT):
            retStr += (f"{self.adjFreq[chr(97+25)]}|").rjust(maxLen)
            äFreq = self.adjFreq["ä"]
            retStr += (f"{äFreq}|").rjust(maxLen)
            öFreq = self.adjFreq["ö"]
            retStr += (f"{öFreq}|").rjust(maxLen)
            üFreq = self.adjFreq["ü"]
            retStr += f"{üFreq}"

        retStr += f"]  {self.getSum()}"
        
        return retStr
    
    # doRepr --> string of acceptable characters to show like "ABCXYZ"
    # use to not print letters that don't appear at all
    def reducedJustifiedRepr(self, doRepr, maxLen):
        retStr = f"{self.name}: [" 

        for i in range(25):
            if (chr(97+i) in doRepr):
                if(retStr[-1] not in "[|"):
                    retStr += "|"
                retStr += (f"{self.adjFreq[chr(97+i)]}").rjust(maxLen)

        if (chr(97+25) in doRepr):
            retStr += (f"|{self.adjFreq[chr(97+25)]}").rjust(maxLen)
        if (UMLAUT):
            retStr += "|"
            if (chr(228) in doRepr):
                äFreq = self.adjFreq["ä"]
                retStr += f"{äFreq}".rjust(maxLen)
            if (chr(246) in doRepr):
                if (retStr[-1] != "|"):
                    retStr += "|"
                öFreq = self.adjFreq["ö"]
                retStr += f"{öFreq}".rjust(maxLen)
            if (chr(252) in doRepr):
                if (retStr[-1] != "|"):
                    retStr += "|"
                üFreq = self.adjFreq["ü"]
                retStr += f"{üFreq}".rjust(maxLen)
        
        retStr += f"]  {self.getSum()}"
        return retStr

    # get frequency of a given letter c
    def freqOf(self, c):
        return self.adjFreq[c]
    
    # get frequency of this letter in the text
    def freq(self):
        return self.ovrFreq
    
    # increment overall frequency
    def incThis(self):
        self.ovrFreq += 1

    # increment adjacent letter frequency
    def incThat(self, c):
        self.adjFreq[c] += 1

    # clear double adjacent letter (ie, AA = 0, BB = 0, etc)
    def clearDouble(self):
        self.adjFreq[self.name] = 0

    # get maximum length of largest frequency
    # used for print formatting
    def getMaxFreq(self):
        maxLen = 0
        for i in range(26):
            maxLen = max(maxLen, self.adjFreq[chr(97+i)])
        if (UMLAUT):
            maxLen = max(maxLen, self.adjFreq[chr(228)])
            maxLen = max(maxLen, self.adjFreq[chr(246)])
            maxLen = max(maxLen, self.adjFreq[chr(252)])
        return len(str(maxLen))

    # return sum of frequencies for all other letters
    def getSum(self):
        sum = 0
        for i in range(26):
            sum += self.adjFreq[chr(97+i)]
        if (UMLAUT):
            sum += self.adjFreq["ü"]
            sum += self.adjFreq["ä"]
            sum += self.adjFreq["ö"]
        return sum
    

#██████╗ ██████╗ ██╗███╗   ██╗████████╗    ███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗
#██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝    ██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝
#██████╔╝██████╔╝██║██╔██╗ ██║   ██║       █████╗  ██║   ██║██╔██╗ ██║██║     ███████╗
#██╔═══╝ ██╔══██╗██║██║╚██╗██║   ██║       ██╔══╝  ██║   ██║██║╚██╗██║██║     ╚════██║
#██║     ██║  ██║██║██║ ╚████║   ██║       ██║     ╚██████╔╝██║ ╚████║╚██████╗███████║
#╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝

# print table of characters present in text
# pass [-1] to vowels to only show character frequencies
def printReducedTable(letters, vowels=[]):
    # find appropriate justification
    just = 0
    for char in letters:
        just = max(just, int(str(letters[char].getMaxFreq())))

    # print only characters present in words.txt
    doPrint = ""
    if (vowels != [-1]):
        banner = "             ["
    else:
        banner = "   ["
    for char in letters:
        if (letters[char].freq() > 0):
            doPrint += char
            banner += (char.rjust(just) + "|")
    banner = banner[:-1] + "]  Sum"
    printFmt(1)
    print(banner)
    for char in doPrint:
        printFmt((doPrint.index(char))%2)
        if (char in vowels):
            print("    VOWEL ", end="")
        elif (vowels != [-1]):
            print("CONSONANT ", end="")
        print(letters[char].reducedJustifiedRepr(doPrint, just))
        printFmtEnd()
    
    if (vowels != [-1]):
        print("------------------------------------",end="")
        for i in range(len(vowels)):
            print("--",end="")
        print()
        print(f"| The following vowels were found: ",end="")
        for i in range(len(vowels)):
            print(f"{vowels[i]},", end="")
        print("|")
        print("------------------------------------",end="")
        for i in range(len(vowels)):
            print("--",end="")
        if (len(vowels) == 0):
            print("No vowels were found...")
        print()

def printFullTable(letters, vowels=[]):
    # find appropriate justification
    just = 0
    for char in letters:
        just = max(just, int(str(letters[char].getMaxFreq())))

    just = JUSTLEN-1
    if (vowels != [-1]):
        banner = "             ["
    else:
        banner = "   ["
    for char in letters:
        banner += (char.rjust(just) + "|")
    banner = banner[:-1] + "]  Sum"

    printFmt(0)
    print(banner)
    for char in letters:
        # additions beyond ord(char)%2) account for ä (228), ö (246), and ü (252)
        printFmt((ord(char)%2) + int(ord(char)/220) + int(ord(char)/240) + int(ord(char)/250))
        if (char in vowels):
            print("    VOWEL ", end="")
        elif (vowels != [-1]):
            print("CONSONANT ", end="")
        print(letters[char])
        printFmtEnd()

    if (vowels != [-1]):
        print("------------------------------------",end="")
        for i in range(len(vowels)):
            print("--",end="")
        print()
        print(f"| The following vowels were found: ",end="")
        for i in range(len(vowels)):
            print(f"{vowels[i]},", end="")
        print("|")
        print("------------------------------------",end="")
        for i in range(len(vowels)):
            print("--",end="")
        if (len(vowels) == 0):
            print("No vowels were found...")
        print()


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
def initLetters():
    # init letters dictionary
    # {"<letter>" : <letter class>}
    # to access the adjacenct frequency of "a" for "b" use:
    #   letters["b"].freqOf("a")
    # that will return the number of times a is adjacent to b
    letters = {};
    for i in range(26):
        letters.update({chr(97+i) : letter(chr(97+i))})
    if(UMLAUT):
        letters.update({"ä" : letter("ä")})
        letters.update({"ö" : letter("ö")})
        letters.update({"ü" : letter("ü")})
    
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
#
def step1(fileName, letters):
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
                    # do nothing
                    # possible improvement --> consider these anyways? Like æ as "ae"?
                    #pass
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
def sukhotinsAlgorithm(fileName):
    letters = initLetters()
    step1(fileName, letters)
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


#███╗   ███╗ █████╗ ██╗███╗   ██╗
#████╗ ████║██╔══██╗██║████╗  ██║
#██╔████╔██║███████║██║██╔██╗ ██║
#██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


def main():
    letters, vowels = sukhotinsAlgorithm(fileName)

    printReducedTable(letters, vowels)

    print("\n")

    printFullTable(letters, vowels)

if __name__ == "__main__":
    main()
