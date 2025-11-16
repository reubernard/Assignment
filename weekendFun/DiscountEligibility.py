total_bill = float(input("Total bill: "))
is_member = input("Member (yes/no): ").lower()

if total_bill >= 1000 and is_member == "yes":
              discount = 0.10
elif total_bill >= 1000:
                discount = 0.05
else:
    discount = 0

final_amount = total_bill - (total_bill * discount)

print("Final amount:", final_amount)
print("Discount applied:", discount * 100, "%")
