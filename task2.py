key = ["A", "B", "C", "D", "A"]
score = 0
correct = 0
wrong = 0
unanswered = 0

for i in range(5):
    ans = input("Enter answer " + str(i + 1) + ": ").upper()

    if ans == "":
        unanswered += 1
    elif ans == key[i]:
        correct += 1
        score += 4
    else:
        wrong += 1
        score -= 1

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)
print("Final score:", score)