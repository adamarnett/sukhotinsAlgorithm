
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
    frequency = 0
    diaeresis = False
    justLen = 0

    def __init__(self, name, diaeresis=False, justLen=6):
        self = self
        # error checking
        if (len(name) > 1):
            return
        # actual letter, ie "a"
        self.name = name.lower()

        # frequencies of letters adjacent to this one
        self.adjFreq = {}

        # whether or not to include diaeresis characters
        self.diaeresis = diaeresis

        # justification length for printing
        self.justLen = justLen

        # for each letter, init frequency to zero
        # {"<letter>" : <frequency of adjacency>}
        for i in range(26):
            self.adjFreq.update({chr(97+i) : 0})
        if (self.diaeresis):
            self.adjFreq.update({"ä" : 0})
            self.adjFreq.update({"ö" : 0})
            self.adjFreq.update({"ü" : 0})
        
        # frequency of this letter in the text
        self.ovrFreq = 0;
    
    def __repr__(self):

        retStr = f"{self.name}: [" 

        for i in range(25):
            retStr += (f"{self.adjFreq[chr(97+i)]}|").rjust(self.justLen)

        if (self.diaeresis):
            retStr += (f"{self.adjFreq[chr(97+25)]}|").rjust(self.justLen)
            äFreq = self.adjFreq["ä"]
            retStr += (f"{äFreq}|").rjust(self.justLen)
            öFreq = self.adjFreq["ö"]
            retStr += (f"{öFreq}|").rjust(self.justLen)
            üFreq = self.adjFreq["ü"]
            retStr += (f"{üFreq}").rjust(self.justLen-1)
        else:
            retStr += (f"{self.adjFreq[chr(97+25)]}").rjust(self.justLen-1)
        
        retStr += f"]  {self.getSum()}"
        
        return retStr
    
    def justifiedRepr(self, maxLen):
        retStr = f"{self.name}: [" 

        for i in range(25):
            retStr += (f"{self.adjFreq[chr(97+i)]}|").rjust(maxLen)

        if (self.diaeresis):
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
    def reducedJustifiedRepr(self, doRepr):
        retStr = f"{self.name}: [" 
        maxLen = self.justLen

        for i in range(25):
            if (chr(97+i) in doRepr):
                if(retStr[-1] not in "[|"):
                    retStr += "|"
                retStr += (f"{self.adjFreq[chr(97+i)]}").rjust(maxLen)

        if (chr(97+25) in doRepr):
            retStr += (f"|{self.adjFreq[chr(97+25)]}").rjust(maxLen)
        if (self.diaeresis):
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
        if (self.diaeresis):
            maxLen = max(maxLen, self.adjFreq[chr(228)])
            maxLen = max(maxLen, self.adjFreq[chr(246)])
            maxLen = max(maxLen, self.adjFreq[chr(252)])
        return len(str(maxLen))

    # return sum of frequencies for all other letters
    def getSum(self):
        sum = 0
        for i in range(26):
            sum += self.adjFreq[chr(97+i)]
        if (self.diaeresis):
            sum += self.adjFreq["ü"]
            sum += self.adjFreq["ä"]
            sum += self.adjFreq["ö"]
        return sum