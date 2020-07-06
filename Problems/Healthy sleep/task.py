a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print("Normal")
elif h <= a <= b:
    print("Deficiency")
else:
    print("Excess")
