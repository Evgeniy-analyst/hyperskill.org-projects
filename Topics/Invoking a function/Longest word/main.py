word1 = input()
word2 = input()

# How many letters does the longest word contain?
count = 1
if (len(word1) > len(word2)) and count == 1:
    print(len(word1))
    count += 1
else:
    print(len(word2))
    count += 1
