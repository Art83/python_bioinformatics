# returning a reverse compliment of a strand

def ReverseComplement(Pattern):   
    revPattern = Reverse(Pattern)
    return Complement(revPattern)


def Reverse(Pattern):
    return "".join(reversed(Pattern))


def Complement(Pattern):
    compl = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([compl[base] for base in Pattern])

def main():
    Pattern = "AAAACCCGGT"
    print(ReverseComplement(Pattern))


if __name__ == "__main__":
    main()


