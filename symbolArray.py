def symbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:len(Genome)//2]
    for i in range(len(Genome)):
        array[i] = ExtendedGenome[i:i+(n//2)].count(symbol)
    return array

def main():
    with open('E_coli.txt') as inputdata:
        Genome = inputdata.read()
    symbol = input("Enter the symbol or kmer")
    print(symbolArray(Genome, symbol))


if __name__ == "__main__":
    main()



