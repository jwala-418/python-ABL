text = input("Enter a paragraph: ").lower()
words = text.split()

for i in range(len(words)):
    if words[i] in words[:i]:
        continue

    count = words.count(words[i])

    if count > 1:
        print(words[i], "appears", count, "times")
        print("Positions:", end=" ")

        for j in range(len(words)):
            if words[j] == words[i]:
                print(j + 1, end=" ")

        print()