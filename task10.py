attendance = float(input("Enter attendance percentage: "))
lab = input("Are all labs completed? (yes/no): ").lower()
internal = float(input("Enter internal marks: "))
fees = input("Are fees cleared? (yes/no): ").lower()

eligible = True

if attendance < 75:
    print("Insufficient attendance")
    eligible = False

if lab != "yes":
    print("Laboratory work incomplete")
    eligible = False

if internal < 40:
    print("Insufficient internal marks")
    eligible = False

if fees != "yes":
    print("Fees not cleared")
    eligible = False

if eligible:
    print("Eligible for final examination")
else:
    print("Not eligible for final examination")