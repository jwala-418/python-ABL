positive = ["good", "excellent", "helpful", "nice"]
negative = ["bad", "poor", "boring", "difficult"]

feedback = input("Enter feedback: ").lower()
pos = 0
neg = 0

words = feedback.split()

for word in words:
    if word in positive:
        pos += 1
    if word in negative:
        neg += 1

score = pos - neg

print("Positive words:", pos)
print("Negative words:", neg)
print("Sentiment score:", score)

if score > 0:
    print("Positive feedback")
elif score < 0:
    print("Negative feedback")
else:
    print("Neutral feedback")