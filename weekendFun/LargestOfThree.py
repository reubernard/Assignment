a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print(largest)
