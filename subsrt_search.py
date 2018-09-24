'''
Looking for substring in a string with find
'''


def substr_search(genome, substring):
    if genome.find(substring) is not -1:
        print("Yes")
    else:
        print("No")
    

def main():
    genome = input()
    substring = input()
    substr_search(genome, substring)



if __name__ == "__main__":
    main()
