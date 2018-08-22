cat_dictionary = {}

for i in range(1, 101):
	cat_dictionary["cat # " + str(i)] = "No"
	
#print(cat_dictionary)

def put_on_hats():
	for round in range(1, 101):
		for cat in range(1, 101):
			if cat % round == 0:
				if cat_dictionary["cat # " + str(cat)] == "No":
					cat_dictionary["cat # " + str(cat)] = "Yes"
				
				else:
					cat_dictionary["cat # " + str(cat)] = "No"

put_on_hats()

for c, hat in cat_dictionary.items():
	if hat == "Yes":
		print(c, "has a hat.")