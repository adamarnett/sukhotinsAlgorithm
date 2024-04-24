
import sukhotin as s
import printFunctions as p
import argparse as a
import os.path as o

# read from this file
#fileName = "kalevala.txt"
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


def main(fileName, cellWidth, d, f, r):

    # error checking
    if (fileName[-4:] != ".txt"):
        raise TypeError(f"File {fileName} is not a .txt file")
    if (not o.isfile(fileName)):
        raise OSError(f"File {fileName} not found")
    

    letters, vowels = s.sukhotinsAlgorithm(fileName, d, cellWidth, r)

    print()

    if (f):
        p.printFullTable(letters, vowels)
    else:
        p.printReducedTable(letters, vowels)

    print()
    
    return 0

    

if __name__ == "__main__":
    parser = a.ArgumentParser(description="Find and return the vowels in a given file.")
    parser.add_argument("fileName",
        type=str,
        nargs=1,
        help=".txt file to employ sukhotin's algorithm on."
    )
    parser.add_argument("cellWidth",
        type=int,
        default=6,
        help="Width of one cell in table printed to the console. Optional.",
        const="arg_was_not_given",
        nargs="?"
    )
    parser.add_argument("-d",
        action="store_true",
        help="Flag to enable use of characters with diaeresis like ä and ö. Optional."
    )
    parser.add_argument("-f",
        action="store_true",
        help="Flag to enable printing of entire frequency table including characters that do not appear in the text. Optional."
    )
    parser.add_argument("-r",
        action="store_true",
        help="Flag to enable printing of rejected (unknown) characters that are not considered by the algorithm. Optional."
    )
    
    args = parser.parse_args()
    main(args.fileName[0], args.cellWidth, args.d, args.f, args.r)
