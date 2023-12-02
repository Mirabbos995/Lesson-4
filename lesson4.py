a = 5621557700
b = int(input("Enter the number from 2 to 10: "))
if a % b:
    print("Correct")
else:
    print("Incorrect")

a = 266
b = int(input("Enter the number from 2 to 10: "))
if a % b:
    print("Correct")
else:
    print("Incorrect")






m = int(input("Enter the number of apples in the basket: "))
n = int(input("Enter the number of students in the group: "))

apples_per_student = m // n
apples_remain = m % n

print(f"If {m} apples are distributed among {n} students equally, each student will receive {apples_per_student} apples, and there will be {apples_remain} apples left in the basket.")
