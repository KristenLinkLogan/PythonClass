
# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

#open and read the file, creating a list of abbreviation/name pairs (by splitting at each new line)
with open('../resources/states.txt','r') as states_file:
	states = states_file.read().split("\n")

print states,'\n'

# now we're splitting each element of the list into an embedded mini list containing the abbr and state name
for index, state in enumerate(states): #enumerate loops through the list and gives you an index and the value for each element
	states[index] = state.split("\t") 

print states,'\n'

#I FOUND IT DIFFICULT TO SORT MY SELECT DROPDOWN USING A DICTIONARY, SO I CONTINUED USING THE LIST OF LISTS INSTEAD.
# convert the list of lists into a dictionary. I found the function dict() does this easily enough
# states_dict = dict(states)

# print states_dict,'\n'

print "<select name='State'>"

# for key in sorted(states_dict.keys()):
# 	print '\t<option value="{0}">{1}</option>'.format(key,states_dict.get(key))
# 	# The problem is that this is sorted by the key (abbreviation) and not the value (state name)

# print "</select>"

for state in states:
	print '\t<option value="{0}">{1}</option>'.format(state[0],state[1])

print "</select>\n"

# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

select_state_html = "<select name='State'>"

for state in states:
	select_state_html += '\n\t<option value="{0}">{1}</option>'.format(state[0],state[1])

select_state_html += "\n</select>"

print select_state_html

with open('../output/states.html','w') as states_file:
	states_file.write(select_state_html)

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

state_details_html = ''

#read the file in and convert to a list of rows
with open('../resources/state_info.csv','r') as state_info_file:
	state_info = state_info_file.read().split('\n')

print state_info,'\n' #some of the characters are encoded (e.g., the "-" standing in for no rank in Puerto Rico); also have quotes around text??

#divide into a list of lists for each state (plus a list of the headers)
for index, state_info_detail in enumerate(state_info):
	state_info[index] = state_info_detail.split(',')

print state_info,'\n'

# pop off the header list
state_info_headers = state_info.pop(0)

print state_info,'\n'
print state_info_headers,'\n'

# create separate lists for each type of data??
# create dict for the state info?
# state_info_dict = {}

# format of dict? should the key be rank or state name? 
# (state name more meaningful by human, but rank is how they will be ordered in the table...)

# {
# 	"1": {
# 	"State": "California",
# 	"Population Estimate": "38332521",
# 	"US House Seats": "53",
# 	"Percent of Total Population": "11.91%"
# 	}
# 	"2": {
# 	"State": "Texas",
# 	"Population Estimate": "26448193",
# 	"US House Seats": "36",
# 	"Percent of Total Population": "8.04%"
# 	}
# }


state_details_html = '<table border="1">\n'

# or just loop through state_info and then within the mini lists inside it...
for index_main, state_info_detail in enumerate(state_info): #index_main counts the states, state_info_detail is each state's info
	#print '{0}: {1}'.format(index_main, state_info_detail)
	state_details_html += '''<tr>\n<td colspan="2"> <b>{0}</b> </td>\n</tr>\n<tr>\n<td> Rank: {1} </td>\n
	<td> Percent: {2} </td>\n</tr>\n<tr>\n<td> US House Members: {3} </td>\n<td> Population: {4} </td>\n
	</tr>'''.format(state_info_detail[1],state_info_detail[0],state_info_detail[4],state_info_detail[3],state_info_detail[2])
	# for index_mini, fact in enumerate(state_info_detail): #index_mini counts the facts within each state_info_detail mini list
	 	#print '{0}: {1}'.format(state_info_headers[index_mini],fact)
	 	
state_details_html += '\n</table>'

with open('../output/states_info.html','w') as states_info_file:
	states_info_file.write(state_details_html)

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.






