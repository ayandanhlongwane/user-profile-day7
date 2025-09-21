multiplication-table.py

Single table
num = int(input("Enter a number: "))
print(f"\nMultiplication table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

Bonus: Tables from 1 to 5
print("\nMultiplication tables from 1 to 5")
for n in range(1, 6):
    print(f"\nTable for {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

