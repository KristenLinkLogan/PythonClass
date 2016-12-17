# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

#read the data in and create lists of rows for the data
with open('../resources/all_employees.csv','r') as employees_file:
	employees_list = employees_file.read().split('\n')

with open('../resources/survey.csv','r') as survey_file:
	survey_list = survey_file.read().split('\n')

# convert each list element (comma-delimited strings; the rows) into embedded lists within the larger lists
for emp_index,employee in enumerate(employees_list):
	employees_list[emp_index] = employee.split(',')
for sur_index,survey in enumerate(survey_list):
	survey_list[sur_index] = survey.split(',')

print employees_list,'\n'
print survey_list,'\n'

#pop off the header rows
employees_headers = employees_list.pop(0)
survey_headers = survey_list.pop(0)

print employees_list,'\n'
print survey_list,'\n'
print employees_headers,'\n'
print survey_headers,'\n'

# use dictionaries to store the data from the 2 files
employees_dict = {}
survey_dict = {}

for index,employee in enumerate(employees_list):
	#get the index of the 'name' item in the employees_headers list, and use it to get the name of the employee from employee list
	#this will be the name of the employee in the mini list (employee)
	name = employee[employees_headers.index("name")]
	# this name will be the key and the value will be a dictionary to conatain all of that employee's data
	employees_dict[name] = {}
	#use the other labels to get the values for the other keys to add to this embedded dictionary
	email = employee[employees_headers.index("email")]
	employees_dict[name]["email"] = email
	phone = employee[employees_headers.index("phone")]
	employees_dict[name]["phone"] = phone
	department = employee[employees_headers.index("department")]
	employees_dict[name]["department"] = department
	position = employee[employees_headers.index("position")]
	employees_dict[name]["position"] = position

for index,survey in enumerate(survey_list):
	# the top level keys of the survey_dict will be survey 1, survey 2, etc., and their values will be, initially, an empty dict
	survey_key = "survey {0}".format(index + 1)
	survey_dict[survey_key] = {}
	email = survey[survey_headers.index("email")]
	survey_dict[survey_key]["email"] = email
	twitter = survey[survey_headers.index("twitter")]
	survey_dict[survey_key]["twitter"] = twitter
	github = survey[survey_headers.index("github")]
	survey_dict[survey_key]["github"] = github

print employees_dict,'\n'
print survey_dict,'\n'

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
# Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

# get the email address for each employee from the employees_dict
# see if it's in the survey_dict
# if it is, print out the message including all the employee's survey info

for name, info in employees_dict.items():
	email_address = info.get("email")
	for survey_number, data in survey_dict.items():
		if data.get("email") == email_address:
			print """{0} took the survey! The respondent's contact information is: Twitter: {1}, Github: {2}, Phone: {3}, Email: {4}
			""".format(name,data.get("twitter"),data.get("github"),data.get("phone"),email_address)


# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github

# let's make a copy of employees_dict and we'll add the survey information to this new dictionary
employees_plus_dict = employees_dict

print employees_plus_dict,'\n'

#use the same loop logic as above, but instead of printing out info, let's add the new info to the dict
for name, info in employees_dict.items():
	email_address = info.get("email")
	for survey_number, data in survey_dict.items():
		if data.get("email") == email_address:
			employees_plus_dict[name]["twitter"] = data.get("twitter")
			employees_plus_dict[name]["github"] = data.get("github")


print employees_plus_dict,'\n'

#use the new dictionary to create the output (a string that will be written to a file)
#start out by writing the column headers to the string
employees_text = "Name,Email,Phone,Department,Position,Twitter,Github"

#loop through the dictionary to add each employee as a new line of data
for name, info in employees_plus_dict.items():
	email = info.get("email","")
	phone = info.get("phone","")
	department = info.get("department","")
	position = info.get("position","")
	twitter = info.get("twitter","")
	github = info.get("github","")
	employees_text += "\n{0},{1},{2},{3},{4},{5},{6}".format(name,email,phone,department,position,twitter,github)

print employees_text

with open('../output/all_employees_plus.csv','w') as employees_plus_file:
	employees_plus_file.write(employees_text)
