''' The function looks for pattern in a sequence'''


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


def main():
  Text = input()
  pattern = input()
  print(PatternCount(Text, pattern))


if __name__ == "__main__":
  main()



