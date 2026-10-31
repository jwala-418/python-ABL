reg = input("Enter registration ID (e.g. 24CSE101): ")

if len(reg) == 9 and reg[:2].isdigit() and reg[2:5].isalpha() and reg[5:].isdigit():
    year = reg[:2]
    branch = reg[2:5]
    number = reg[5:]

    print("Valid registration ID")
    print("Admission year: 20" + year)
    print("Branch:", branch.upper())
    print("Student number:", number)
else:
    print("Invalid registration ID")