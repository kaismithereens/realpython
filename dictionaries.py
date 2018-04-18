phonebook = {"Jenny": "867-5309", "Mike Jones": "281-330-8004", "Destiny": "900-783-3369"}
print(phonebook)
print(phonebook["Jenny"])

phonebook["Obama"] = "202-456-1414"
print(phonebook)

phonebook["Jenny"] = "555-0199"
print(phonebook)

del(phonebook["Destiny"])
print(phonebook)

print(phonebook.keys())
names = phonebook.keys
print(type(names))
names = list(phonebook.keys())
print(type(names))

for contact_name in phonebook:
	print(contact_name, phonebook[contact_name])

if "Jenny" in phonebook:
	print("True")
	
for contact_name in sorted(phonebook):
	print(contact_name, phonebook[contact_name])
	
contacts = {"Jenny": {"cell": "555-0199", "home": "867-5309"}, "Jones": {"home": "281-330-8004"}, "Destiny": {"work": "900-783-3369"}}
print(contacts)
print(contacts["Jenny"]["cell"])

simple_dict = dict(string1="value1", string2=2, string3=3.0)
print(simple_dict)

simple_dict2 = dict([("string1","value1"), ("string2",2), ("string3",3.0)])
print(simple_dict2)