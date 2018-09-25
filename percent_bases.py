'''
Calculating percentage of all bases in a sequence
'''

def percentage_bases(genome):
    bases =  ["A", "G", "C", "T"]
    for base in bases:
        print(base,round(genome.count(base)/len(genome),2))



def main():
    genome = input()
    percentage_bases(genome)


if __name__ == "__main__":
    main()


 
