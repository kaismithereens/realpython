birthdays = {}
birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57' 
birthdays['Darth Vader'] = '4/1/41'
print(birthdays)

if 'Yoda' in birthdays:
	print(birthdays['Yoda'])
else:
	birthdays['Yoda'] = 'unknown'
	
if "Darth Vader" in birthdays:
	print(birthdays['Darth Vader'])
else:
	birthdays["Darth Vader"] = 'unknown'
	
for element in sorted(birthdays):
	print(element, birthdays[element])
	
del(birthdays["Darth Vader"])
print(birthdays)

the_other_dictionary = dict([("Luke Skywalker", "5/24/19"), ("Obi-Wan Kenobi", "3/11/57"), ("Darth Vader","4/1/41")])
print(the_other_dictionary)