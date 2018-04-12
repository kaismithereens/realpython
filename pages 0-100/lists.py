
colors = ["red", "green", "burnt sienna", "blue"]
scores = [10, 8, 9, -2, 9]
my_list = ["one", 2, 3.0]

print(colors[2])
print(my_list[0])
print(scores[0:2])

print(colors)
colors[0] = "burgundy"
colors[2] = "electric indigo"
print(colors)

animals = []
animals.append("lion")
animals.append("tiger")
animals.append("dog")
print(animals)

animals.remove("lion")
animals.remove("tiger")
print(animals)

cities = []
cities.append("New York")
print(cities)
cities.extend(["San Francisco", "Boston", "Copenhagen"])
print(cities)

print(colors.index("blue"))

large_cats = animals
large_cats.append("mouse")
print(animals)

large_cats = animals[:]
large_cats.append("leopard")
print(large_cats)
print(animals)

large_cats = []
large_cats.extend(animals)
print(large_cats)

animals.sort()
print(animals)

two_by_two = [[1,2],[3,4]]
print(two_by_two[1][0])

list = ["I heard you liked lists", ["so i put a list"],["in your list"]]
print(list)

groceries = "eggs, spam, pop rocks, cheese"
grocery_list = groceries.split(",")
print(grocery_list)