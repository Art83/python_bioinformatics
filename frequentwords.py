#find every key in the frequency map whose corresponding value is equal to the maximum m

def FrequentWords(Text, k):
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    words = [key for key in freq if freq[key] == m]
    return words

def FrequencyMap(Text, k):
    freq = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = freq.get(Pattern,0)+1
    return freq


def main():
    Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    print(FrequentWords(Text, k))


if __name__ == "__main__":
    main()



