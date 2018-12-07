'''computing the frequency map of a given string Text and integer k.'''

def FrequencyMap(Text, k):
    freq = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = freq.get(Pattern,0)+1
    return freq


def main():
  Text = input()
  k = int(input())
  print(FrequencyMap(Text, k))


if __name__ == "__main__":
  main()


'''from collections import Counter
# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):	
    return dict(Counter([Text[i:i+k] for i in range(len(Text) - k + 1)])
'''
