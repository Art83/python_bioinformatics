def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = ExtendedGenome[0:(n//2)].count(symbol)

    for i in range(1, n):
# start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

# the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def main():
    with open('E_coli.txt') as inputdata:
        Genome = inputdata.read()
    symbol = input("Enter the symbol or kmer")
    print(FasterSymbolArray(Genome, symbol))


if __name__ == "__main__":
    main()

