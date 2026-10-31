days = int(input("Enter number of days (28-31): "))
start = int(input("Starting weekday (0=Mon, 6=Sun): "))

if 28 <= days <= 31 and 0 <= start <= 6:
    print("Mon Tue Wed Thu Fri Sat Sun")

    for i in range(start):
        print("    ", end="")

    for day in range(1, days + 1):
        print("%3d" % day, end=" ")

        if (start + day) % 7 == 0:
            print()

    print()
else:
    print("Invalid input")
    