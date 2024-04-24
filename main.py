
import sukhotin as s
import printFunctions as p


# read from this file
fileName = "kalevala.txt"
#fileName = "frankenstein.txt"
#fileName = "aliceInWonderland.txt"
#fileName = "collection.txt"
#fileName = "ShikéyahBidahNa'at'a'í.txt"
#fileName = "verwandlung.txt"
#fileName = "words.txt"
#fileName = "empty.txt"


#███╗   ███╗ █████╗ ██╗███╗   ██╗
#████╗ ████║██╔══██╗██║████╗  ██║
#██╔████╔██║███████║██║██╔██╗ ██║
#██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


def main():

    letters, vowels = s.sukhotinsAlgorithm(fileName)

    p.printReducedTable(letters, vowels)

    print("\n")

    p.printFullTable(letters, vowels)

if __name__ == "__main__":
    
    main()
