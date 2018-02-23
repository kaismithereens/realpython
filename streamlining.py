name = "Zaphod"
num_heads = 2
num_arms = 3

print(name, "has",str(num_heads), "heads and", str(num_arms), "arms")
print(name+ " has "+str(num_heads)+ " heads and "+ str(num_arms)+ " arms")
print("{} has {} heads and {} arms".format(name, num_heads, num_arms))
print("{0} has {1} heads and {2} arms".format(name, num_heads, num_arms))
print("{2} has {0} heads and {1} arms".format(num_heads, num_arms, name))
print("{0} has {0} heads and {0} arms".format(name, num_heads, num_arms))
print("{name} has {num_heads} heads and {num_arms} arms".format(name="Zaphod", num_heads=3, num_arms=2))

print (f"This is a {num_arms} string") #formatted string

print(f"{name} has {num_heads} heads and {num_arms} arms")