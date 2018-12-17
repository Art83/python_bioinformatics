# Finding all occurences of a ppatern in a string



def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    i = -1
    while True:
        i = Genome.find(Pattern, i+1)
        if i != -1:
            positions.append(i)
        else:
            break
    return positions

#Alternative way

'''
def PatternMatching(Pattern,Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions
'''


def main():
    with open('Vibrio_cholerae.txt') as input:
        Genome = input.read()
    print(PatternMatching("CTTGATCAT",Genome))


if __name__ == "__main__":
    main()
