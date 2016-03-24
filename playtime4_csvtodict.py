# Challenge Level: Advanced

# Group exercise!

# Scenario: Your organization has put on three events and you have a CSV with details about those events
#           You have the event's date, a brief description, its location, how many attended, how much it cost, and some brief notes
#           File: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/events.csv

# Goal: Read this CSV into a dictionary.

# Your function should return a dictionary that looks something like this. 
# Bear in mind dictionaries have no order, so yours might look a little different!
# Note that I 'faked' the order of my dictionary by using the row numbers as my keys.

# {0: 
#     {'attendees': '12', 
#     'description': 'Film Screening', 
#     'notes': 'Panel afterwards', 
#     'cost': '$10 suggested', 
#     'location': 'In-office', 
#     'date': '1/11/2014'}, 

# 1: 
#     {'attendees': '12', 
#     'description': 'Happy Hour', 
#     'notes': 'Too loud', 
#     'cost': '0', 
#     'location': 'That bar with the drinks', 
#     'date': '2/22/2014'}, 
# 2: 
#     {'attendees': '200', 
#     'description': 'Panel Discussion', 
#     'notes': 'Full capacity and 30 on waitlist', 
#     'cost': '0', 
#     'location': 'Partner Organization', 
#     'date': '3/31/2014'}
# }

from playtime4_csvtolist import csv_to_list

def csv_to_dict(filename,delimiter=","):
	"""
	"""

	# call csv_to_list function to create a list of lists (called 'list_of_lists' from the csv file
	# the list of lists will contain a list with the headers and a list for each row of data

	list_of_lists = csv_to_list(filename)

	# pop off the list of headers

	headers_list = list_of_lists.pop(0)

	#rename the original list just to indicate that it's just got the data in it now.

	data_lists = list_of_lists

	# count how many columns of data there are

	record_count = len(headers_list)

	#initialize dict and a counter

	the_dictionary = {}
	count = 0

	# put the data into an embedded dictionary
	# the first level keys will be the row numbers (1 for each row of data in the csv)
	# the column headers will be the 2nd level keys to access each data point 

	for data_row_index,data_row in enumerate(data_lists):
		record_key = "row {0}".format(data_row_index + 1)
		the_dictionary[record_key] = {}
		while count < record_count:
			for header_index,header in enumerate(headers_list):
				header_key = header
				the_dictionary[record_key][header_key] = data_row[count]
				count = count + 1
		count = 0

	return the_dictionary
				
		
#test the function
print csv_to_dict('../resources/events.csv')


