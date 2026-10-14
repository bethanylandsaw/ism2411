# AI disclosure: I used ChatGPT for guided help understanding functions,
# debugging errors, and checking my work. I typed and tested the code myself

# Question 1:
# The first bug I noticed was that total was being replaced by each sale instead of adding all the sales together
# I found it by looking at the loop and thinking about what the value of total would become each time it ran
# This tells me that when I am debugging, I should look at the individual lines of code to see which part is wrong and fix it

# Question 2:
# apply_discount takes two inputs: a price and a tier, such as gold, silver, bronze, or none
# It applies the discount connected to that tier and returns the new discounted price
# A colleague could use this function without reading the body because they only need to provide a price and tier, and the function returns the discounted price

# Question 3:
# AI disclosure: I used ChatGPT for guided help understanding functions, debugging errors, and checking my work. I typed and tested the code myself
# It built my understanding because it showed me when I did something wrong instead of letting me continue without understanding the mistake

# Exercise 1

# Define calcuation tac function

def calculate_tax(price, rate):
    return price * rate

# Calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax for $250 at 8%: ${tax2:.2f}") # 20.00

# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price

# Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactro into a fucntion
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    after_tax = discounted + tax
    return after_tax


print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
# Bug 1: total is being replaced by each sale instead of adding each sale to the running total
# Bug 2: the while loop goes one index too far and tries to access sales[5], which does not exist
# Bug 3: count increases for every sale instead of only counting sales that meet the required condition, such as sales of $100 or more
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    if sale >= 100:
        count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6
x = 100  # global variable

def double_it():
    x = 999  # local variable
    return x * 2

print(x)
print(double_it())
print(x)
# The x inside the function is local, so changing it does not change the global x outside the function