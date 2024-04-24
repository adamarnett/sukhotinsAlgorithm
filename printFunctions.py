
#██████╗ ██████╗ ██╗███╗   ██╗████████╗    ███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗
#██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝
#██████╔╝██████╔╝██║██╔██╗ ██║   ██║       █████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║   
#██╔═══╝ ██╔══██╗██║██║╚██╗██║   ██║       ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║   
#██║     ██║  ██║██║██║ ╚████║   ██║       ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   
#╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   

# pretty colors --> works on various UNIXes
# IDE/terminal themes may modify the colors a bit
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
    #just = 0
    #for char in letters:
    #    just = max(just, int(str(letters[char].getMaxFreq())))

    # print only characters present in words.txt
    doPrint = ""
    if (vowels != [-1]):
        banner = "             ["
    else:
        banner = "   ["
    for char in letters:
        if (letters[char].freq() > 0):
            doPrint += char
            banner += (char.rjust(letters[char].justLen) + "|")
    banner = banner[:-1] + "]  Sum"
    printFmt(1)
    print(banner)
    for char in doPrint:
        printFmt((doPrint.index(char))%2)
        if (char in vowels):
            print("    VOWEL ", end="")
        elif (vowels != [-1]):
            print("CONSONANT ", end="")
        print(letters[char].reducedJustifiedRepr(doPrint))
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

    #just = JUSTLEN-1
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