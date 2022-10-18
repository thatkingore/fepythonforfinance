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



# WHILE Loops #

# Equals: x == y
# Not Equal to: x != y
# Less than: x < y
# Greater than: x > y
# Less than or Equal to: x <= y
# Greater than or Equal to: x >= y

i = 2
while i < 5:
    print(i)
    i = i + 2

# Workout 1 #

current_assets = 10 # in millions
while current_assets < 70:
    print(current_assets)
    current_assets = current_assets + 10
else:
    print("Exit.")



# Functions #

# Equals: x == y
# Not Equal to: x != y
# Less than: x < y
# Greater than: x > y
# Less than or Equal to: x <= y
# Greater than or Equal to: x >= y

def job_role (department):
    print("I work in the " + department + " deparment.")

job_role("Risk")

# Workout 1 #

def square(s):
    print("The square of " + str(s) + " is " + str(s ** 2))

square(2)
square(3486387)
# A function that calculates the square of any number


# Workout 2 #

def cube(c):
    print("The cube of " + str(c) + " is " + str(c ** 3))

cube(2)
cube(3486387)
# A function that calculates the cube of any number


# Workout 3 #

def divide_by_two(d_2):
    print("Dividing " + str(d_2) + " by 2 gives " + str(d_2 / 2))

divide_by_two(2)
divide_by_two(3486387)
# A function that divides any number by 2
