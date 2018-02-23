weight = 0.2
animal = "newt"

print(str(weight),"kg is the weight of the", animal)

print("{} kg is the weight of the {}".format(weight, animal))

print("{0} kg is the weight of the {1}".format(weight,animal))
print ("{1} kg is the weight of the {0}".format(animal,weight))

print("{weight} kg is the weight of the {animal}".format(weight="33",animal="dog"))

print(f"{weight} kg is the weight of the {animal}")