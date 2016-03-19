# Goal: Using the code from Lesson 3: File handling and dictionaries, create a function that will open a CSV file and return the result as a nested list.


def csv_to_list(filename,delimiter=","):
	
	"""
	Returns a nested list of records from a delimited file
	"""

	with open(filename,'r') as csv_file:
		records = csv_file.read().split("\n")

	# now we're splitting each element of the list into an embedded list containing data elements in each row
	for index, record in enumerate(records): #enumerate loops through the list and gives you an index and the value for each element
		records[index] = record.split(delimiter) 

	return records

#testing the function...

print csv_to_list('../resources/survey.csv'),'\n'
print csv_to_list('../resources/states.csv'),'\n'
print csv_to_list('../resources/state_info.csv'),'\n'
print csv_to_list('../resources/contacts.csv'),'\n'

