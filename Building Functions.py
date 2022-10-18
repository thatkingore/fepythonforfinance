# IF Statements #

# Equals: x == y
# Not Equal to: x != y
# Less than: x < y
# Greater than: x > y
# Less than or Equal to: x <= y
# Greater than or Equal to: x >= y

x = 5
y = 2
if x > y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")

# Workout 1 #

x = 2
y = 3

if y > x:
    print("y is greater than x")


# Workout 2 #

x = 2
y = 2

if y > x:
    print("y is greater than x")
elif y == x:
    print("y is equal to x")


# Workout 3 #

x = 2
y = 1

if y > x:
    print("y is greater than x")
elif y == x:
    print("y is equal to x")
else:
    print("y is less than x")


# FOR Loops #

# Equals: x == y
# Not Equal to: x != y
# Less than: x < y
# Greater than: x > y
# Less than or Equal to: x <= y
# Greater than or Equal to: x >= y

Bonds = ["Fixed rate bonds", "Floating rate bonds", "Zero coupon bonds"]
for x in Bonds:
    print(x)

# Workout 1 #

terms = ["M&A", "FIG", "FICC"]
for x in terms:
    print(x)
else:
    print("End of list.")


i = 2
while i < 5:
    print(i)
    i = i + 2