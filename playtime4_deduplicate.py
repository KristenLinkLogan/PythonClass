# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

#create a function to create the de-duplicated list (I think we already did this as a group. see remove_duplicates.py)
#create a function to create the list of items that are in both lists

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

#FUNCTIONS I'LL USE

#create a function to convert the contents of the txt files to lists
def txt_to_list(filename,delimiter="\n"):
	
	"""
	Given a text file containing one data value on each line, returns a list of the data in the file
	"""

	with open(filename,'r') as the_file:
		the_list = the_file.read().split(delimiter)

	return the_list

#create a function to merge lists
def merge_lists(list_of_list_names):

	"""
		Takes a list of the names of the lists to merge, and creates one big list containing the data from each of the given lists
	"""

	merged_list = []
	for a_list in list_of_list_names:
		merged_list.extend(a_list)

	return merged_list

#use the function we created in class to remove duplicates:
def remove_duplicates(from_list):

    """ 
        The function list() will convert an item to a list. 
        The function set() will convert an item to a set.
        A set is similar to a list, but all values must be unique.
        Converting a list to a set removes all duplicate values.
        We then convert it back to a list since we're most comfortable working with lists.
    """

    uniqeified_list = list(set(from_list))

    return uniqeified_list

# create a function to write the contents of a list to a text file
def list_to_txt(from_list,filename,delimiter):
	
	"""
	Given a list, writes the items in the list to a specified text file using the delimiter specified. The contents of the file, if it already exists, will be overwritten
	"""

	list_len = len(from_list)
	string = ""

	for index,list_item in enumerate(from_list):
		if index != list_len:
			string += "{0}{1}".format(list_item,delimiter)
		else:
			string += "{0}".format(list_item)

	with open(filename,'w') as the_file:
		the_file.write(string)


# create a function to make a list of duplicates from two other lists
def get_list_of_duplicates(list1,list2):

	"""
	Takes the names of the lists over which to search for duplicates, and creates one list containing the items that are in both lists
	"""

	duplicates_lists = []

	for list1_item in list1:
		for list2_item in list2:
			if list1_item == list2_item:
				duplicates_lists.append(list1_item)

	return duplicates_lists



# THE PROGRAM (USING THE FUNCTIONS)

# create two lists of attendees

film_attendees = txt_to_list('../resources/film_screening_attendees.txt')
happy_hour_attendees = txt_to_list('../resources/happy_hour_attendees.txt')

print film_attendees
print "\n"
print happy_hour_attendees
print "\n"


# put the two lists together to use as input to the remove_duplicates function

merged_attendees_list = merge_lists([film_attendees,happy_hour_attendees])

print merged_attendees_list
print "\n"


# create the deduplicated list of attendees

deduplicated_attendees_list = remove_duplicates(merged_attendees_list)

print deduplicated_attendees_list


# create a new file with the deduplicated list of attendees

list_to_txt(deduplicated_attendees_list,'../output/deduplicated_attendees.txt','\n')

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

both_events_attendees_list = get_list_of_duplicates(film_attendees,happy_hour_attendees)

list_to_txt(both_events_attendees_list,'../output/attended_both.txt','\n')




