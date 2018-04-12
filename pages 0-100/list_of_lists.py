def enrollment_stats(list_of_universities):
	
	number_of_students = []
	tuition_fee = []
	
	for university in list_of_universities:
		number_of_students.append(university[1])
		tuition_fee.append(university[2])
		
	return number_of_students, tuition_fee

def mean(my_list):
	list_sum = 0
	for i in range(len(my_list)):
		list_sum = list_sum + int(my_list[i])
	return int(list_sum/len(my_list))

def median(my_list):
	sort_by_hight = sorted(my_list)
	lenght = len(sort_by_hight)
	if not lenght % 2:
		return (sort_by_hight[int(lenght / 2)] + sort_by_hight[int(lenght / 2 - 1)]) / 2
	return sort_by_hight[int(lenght / 2)]
	
universities = [
	['California Institute of Technology', 2175, 37704],
	['Harvard', 19627, 39849],
	['Massachusetts Institute of Technology', 10566, 40732],
	['Princeton', 7802, 37000],
	['Rice', 5879, 35551],
	['Stanford', 19535, 40569],
	['Yale', 11701, 40500]	
]

stats = enrollment_stats(universities)
#print(stats[0])
#print(stats[1])
print("**************************************")

total_number = 0
for student in stats[0]:
	total_number = total_number + student
print("Total students:", total_number)

total_tuition = 0
for tuitiion in stats[1]:
	total_tuition = total_tuition + tuitiion
print("Total tuition:", total_tuition)
print()
print()

print("Student mean:", mean(stats[0]))
print("Student median:", median(stats[0]))
print()
print()
print("Tuition mean:	$", mean(stats[1]))
print("Student mean:	$", median(stats[1]))
print("**************************************")


