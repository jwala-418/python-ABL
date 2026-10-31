email = input("Enter student email: ")
reg = input("Enter registration ID: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email")
else:
    print("Invalid email")

if len(reg) == 10 and reg.isalnum():
    print("Valid registration ID")
else:
    print("Invalid registration ID")