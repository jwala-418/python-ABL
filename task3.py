records = [
    "P101,2,500",
    "P102,3,900",
    "P103,1,250"
]

for record in records:
    parts = record.split(",")

    if len(parts) == 3:
        code = parts[0]
        quantity = parts[1]
        amount = parts[2]

        if quantity.isdigit() and amount.isdigit():
            print("Product:", code)
            print("Quantity:", quantity)
            print("Amount:", amount)
        else:
            print("Malformed record:", record)
    else:
        print("Malformed record:", record)